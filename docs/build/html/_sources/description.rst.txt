.. on the HPC cluster (in this case the `Baobab<https://baobab.unige.ch/enduser/src/enduser/access.html>_` hosted by the University of Geneva.

Description
===========

The Django app structure
------------------------

See the full `Django documentation <https://docs.djangoproject.com/en/3.0/>`_ for more details.
Essentially, the Django structure is designed in a way so that smaller individual apps that are independent from one another (i.e. serve a specific purpose) can be implemented together and reused to make an integral web-app.
The flow for a Django build follows the concept of "layers" that together implement an app.
Here is a brief list of these layers:

* The model layer
    Django provides an abstraction layer (the “models”) for structuring and manipulating the data of your Web application.

* The view layer
    Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response.

* The template layer
    The template layer provides a designer-friendly syntax for rendering the information to be presented to the user.

* Forms
    Django provides a rich framework to facilitate the creation of forms and the manipulation of form data.

.. figure:: /images/Django-Flow.png
   :alt: Django app structure.
   :scale: 50%

   *A model of the Django app structure (https://www.youtube.com/watch?v=jmX27FrCqqs)*


Posydon-web functionalities
--------------------------------

This web-app consists of 2 apps:

   * pages
       Defines the basic skeleton for the the overal site structure (ex: Home, Navbar, About...)
   * sims
       This is the main app for the project. It's purpose is the handling of simulations, and provides the 3 following functionalities:

       .. toctree::
          :numbered:

          Simulation flow visualization. <flow-graph>
          Binary evolution script generation. <script-gen>
          Simulation handling. <sim-handler>

       **Usage**
         When the ``<posydon-web-addr>/sims/`` url is requested, the user is served the *Simulations* page. Here, a user can view existing simulations (the term *simulation* here refers to the instance of a set of simulation properties linked to the database (`SimProp`_ model), as well as its corresponding job on the cluster and the results if these exist), as well as create a new one. In this case, the ``<posydon-web-addr>/sims/create`` url will be requested and will render a form for the user to fill in, which contains the fields representing the simulation properties.

         .. warning::
            The implementation for submitting a *simulation properties* form has been hard-coded and so far only supports the ``step-zams/cosmic`` and ``step-mesa`` options.

         From the *simulations* page, a user can click on a simulation, and ``<posydon-web-addr>/sims/<id>`` will be requested, with ``id`` representing the primary key of the SimProp instance associated with it, in other words, the unique id corresponding to the simulation in the database.
