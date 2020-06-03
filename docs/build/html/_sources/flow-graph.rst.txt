Flow visualization
==================

This section describes the process to visualize a simulation flow.

When the url ``<posydon-web-addr>/sims/<id>/graph`` is requested, this will make the server render the image using the genGraph module:

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
