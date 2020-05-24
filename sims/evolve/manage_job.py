"""When run this script executes system calls (uses the subprocess module) to do these actions:
    1- copy the generated population synthesis script contained in sims/properties/outputs/script.py to the Unige Baobab cluster at user@baobab2.hpc.unige.ch:/~/POSYDON/PopSyn
    2- write slurm script (with email adress contained as parameter) and send to cluster
    3- establish ssh connection to the cluster
    4- activate conda environment
    5- run slurm script (with sbatch)
"""
import subprocess, os, datetime
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "posydon.settings")

#GLOBAL PATH VARIABLES
REMOTE_USR = 'stahle8' #will later be web_app user
HOST = '@baobab2.hpc.unige.ch'  #BAOBAB cluster adress
#these are the directories where simulation output files are located (see get_rmt_sim_dir(pk) and get_lcl_sim_dir(pk)    functions at end of script for retrieving the corresponding directory for one simulation)
REMOTE_DIR = REMOTE_USR+HOST+':~/POSYDON/PopSyn/'
LOCAL_DIR = os.path.join(settings.BASE_DIR, 'sims/evolve/outputs/')

def run_sim(email, pk):
    """Called by SimEvolView, when a user wants to run a simulation. This function will handle sending the relevant scripts to the cluster, and execute the binary evolution script from the remote server. Additionally, generates two log files for the standard output and error streams during the remote execution.
    Executes the following actions using the subprocess module:
        1- copy the generated population synthesis script contained in sims/properties/outputs/<pk>/script.py to the Unige Baobab cluster at user@baobab2.hpc.unige.ch:/~/POSYDON/PopSyn/<pl>/
        2- write slurm script (with email adress contained as parameter) and send to cluster. Uses the helper function write_slurm(email).
        3- establish ssh connection to the cluster and do:
            3.1- activate conda environment
            3.2- run slurm script (with sbatch)
            Redirects stderr/stdout to log files.

    Parameters
    ----------
    email : string
        User's email adress specified for job notification. Used to generate slurm script.
    pk : int
        Represents the (unique) primary key of the SimProp object from which a simulation has been run.

    Returns
    -------
    string
        Path to the generated local results directory.

    """


    #PATH INITIALISATION
    remote_sim_dir = get_rmt_sim_dir(pk)
    local_sim_dir = get_lcl_sim_dir(pk)
    log_err = local_sim_dir+'err.txt'
    log_out = local_sim_dir+'out.txt'
    host_sim_dir = "~/POSYDON/PopSyn/"+str(pk) #sim dir path on remote host

    #EXECUTE SUBPROCESSES

    #0 initialize directories with primary key
    #create (unique) local sim outputs directory
    if not os.path.exists(local_sim_dir):
        os.makedirs(local_sim_dir)
    #create (unique) remote simdirectory if not exists
    cmd = "mkdir -p "+host_sim_dir
    proc = subprocess.run(['ssh', '-T', REMOTE_USR+HOST, cmd])

    #1 copy generate python script to cluster
    script_path = os.path.join(settings.BASE_DIR, 'sims/properties/outputs/'+str(pk)+'/script.py')
    copy_py_proc = subprocess.run(['scp', script_path, remote_sim_dir])

    #2 edit slurm script to incorportate email
    slurm_path = local_sim_dir+'run-script.slurm'
    write_slurm(slurm_path, email)
    # copy run-script.slurm to cluster
    copy_slurm_proc = subprocess.run(['scp', slurm_path, remote_sim_dir])

    #3 connect to ssh server
    #will connect to ssh, then write subsequent commands to the stdin stream
    with open(log_out, 'w') as out, open(log_err, 'w') as err: #open log files context
        ssh_proc = subprocess.Popen(["ssh", '-T', REMOTE_USR+HOST],
                            stdin =subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            bufsize=0)

        # Send ssh commands to stdin
        commands = """conda activate env
cd """+host_sim_dir+"""
sbatch run-script.slurm
"""
        out_string, err_string = ssh_proc.communicate(commands)
        out.write(out_string)
        err.write(err_string)





