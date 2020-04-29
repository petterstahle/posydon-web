import ast
prop = SimulationProperties(
    flow={
        ('MS', 'MS', 'ZAMS', None): 'step_cosmic',
        ('BH', 'HeMS', 'detached', None): 'step_mesa',
        ('BH', 'PostHeMS', 'detached', None): 'step_mesa',
        ('NS', 'HeMS', 'detached', None): 'step_end',
        ('NS', 'PostHeMS', 'detached', None): 'step_end',
        ('HeMS', 'BH', 'detached', None): 'step_mesa',
        ('PostHeMS', 'BH', 'detached', None): 'step_mesa',
        ('PostHeMS', 'NS', 'detached', None): 'step_end',
        ('HeMS', 'NS', 'detached', None): 'step_end'
    },
    step_cosmic=CosmicBSE('CO+He', model),
    step_mesa=step_MESA(
                      mechanism='Fryer+12-delayed',
                      sigma_kick=265.,
                      phi=None,
                      cos_theta=None,
                      mean_anomaly=None,
                      mass_central_BH=2.51,
                      neutrino_mass_loss_fraction=0.1,
                      neutrino_AM_loss=False,
                      PISN='Marchant+2019',
                      log_scale=True,
                      verbose=False),
    step_end = end,
    max_time = 13.7e9
)

model = {'xi': 0.5, 'bhflag': 1, 'neta': 0.5, 'windflag': 3,
       'wdflag': 1, 'alpha1': 1.0, 'pts1': 0.001, 'pts3': 0.02,
       'pts2': 0.01, 'epsnov': 0.001, 'hewind': 0.5, 'ck': -1000,
       'bwind': 0.0, 'lambdaf': 0.5, 'mxns': 2.5, 'beta': -1.0,
       'tflag': 1, 'acc2': 1.5, 'nsflag': 4, 'ceflag': 1,
       'eddfac': 1.0, 'ifflag': 0, 'bconst': -3000,
       'sigma': 265.0, 'gamma': -2.0, 'pisn': -2,
       'bhsigmafrac' : 1.0, 'polar_kick_angle' : 90,
       'qcrit_array' : [0.0,0.0,3.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
       'cekickflag' : 2, 'cehestarflag' : 1, 'cemergeflag' : 0, 'ecsn' : 2.5,
       'ecsn_mlow' : 1.4, 'aic' : 1, 'ussn' : 1, 'sigmadiv' :-20.0,
       'qcflag' : 4, 'eddlimflag' : 0,
       'fprimc_array' : [2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0],
       'bhspinflag' : 0, 'bhspinmag' : 0.0, 'rejuv_fac' : 1.0,
       'rejuvflag' : 0, 'htpmb' : 1, 'ST_cr' : 1, 'ST_tide' : 0,
       'bdecayfac' : 1, 'metallicity': 0.00132}

properties = {
'flow': {
    ('MS', 'MS', 'ZAMS', None): 'step_cosmic',
    ('BH', 'HeMS', 'detached', None): 'step_mesa',
    ('BH', 'PostHeMS', 'detached', None): 'step_mesa',
    ('NS', 'HeMS', 'detached', None): 'step_end',
    ('NS', 'PostHeMS', 'detached', None): 'step_end',
    ('HeMS', 'BH', 'detached', None): 'step_mesa',
    ('PostHeMS', 'BH', 'detached', None): 'step_mesa',
    ('PostHeMS', 'NS', 'detached', None): 'step_end',
    ('HeMS', 'NS', 'detached', None): 'step_end'
    },

'step_cosmic': {
'end': 'CO+He',
'evolve_dict': model
    },

'step_mesa': {
'mechanism': 'Fryer+12-delayed',
'sigma_kick': 265.,
'phi': None,
'cos_theta': None,
'mean_anomaly': None,
'mass_central_BH': 2.51,
'neutrino_mass_loss_fraction': 0.1,
'neutrino_AM_loss': False,
'PISN': 'Marchant+2019',
'log_scale': True,
'verbose': False
},

'step_end': 'end',

'max_time': 13.7e9
}

evolve_dict = "{'xi': 0.5, 'bhflag': 1, 'neta': 0.5, 'windflag': 3,\r\n       'wdflag': 1, 'alpha1': 1.0, 'pts1': 0.001, 'pts3': 0.02,\r\n       'pts2': 0.01, 'epsnov': 0.001, 'hewind': 0.5, 'ck': -1000,\r\n       'bwind': 0.0, 'lambdaf': 0.5, 'mxns': 2.5, 'beta': -1.0,\r\n       'tflag': 1, 'acc2': 1.5, 'nsflag': 4, 'ceflag': 1,\r\n       'eddfac': 1.0, 'ifflag': 0, 'bconst': -3000,\r\n       'sigma': 265.0, 'gamma': -2.0, 'pisn': -2,\r\n       'bhsigmafrac' : 1.0, 'polar_kick_angle' : 90,\r\n       'qcrit_array' : [0.0,0.0,3.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\r\n       'cekickflag' : 2, 'cehestarflag' : 1, 'cemergeflag' : 0, 'ecsn' : 2.5,\r\n       'ecsn_mlow' : 1.4, 'aic' : 1, 'ussn' : 1, 'sigmadiv' :-20.0,\r\n       'qcflag' : 4, 'eddlimflag' : 0,\r\n       'fprimc_array' : [2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0],\r\n       'bhspinflag' : 0, 'bhspinmag' : 0.0, 'rejuv_fac' : 1.0,\r\n       'rejuvflag' : 0, 'htpmb' : 1, 'ST_cr' : 1, 'ST_tide' : 0,\r\n       'bdecayfac' : 1, 'metallicity': 0.00132}"

print(str(evolve_dict))
print(ast.literal_eval(str(evolve_dict)))












# step_default =
# {
#     'step_COSMIC':[
#     ('BH', 'MS'),
#     ('BH', 'PostMS'),
#     ('BH', 'HeMS'),
#     ('BH', 'PostHeMS'),
#     ('BH', 'WD'),
#     ('NS', 'MS'),
#     ('NS', 'PostMS'),
#     ('NS', 'HeMS'),
#     ('NS', 'PostHeMS'),
#     ('NS', 'WD')
#     ],
#     'step_MESA':[
#     ('BH', 'BH'),
#     ('BH', 'NS'),
#     ('NS', 'BH'),
#     ('NS', 'NS'),
#     ('NS', 'WD'),
#     ('PostHeMS', 'MS')
#     ],
#     #step_COLLAPSE, step_ODE, step_RLO, step_NORLO...
#
# }



step_default = {
    'step_1':[
    ('star1_state2','star2_state2'),
    ('star1_state3','star2_state3'),
    ('star1_state4','star2_state4'),
    ('star1_state5','star2_state5'),
    ('star1_state6','star2_state6')],
    'step_2':
    [('star1_state7','star2_state7'),
    ('star1_state8','star2_state8')],
    'step_3':
    [('star1_state9','star2_state9')]
    }
