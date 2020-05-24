import numpy as np
import pickle
from tqdm import tqdm
from posydon.binary_evol import SimulationProperties
from posydon.binary_evol.cosmic_bse import CosmicBSE
from posydon.binary_evol.step_BH_He_star import step_MESA
from posydon.popsyn import gen_zams_binaries_COMPAS
from posydon.utils import constants

# chose a metallicity value
Z = 0.0001

# model for CosmicBSE step
model = {'xi': 0.5, 'bhflag': 1, 'neta': 0.5, 'windflag': 3,
       'wdflag': 1, 'alpha1': 1.0, 'pts1': 0.001, 'pts3': 0.02,
       'pts2': 0.01, 'epsnov': 0.001, 'hewind': 0.5, 'ck': -1000,
       'bwind': 0.0, 'lambdaf': 0.5, 'mxns': 2.5, 'beta': -1.0,
       'tflag': 1, 'acc2': 1.5, 'remnantflag': 4, 'ceflag': 1,
       'eddfac': 1.0, 'ifflag': 0, 'bconst': -3000,
       'sigma': 265.0, 'gamma': -2.0, 'pisn': -2,
       'bhsigmafrac' : 1.0, 'polar_kick_angle' : 90,
       'qcrit_array' : [0.0,0.0,3.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
       'cekickflag' : 2, 'cehestarflag' : 0, 'cemergeflag' : 0, 'ecsn' : 2.5,
       'ecsn_mlow' : 1.4, 'aic' : 1, 'ussn' : 1, 'sigmadiv': -20.0,
       'qcflag' : 4, 'eddlimflag' : 0, 'rembar_massloss': 0.5,
       'fprimc_array' : [2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0],
       'bhspinflag' : 0, 'bhspinmag' : 0.0, 'rejuv_fac' : 1.0,
       'rejuvflag' : 0, 'htpmb' : 1, 'ST_cr' : 1, 'ST_tide' : 0,
       'bdecayfac' : 1, 'metallicity': Z}

# end step
def end(binary):
    binary.event = 'END'

# simulation properties
prop = SimulationProperties(
    flow={
        ('MS', 'MS', 'ZAMS', None): 'step_zams',
        ('BH', 'HeMS', 'detached', None): 'step_mesa',
        ('BH', 'PostHeMS', 'detached', None): 'step_mesa',
        ('NS', 'HeMS', 'detached', None): 'step_end',
        ('NS', 'PostHeMS', 'detached', None): 'step_end',
        ('HeMS', 'BH', 'detached', None): 'step_mesa',
        ('PostHeMS', 'BH', 'detached', None): 'step_mesa',
        ('PostHeMS', 'NS', 'detached', None): 'step_end',
        ('HeMS', 'NS', 'detached', None): 'step_end'
    },
    step_zams=CosmicBSE(end='CO+He', evolve_dict=model),
    step_mesa=step_MESA(metallicity = Z,
                        mechanism='Fryer+12-delayed',
                        sigma_kick=265.000,
                        mass_central_BH=3.000,
                        neutrino_mass_loss=0.500,
                        PISN='Marchant+19',
                        log_scale=True,
                        verbose=False),
    step_end = end,
    max_time = 13700000000.0
)

# generate binaries
p_min = 0.4
p_max = 10**3.5
pop = gen_zams_binaries_COMPAS( nbin = 1000 , alpha=2.3, m_lim=[5,150], p_lim=[p_min,p_max],  metallicity=Z, properties = prop )

# evolve binaries
BBHs = [] # store here BBHs
for binary in tqdm(pop):
    try:
        binary.evolve()
        if binary.orbital_period > 0. and binary.orbital_period < 10.:
            BBHs.append(binary)
    except Exception as err:
        print(err, binary.restore())

# saving routine
print('We found', len(BBHs), 'BBHs')
with open('./BBHs-population.pkl', 'wb') as file:
    pickle.dump(BBHs, file)