def pull_results(pk):
    """Copies the .pkl results file corresponding to the simulation with id 'pk' (primary key) from the cluster to the local server when a user wants to retrieve it. Function is called from the SimResultsView view handler.

    Parameters
    ----------
    pk : int
        Represents the (unique) primary key of the SimProp object from which a simulation has been run.

    Returns
    -------
    string
        File path of the results file.

    """
    #PATH INITIALISATION
    remote_results_path = get_rmt_sim_dir(pk)+'BBHs-population.pkl'
    local_results_path = get_lcl_sim_dir(pk)+'BBHs-population.pkl'
    try:
        proc = subprocess.run(['scp', remote_results_path, local_results_path])
    except FileNotFoundError:
        print("No results file found!")
    except Exception as e:
        print(e)

    return local_results_path


def gen_log(pk):
    """Generates one log.txt file by appending the stderr and stdout log files compiled during a simulation run on the cluster.

    Parameters
    ----------
    pk : int
        Represents the (unique) primary key of the SimProp object from which a simulation has been run.

    Returns
    -------
    string
        Path of generated log file.

    """
    #PATH INITIALISATION
    local_sim_dir = get_lcl_sim_dir(pk)
    log_path = local_sim_dir+'log.txt'

    #import err and out files from the cluster after job completion
    import_logfiles(pk)

    ## TODO: append retrieved files to the local out and err log files generated during ssh connection (in run_sim)

    with open(log_path, 'w+') as log:
        current_date = datetime.datetime.now()
        date_string = '{:%m/%d/%y %H:%M}'.format(current_date)
        header = "LOG FILE COMPILED ON  "+date_string+"\nSIM ID: "+str(pk)+"""
----------------------------------------------
"""
        log.write(header)
        log.write("OUT STREAM:\n\n")
        #append out and err files to one log file
        with open(local_sim_dir+'out.txt', 'r') as out:
            log.write(out.read())   #append webserver-side output log
        with open(local_sim_dir+'job_out.out', 'r') as job_out:
            log.write(job_out.read())   #append cluster job output log
        log.write("""
----------------------------------------------
ERR STREAM:

""")
        with open(local_sim_dir+'err.txt', 'r') as err:
            log.write(err.read())   #append webserver-side error log
        with open(local_sim_dir+'job_err.err', 'r') as job_err:
            log.write(job_err.read())   #append cluster job error log

    return log_path


###################################
#HELPER FUNCTIONS
def get_rmt_sim_dir(pk):
    return REMOTE_DIR+str(pk)+'/'
def get_lcl_sim_dir(pk):
    return LOCAL_DIR+str(pk)+'/'

def write_slurm(path, email):
    #Helper function: generate slurm script at path
    #with email as param for notifications
    with open(path, 'w') as f:
        buffer = """#!/bin/bash
#
#Specify email adress for notification:
#SBATCH --mail-user="""+email+"""
#SBATCH --mail-type=ALL
#SBATCH --account=fragkos
#
#SBATCH --job-name=pop-syn
#SBATCH --output=log_%a.out
#SBATCH --error=log_%a.err
#SBATCH --partition=debug-EL7
#SBATCH --ntasks=1
#SBATCH --mem=4000
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1

srun python script.py\n"""
        f.write(buffer)

def import_logfiles(pk):
    remote_sim_dir = get_rmt_sim_dir(pk)
    local_sim_dir = get_lcl_sim_dir(pk)
    #retrieve logs with scp
    import_err = subprocess.run(['scp', remote_sim_dir+'*.err', local_sim_dir+'job_err.err'])
    import_out = subprocess.run(['scp', remote_sim_dir+'*.out', local_sim_dir+'job_out.out'])
