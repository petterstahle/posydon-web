"""When run this script executes system calls (uses the subprocess module) to do these actions:
    1- copy the generated population synthesis script contained in sims/properties/outputs/script.py to the Unige Baobab cluster at user@baobab2.hpc.unige.ch:/~/POSYDON/PopSyn
    2- write slurm script (with email adress contained as parameter) and send to cluster
    3- establish ssh connection to the cluster
    4- activate conda environment
    5- run slurm script (with sbatch)
"""
import subprocess, os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "posydon.settings")

def run_sim(email, title):
    #PATH INITIALISATION
    REMOTE_USR = 'stahle8' #will later be web_app user
    HOST = '@baobab2.hpc.unige.ch:~/'
    dest_path = REMOTE_USR+HOST+'POSYDON/PopSyn/' #set path args
    log_path = os.path.join(settings.BASE_DIR, 'sims/evolve/outputs/logs/'+title+'_log.txt')

    #EXECUTE SUBPROCESSES

    #1 copy generate python script to cluster
    script_path = './sims/properties/outputs/'+title+'.py'
    copy_py_proc = subprocess.run(['scp', script_path, dest_path])
        #todo add exceptions and error handling to show errors on browser page

    #2 edit slurm script to incorportate email and title
    slurm_path = os.path.join(settings.BASE_DIR, 'sims/evolve/outputs/run-script.slurm')
    print(slurm_path)
    write_slurm(slurm_path, email, title)
    #add option to manually write slurm script in browser?

    # copy run-script.slurm to cluster
    copy_slurm_proc = subprocess.run(['scp', slurm_path, dest_path])
        #todo add exceptions and error handling to show errors on browser page


    #3 connect to ssh server
    #will connect to ssh, then write subsequent commands to the sdtin stream
    with open(log_path, 'a') as log: #open log file context
        ssh_proc = subprocess.Popen(["ssh", REMOTE_USR+HOST],
                            shell =True,
                            stdin =subprocess.PIPE,
                            stdout=log,
                            stderr=log,
                            universal_newlines=True,
                            bufsize=0)

        #test: write a new doc
        ssh_proc.stdin.write("touch ~/POSYDON/PopSyn/hello_world.txt\n")

        # # Send ssh commands to stdin
        # ssh.stdin.write("conda activate env\n") #activate env
        # ssh.stdin.write("sbatch ~/POSYDON/PopSyn/run-script.slurm\n") #run job
        ssh_proc.stdin.close()


def write_slurm(path, email, title):
    """Helper function: generate slurm script at path with email as param for notifications"""
    with open(path, 'w') as f:
        buffer = """#!/bin/bash
#SBATCH --mail-user="""+email+"""
#SBATCH --mail-type=ALL
#SBATCH --account=fragkos
#SBATCH --job-name=pop-syn
#SBATCH --output=log_%a.out
#SBATCH --error=log_%a.err
#SBATCH --partition=debug-EL7
#SBATCH --ntasks=1
#SBATCH --mem=4000
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1

srun python """+title+".py\n"
        f.write(buffer)




# def get_results()


# #TEST
# write_slurm('./outputs/run-script.slurm', 'what@test.com', 'test')
# slurm_path = os.path.join(settings.BASE_DIR, 'sims/evolve/outputs/run-script.slurm')
# print(slurm_path)
