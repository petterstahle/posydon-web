This django app is used to handle the Posydon simulations and data visualizations.
Contains:
-SimProp model object and its views

-Html templates for viewing and handling the simulations

-genGraph mapping function script (function used to map a flow to a .dot graph and render it).
See sims/graph/genGraph.py

-genScript mapping function script, which generates a python script from Simulation Properties arguments to evolve binaries.
See sims/properties/genScript.py

-manage_job.py script which contains:
  -run_sim function, which handles the execution of the binary evolution on the cluster.
  -#TODO: Will contain a results retrieval function.
See sims/evolve/manage_job.py
