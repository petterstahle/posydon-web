Evolution script generation
===========================

This section describes the process to automatically generate the python script for running a simulation from a given set of simulation properties.

When the url ``<posydon-web-addr>/sims/<id>/download-script`` is requested, the server will generate and serve the python script ``script.py`` as an attachment, using the genScript module located in ``src/sims/properties/genScript.py``.

**Storage**:
   The default path for generated scripts is in the following directory: ``src/sims/properties/outputs/<id>/``, where ``id`` corresponds to the primary key of the ``SimProp`` *simulation properties* object. 

.. automodule:: sims.properties.genScript
   :members:
