"""This script contains the procedure genScript(obj, filepath),
which generates the script for running a binaries evolution simulation.
It takes as inputs:
    obj: The SimProp database model which contains the info for SimulationProperties
    filepath: path where the .py file is written."""

def genScript(obj, filepath):
    #generate string blocks
    imports = """import numpy as np
from tqdm import tqdm
from posydon.binary_evol import SimulationProperties
from posydon.binary_evol.cosmic_bse import CosmicBSE
from posydon.binary_evol.step_BH_He_star import step_MESA
from posydon.popsyn import gen_zams_binaries_COMPAS
from posydon.utils import constants"""
    metallicity_block = """# chose a metallicity value
Z = """ + str(obj.metallicity)
    model_block = """# model for CosmicBSE step
model = """ + obj.cosmic_evolve_dict
    end_block = """# end step
def end(binary):
    binary.event = 'END'"""

    #simulation properties block
    simprop_head = """# simulation properties
prop = SimulationProperties("""
    flow = "    flow=" + obj.flow + ","
    step_zams = "    step_zams=CosmicBSE(end='" + obj.cosmic_end + "', evolve_dict=model),"
    step_mesa = """    step_mesa=step_MESA(metallicity = Z,
                        mechanism='""" + obj.mesa_mechanism + """',
                        sigma_kick=""" + str(obj.mesa_sigma_kick) + """,
                        mass_central_BH=""" + str(obj.mesa_mass_central_BH) + """,
                        neutrino_mass_loss=""" + str(obj.mesa_neutrino_mass_loss) + """,
                        PISN=""" + obj.mesa_PISN + """,
                        log_scale=""" + str(obj.mesa_log_scale) + """,
                        verbose=""" + str(obj.mesa_verbose) + "),"
    step_end = "    step_end = " + obj.step_end + ","
    max_time = "    max_time = " + str(obj.max_time)
    #make simulation properties block
    simprop_block = simprop_head + '\n' + flow + '\n' + step_zams + '\n' + step_mesa + '\n' + step_end + '\n' + max_time + "\n)"

    binaries_block = """# generate binaries
p_min = 10**0.15
p_max = 10**3.5
pop = gen_zams_binaries_COMPAS( nbin = 1000 , alpha=2.3, m_lim=[5,150], p_lim=[p_min,p_max],  metallicity=Z, properties = prop )

# evolve binaries
for binary in tqdm(pop):
    try:
        binary.evolve()
    except Exception as err:
        print(err, binary.restore())

# TODO: saving routine"""

    #make script string
    buffer = imports + '\n\n' + metallicity_block + '\n\n' + model_block + '\n\n' + end_block + '\n\n' + simprop_block + '\n\n' + binaries_block

    #generate script
    with open(filepath,'w') as f:
        f.write(buffer)
        f.close()
