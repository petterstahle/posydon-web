"""This python file is used to take a simulation flow and generate its
associated graph. The main function genGraph is called from the FlowGraphView view function, and uses the parseFlow_dict() method for parsing a flow into the desired fields, and the genGraphHelper() method for generating a graph from the given flow fields.
This script requires a step_default dictionary to be defined. It contains the list of steps and their corresponding bubbles.
It uses the graphviz library and its Digraph method for generating graphs from dot files. """

from graphviz import Digraph
import ast

# dictionary of steps with default children states
# step_default = {
#     'step_1':
#     [('star1_state2','star2_state2'),
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

step_default = {
    'step_zams':{'CO+He':[
    ('BH', 'HeMS'),
    ('HeMS', 'BH'),
    ('BH', 'PostHeMS'),
    ('PostHeMS', 'BH'),
    ('NS', 'HeMS'),
    ('HeMS', 'NS'),
    ('NS', 'PostHeMS'),
    ('PostHeMS', 'NS')]},
    'step_mesa':[
    ('BH', 'BH'),
    ('BH', 'NS'),
    ('NS', 'BH'),
    ('NS', 'NS'),
    ('NS', 'WD'),
    ],
    #step_COLLAPSE, step_ODE, step_RLO, step_NORLO...
    }



def parseFlow_dict(flow):
    """Parses the content of a flow given as a dictionary, used in genGraph() function.
    See below for flow examples for correct format.
    Returns a list of 'levels'.
    Each level represents a bubble and it's following step. It is composed of 3 strings: starA+state, starB+state, step"""
    parsed_fields = []
    for key, value in flow.items():
        level = [key[0], key[1], value]
        parsed_fields.append(level)
    return parsed_fields



def genGraphHelper(parsed_flow, title = 'graph', path = './outputs/', format = 'png', **kwargs):
    """Procedure generating a graphviz.digraph from a parsed flow
    Arguments:
    -parsed_flow:   return value described in parseFlow_dict()
    -title: name of image
    -path: path where image is to be generated. Default is /sims/graph/outputs
    -format: format of image (must be supported by Digraph method), default is .png (better suited for web)
    Returns nothing"""
    # may be necessary to import library from function call depending on implementation
    # from graphviz import Digraph

    #INITIALISATION
    #default graph attributes:
    bubble_shape = 'circle'
    bubble_width = '1'
    step_shape = 'box'
    default_step_style = 'bold'
    step_width = '0.2'
    step_height = '1'
    END = 'step_end'
    default_arrowtype = 'normal'
    #default steps dictionnary
    steps = step_default
    #initialise <step_label:step_node> index pairs dict
    stepIndexes={k:None for k in steps.keys()}

    #GENERATION
    #initialise dot file
    dot = Digraph(format=format)
    for i, level in enumerate(parsed_flow):
        #NODES

        #bubble node
        starStateA = level[0]
        starStateB = level[1]
        #step node
        step_label = level[2]
        bubble_label = starStateA + '\n' + starStateB
        bubble_index = 'B' + str(i)
        #generate bubble
        dot.node(bubble_index, label=bubble_label, shape=bubble_shape, fixedsize='true', width=bubble_width)
        #for step_end
        step_style = default_step_style
        if step_label == END:
            step_style = 'dashed'
            step_index = 'S' + str(i)
        else:
            #add to index dict if not already added
            if not(stepIndexes[step_label]):
                stepIndexes[step_label] = 'S' + str(i)
            #retrieve index from index_dict
            step_index = stepIndexes[step_label]
        #generate step
        dot.node(step_index, label=step_label, shape=step_shape, width=step_width, height=step_height, style=step_style)

        #EDGES

        #bubble-to-step edge
        arrow=default_arrowtype
        style=None
        if step_label == END:
            arrow='none'
            style='dashed'
        dot.edge(bubble_index, step_index, arrowhead=arrow, style=style)
        #step-to-bubble edge
        #this is where we use the step_default dictionary to connect the bubble to its parentstep (nextbubble)
        stepParent = None
        for step, el in steps.items():
            #if el is a dictionary (for ex. step_cosmic has values as dict with keys as cosmic_end params and values as bubbles)
            if isinstance(el, dict):
                if (kwargs['cosmic_end']):
                    if (starStateA, starStateB) in el[kwargs['cosmic_end']]:
                        stepParent = step
            else: #if el is just a list (i.e. step_mesa)
                if (starStateA, starStateB) in el:
                    stepParent = step
        #if bubble has a parent step, we connect it
        if(stepParent):
            parent_index = stepIndexes[stepParent]
            dot.edge(parent_index, bubble_index, arrowhead=default_arrowtype)


    #RENDER GRAPH
    full_path = path + title
    dot.render(full_path)
    return



def genGraph(flow, title = 'graph', path = './outputs/', format = 'png', **kwargs):
    """Function used to generate graph from a flow with correct format.
    Uses parseFlow_dict and genGraphHelper helper functions.
    Uses the step_default dictionary, which maps bubbles to their default corresponding parent step
    Arguments:
    -flow: flow as dictionary with correct format, see examples below.
    -title: name of image
    -path: path where image is to be generated. Default is /sims/graph/outputs
    -format: format of image (must be supported by Digraph method), default is .png (better suited for web)
    Returns nothing
    """
    flow_parsed = None
    # if flow is a string, transform it to a dict
    if isinstance(flow, str):
        flow_dict = ast.literal_eval(flow)
        flow_parsed = parseFlow_dict(flow_dict)
    else:
        flow_parsed = parseFlow_dict(flow)
    genGraphHelper(flow_parsed, title, path, format, **kwargs)
    return



##################################################
################ flow examples ###################
##################################################
#if a flow is in the form of a string, the genGraph function uses the ast.literal_eval method to directly treat it as a dict.

# flow = """{
#     ('star1_state1', 'star2_state1', 'detached', None): 'step_1',
#     ('star1_state2', 'star2_state2', 'detached', None): 'step_2',
#     ('star1_state3', 'star2_state3', 'detached', None): 'step_2',
#     ('star1_state4', 'star2_state4', 'detached', None): 'step_end',
#     ('star1_state5', 'star2_state5', 'detached', None): 'step_3',
#     ('star1_state6', 'star2_state6', 'detached', None): 'step_3',
#     ('star1_state7', 'star2_state7', 'detached', None): 'step_end',
#     ('star1_state8', 'star2_state8', 'detached', None): 'step_end',
#     ('star1_state9', 'star2_state9', 'detached', None): 'step_end',
#     }"""

# flow = {
#         ('MS', 'MS', 'ZAMS', None): 'step_COSMIC',
#         ('BH', 'HeMS', 'detached', None): 'step_mesa',
#         ('BH', 'PostHeMS', 'detached', None): 'step_mesa',
#         ('NS', 'HeMS', 'detached', None): 'step_end',
#         ('NS', 'PostHeMS', 'detached', None): 'step_end',
#         ('PostHeMS', 'NS', 'detached', None): 'step_end',
#         ('BH', 'NS', 'detached', None): 'step_end',
#         ('BH', 'BH', 'detached', None): 'step_end',
#         }

# run script for debug
# genGraph(flow, title='test', format='pdf')






# buggy function, use parseFlow_dict if possible
# will parse the content of flow given as a string
# returns list of "flow levels"
# each 'level' is a list of 3 elements (string): starA_state, starB_state, step_name
# def parseFlow_string(flow):
#
#     #split flow into levels
#     levels = flow.strip()
#     levels = levels.strip('{}')
#     levels = levels.strip()
#     levels = levels.split('\n')
#
#     flow_size = len(levels)
#     parsed_fields = [[] for _ in range(flow_size)]
#
#     #level parsing
#     for i, l in enumerate(levels):
#         #partition level into bubble and step
#         bubble, _, step = l.partition(':')
#
#         #bubble parsing
#         bubble = bubble.strip()
#         bubble = bubble.strip('()')
#         #split bubble into params
#         params = bubble.split(',')
#         #delete last 2 fields of params (not useful for graph)
#         params.pop(-1)
#         params.pop(-1)
#         #param parsing
#         for p in params:
#             p = p.strip()
#             p = p.strip("''")
#             #add to field
#             parsed_fields[i].append(p)
#
#         #step parsing
#         step = step.strip(',')
#         step = step.strip()
#         step = step.strip("''")
#         #add to field
#         parsed_fields[i].append(step)
#
#     return parsed_fields
