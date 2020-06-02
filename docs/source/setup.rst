Get started
============

Follow these step-by-step instructions to setup the Django server (This is for development. See https://docs.djangoproject.com/en/3.0/topics/install/ for more info).

1. Set up a virtual environment (Linux & macOS).
   For this step, it is recommended to use pip with the python module *virtualenv*. This step (and step 3 for activating the virtual environment) follows the documentation on https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ (see this page for more info or for a Windows setup). Anaconda can also be used if needed (see https://www.anaconda.com/blog/using-pip-in-a-conda-environment in this case and skip this section) .
   * install `pip`:
   `python3 -m pip install --user --upgrade pip`
   * install `virtualenv` (already included as of Python 3.3 as *venv*):
   `python3 -m pip install --user virtualenv`
   * create virtual environment:
   `python3 -m venv env`
   venv will create a virtual Python installation in the `env` folder.

2. Clone Github repo into your `env` directory.

3. Activate virtual environment.
   Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH
   * cd into your environment:
   `cd env/`
   * run
   `source bin/activate`
   Your shell prompt should now show `(env) user@localhost:/<path-to-env>/env/`
   You can leave the virtual environment any time by simply running:
   `deactivate`

4. Install project dependencies.
   Here you will actually install the required packages for the project, listed in the `requirements.txt` file in the `docs` folder.
   * cd into the project root (local git repo, contains a `docs/` and a `src/` directory)
   * install dependencies with:
   `pip install -r docs/requirements.txt`
