Flow visualization
==================

This section describes the process to visualize a simulation flow.

When the url ``<posydon-web-addr>/sims/<id>/graph`` is requested, this will make the server render the image using the genGraph module located in ``src/sims/graph/genGraph.py``.

*Option*: You can also add the following options in the url to download the image as a pdf:
   ``<posydon-web-addr>/sims/2/graph/?format=pdf&download=true``

**Storage**:
   The default path for generated graphs is in the following directory: ``src/sims/graph/outputs/``, and each graph is identified by the title field of its corresponding ``SimProp`` *simulation properties* object.

.. automodule:: sims.graph.genGraph
   :members: genGraph


Example of a flow with correct format
-------------------------------------
::

   flow = {
           ('MS', 'MS', 'ZAMS', None): 'step_COSMIC',
           ('BH', 'HeMS', 'detached', None): 'step_mesa',
           ('BH', 'PostHeMS', 'detached', None): 'step_mesa',
           ('NS', 'HeMS', 'detached', None): 'step_end',
           ('NS', 'PostHeMS', 'detached', None): 'step_end',
           ('PostHeMS', 'NS', 'detached', None): 'step_end',
           ('BH', 'NS', 'detached', None): 'step_end',
           ('BH', 'BH', 'detached', None): 'step_end',
           }

Example of step_default dictionary
----------------------------------

::

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
     ]
     }
