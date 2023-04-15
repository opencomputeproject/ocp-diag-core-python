# Developer notes

### Setup a devenv

There are multiple ways of setting up a python dev environment, but likely the easiest is to use a [venv](https://docs.python.org/3/library/venv.html).

In order to do so:
1. make a new venv and activate it
    ```bash
    # in the ocp-diag-python root dir
    $ python -m venv env
    $ source ./env/bin/activate
    ```
2. install dependencies using pip (pip installation depends on operating system. see [official instructions](https://pip.pypa.io/en/stable/installation/))
    ```bash
    $ pip install -r requirements.txt
    ```
3. check that pytest works (needed later)
    ```bash
    $ pytest -v
    ```
4. *[optiona]* deactivate/exit the env
    ```bash
    $ deactivate
    ```