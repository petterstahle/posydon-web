Simulation handling
===================

This script describes the usage and process for executing simulations and handling results or logs of a given simulation.
Simulations are run remotely on a HPC cluster (in this case the `Baobab <https://baobab.unige.ch/enduser/src/enduser/access.html>`_ cluster hosted by the University of Geneva).


*usage* :
   From a given *simulation properties details* page, contained in ``<posydon-web-addr>/sims/<id>/``, a user can request to run a simulation. To do this, the user must first submit a valid email address. This email is processed in a SLURM script and is used to notify the user when and if the simulation job has begun successfully on the cluster, as well as finished.

   When the simulation request has been sent, the server utilizes the manage_job module located in ``src/sims/evolve/manage_job.py``. The user is then redirected to the *results* page at ``<posydon-web-addr>/sims/<id>/results/``, where simulation results and log files in case of errors can be downloaded.

   .. warning::
      In the current version of this web-app, requesting these files may cause errors if a they do not exist (i.e. have not yet been created, because a job has not been completed or was not submitted succesfully).


**Storage**:
   The default path for generated results/log files is in the following directory: ``src/sims/evolve/outputs/<id>``, where ``id`` corresponds to the primary key of the ``SimProp`` *simulation properties* object.


.. automodule:: sims.evolve.manage_job
  :members: REMOTE_USR, HOST, REMOTE_DIR, run_sim, pull_results, gen_log
