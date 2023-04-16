# Developer notes

All of the below topics start from the baseline of a valid git clone on a Linux type operating system.
To get started, the normal git/github clone procedure can be used. For quick reference, the command below does this:
```bash
$ git clone git@github.com:opencomputeproject/ocp-diag-python.git
$ cd ocp-diag-python
```

If you don't already have SSH credentials set up with Github, the HTTP clone should work as well (though it may lead to asking for credentials on every git push later on).
```bash
$ git clone https://github.com/opencomputeproject/ocp-diag-python.git
$ cd ocp-diag-python
```

## Setup a devenv

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

## Committing code

To add new code (or address an issue), we are using a modified [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) branching strategy.

The following steps show the process where the development work is being done on a local clone of the repository. This is relevant for the core team and approved members.

If you are not an approved member at this time, making a PR implies that you have made a fork on your own Github account. When working on a fork, the steps to contribute are similar, the only difference being in how the PR is created. In this case, you'll push the new branch to your fork and create a PR targetting the [upstream](https://github.com/opencomputeproject/ocp-diag-python) repository `dev` branch.

Steps:
1. make sure you are on the latest commit
    ```bash
    $ git checkout dev
    $ git pull origin dev # this may be upstream, not origin, when working with a fork
    ```
2. make a new feature branch from `dev` branch. It should have a short name based on the feature you're implementing, eg. `fea/add_linter`. In case of bugfixing, the prefix changes, like `bugfix/what_is_fixed`.
    ```bash
    $ git checkout -b fea/$name
    ```
3. add your changes now, including any tests and run pytest and linter (here [black](https://pypi.org/project/black/)). These are also checked upstream, and will block your PR if they fail.
    ```bash
    $ pytest -v # check that everything is green
    $ black . # will reformat all the source files
    $ mypy ocptv tests examples --check-untyped-defs # check the type annotations
    ```
4. if the tests above pass and everything is ready, push and make a PR. This can be done either from the Github website or using [gh cli](https://cli.github.com/manual/gh_pr_create).
5. the PR will now be reviewed. If everything is ok, a maintainer will merge it to the `dev` branch.

**Note on stacked PRs:** if you'd like to have multiple reviews for a bigger feature implementation, there is the option of making a stack of PRs. The recommendation is that a feature branch is started from `dev`, then multiple branches (each with their own PR) are started from the feature branch. All of these PRs will be **rebased** on the feature branch, followed by a final PR for the feature branch (which likely does not need to be reviewed, based on the stacked reviews). This final feature branch will then be merged normally into `dev`.

There are tools that automate this process (although in a slightly different fashion, but still accepted), like [graphite](https://graphite.dev/stacking).

### Github actions

It may be useful to run the github actions locally, both when working on them directly but also on the python codebase (useful to check that other supported python versions haven't been broken; you may need to modify conditions in [tests.yaml](./.github/workflows/tests.yaml)).

The [act-cli](https://github.com/nektos/act) project can be used for this. It will download a docker container (with an LTS ubuntu) and run all of the relevant github actions in the repo. This assumes that you have [docker installed](https://docs.docker.com/get-docker/).

Run it just by simply using the `act` command in the repository root dir.
