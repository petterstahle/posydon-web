Get started
============

Follow these step-by-step instructions to setup the Django server (This is for development. See https://docs.djangoproject.com/en/3.0/topics/install/ for more info).


Django environment setup
------------------------

|

1. **Set up a virtual environment** (Linux & macOS).

   For this step, it is recommended to use pip with the python module *virtualenv*. This step (and step 3 for activating the virtual environment) follows the documentation on https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ (see this page for more info or for a Windows setup).
   Anaconda can also be used if needed (see https://www.anaconda.com/blog/using-pip-in-a-conda-environment in this case and skip this section).

   * install ``pip`` ::

       python3 -m pip install --user --upgrade pip

   * install ``virtualenv`` (already included as of Python 3.3 as ``venv``)::

       python3 -m pip install --user virtualenv

   * create virtual environment::

       python3 -m venv env

     venv will create a virtual Python installation in the ``env`` folder.

|

2. **Import project.**

   Clone Github repo into your ``env`` directory.

|

3. **Activate virtual environment.**

   Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH

   * cd into your environment: ``cd env/``
   * run: ``source bin/activate``
     Your shell prompt should now display ``(env) user@localhost:/<path-to-env>/env/``

     You can leave the virtual environment any time by simply running:
     ``deactivate``

|

4. **Install project dependencies.**

   Here you will install the required packages for the project, listed in the ``requirements.txt`` file in the ``docs/`` folder.

   * cd into the local git repo root (contains the `docs/` documentation and the `src/` source code directories. )
   * install dependencies with::

       pip install -r docs/requirements.txt

|

Django server setup
-------------------


|

5. *Optional* **Setup your database.**
   This step should not be necessary because the sqlite3 database used during development is already locally contained in the project root ``src/dp.sqlite3``.
   However, should you wish to use another database, you can do the following:

   * Enter database settings in the project settings file contained in ``src/posydon/settings.py`` at the following location::

       # Database
       # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
           }
       }

   * Initialize your database::

       python ./manage.py syncdb
       python ./manage.py migrate

|

6. **Setup the Django admin.**

   The admin interface for Django web apps is very powerful. From there you can directly manage database models among other things (see https://docs.djangoproject.com/en/3.0/ref/contrib/admin/).
   To use this functionality (which may be required), you will need to create a new superuser for the admin::

     python ./manage.py createsuperuser

|

7. **Run server.**

   Finally, run the development server::

     python ./manage.py runserver

   The shell should run the server and display something resembling this message::

     Watching for file changes with StatReloader
     Performing system checks...

     System check identified no issues (0 silenced).
     June 02, 2020 - 17:35:31
     Django version 3.0.4, using settings 'posydon.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.

   Open the http link in your browser and you should be served the web-app home page!

|

Your server should now be setup, see the *intro* for a brief description of the web-app and its functionalities.
