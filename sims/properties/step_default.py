step_default = {
    'step_COSMIC':{'CO+He':[
    ('BH', 'HeMS'),
    ('BH', 'PostHeMS'),
    ('NS', 'HeMS'),
    ('NS', 'PostHeMS')]},
    'step_MESA':[
    ('BH', 'BH'),
    ('BH', 'NS'),
    ('NS', 'BH'),
    ('NS', 'NS'),
    ('NS', 'WD'),
    ],
    #step_COLLAPSE, step_ODE, step_RLO, step_NORLO...
    }

for k,v in step_default.items():
    if isinstance(v, dict):
        for k2,v2 in v.items():
            if ('BH', 'BH') in v2:
                print(k)
    else:
        if ('BH', 'BH') in v:
            print(k)

#
# step_default = {
#     'step_1':[
#     ('star1_state2','star2_state2'),
#     ('star1_state3','star2_state3'),
#     ('star1_state4','star2_state4'),
#     ('star1_state5','star2_state5'),
#     ('star1_state6','star2_state6')],
#     'step_2':
#     [('star1_state7','star2_state7'),
#     ('star1_state8','star2_state8')],
#     'step_3':
#     [('star1_state9','star2_state9')]
#     }
# print(step_default['step_COSMIC'].values())
# print(('BH', 'HeMS') in step_default['step_COSMIC'].values())
