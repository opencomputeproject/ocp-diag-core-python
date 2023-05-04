# ocp-diag-python

The **OCP Test & Validation Initiative** is a collaboration between datacenter hyperscalers having the goal of standardizing aspects of the hardware validation/diagnosis space, along with providing necessary tooling to enable both diagnostic developers and executors to leverage these interfaces.

Specifically, the [ocp-diag-python](https://github.com/opencomputeproject/ocp-diag-python) project makes it easy for developers to use the **OCP Test & Validation specification** artifacts by presenting a pure-python api that can be used to output spec compliant JSON messages.

To start, please see below for [installation instructions](https://github.com/opencomputeproject/ocp-diag-python#installation) and [usage](https://github.com/opencomputeproject/ocp-diag-python#usage).

This project is part of [ocp-diag-core](https://github.com/opencomputeproject/ocp-diag-core) and exists under the same [MIT License Agreement](https://github.com/opencomputeproject/ocp-diag-python/LICENSE).

### Installation

Stable releases of the **ocp-diag-python** codebase are published to **PyPI** under the package name [ocptv](https://pypi.org/project/ocptv/), and can be easily installed with python package managers.

**Minimum python version is currently py37.**

For general usage, the following steps should be sufficient to get the latest stable version:

- **\[option 1]**: using the [Package Installer for Python](https://pypi.org/project/pip/)

    *\[optional]* if your project needs or already has a venv, activate it first, otherwise the installation will be system-wide.
    ```bash
    $ python -m venv env
    $ source env/bin/activate
    ```

    Then just install:
    ```bash
    $ pip install ocptv
    ```
- **\[option 2]** using [Python Poetry](https://python-poetry.org/)

    *\[optional]* for a completely new project, run either `poetry new` or `poetry init` (see [poetry docs](https://python-poetry.org/docs/basic-usage/#project-setup)). Then:

    ```bash
    $ poetry add ocptv
    ```

To use the bleeding edge instead of the stable version, the git repository should be cloned.
This assumes that the clone is manually kept up to date by git pulling whenever there are new commits upstream. All of the installation methods below will automatically use the latest library code.

First clone the upstream latest code:
```bash
$ git clone https://github.com/opencomputeproject/ocp-diag-python.git
$ cd ocp-diag-python
$ git checkout dev # dev branch has the latest code
```

- **\[option 1]**: using `pip` editable install

    Similar to the stable version steps above, but with `-e`. Either system-wide or inside a venv.
    ```bash
    $ pip install -e path/to/git_cloned/ocp-diag-python
    ```
- **\[option 2]**: using `poetry`

    The `--editable` flag is still in **1.2beta** as of this writing, so add the dependency to your `pyproject.toml` with `develop = true`:
    ```toml
    [tool.poetry.dependencies]
    ocptv = { path = "path/to/git_cloned/ocp-diag-python", develop = true }
    ```

    Then install everything:
    ```bash
    $ poetry install
    ```

The instructions above assume a Linux-type system. However, the steps should be identical on Windows and MacOS platforms.

See [docs.python.org](https://docs.python.org/3/library/venv.html) for more details on how to use python venvs.

### Usage

The specification does not impose any particular level of usage. To be compliant, a diagnostic package just needs output the correct artifact messages in the correct format. However, any particular such diagnostic is free to choose what aspects it needs to use/output; eg. a simple validation test may not output any measurements, opting to just have a final Diagnosis outcome.

**Full API reference is available [here](https://github.com/opencomputeproject/ocp-diag-python/blob/dev/docs/index.md).**

A very simple starter example, which just outputs a diagnosis:
```py
import ocptv.output as tv

def main():
    run = tv.TestRun(name="simple_diagnosis", version="1.0")
    dut = tv.Dut(id="server0", name="server0.domain.net")
    with run.scope(dut=dut):
        step = run.add_step("check_fanspeed")
        with step.scope():
            if get_fan_speed() > 1600: # assuming external get_fan_speed() impl
                step.add_diagnosis(DiagnosisType.PASS, verdict="fan_ok")
            else:
                step.add_diagnosis(DiagnosisType.FAIL, verdict="fan_low")
```

Expected output (slightly reformatted for readability):
```json
{"schemaVersion": {"major": 2, "minor": 0}, "sequenceNumber": 0, "timestamp": "2023-04-19T20:54:05.652514+01:00"}

{"testRunArtifact": {
    "testRunStart": {
        "name": "simple_diagnosis",
        "version": "1.0", "commandLine": "", "parameters": {},
        "dutInfo": {
            "dutInfoId": "server0", "name": "server0.domain.net",
            "platformInfos": [], "softwareInfos": [], "hardwareInfos": []
        }
    }
}, "sequenceNumber": 1, "timestamp": "2023-04-19T20:54:05.652646+01:00"}

{"testStepArtifact": {
    "testStepId": "0",
    "testStepStart": { "name": "check_fanspeed" }
}, "sequenceNumber": 2, "timestamp": "2023-04-19T20:54:05.652771+01:00"}

{"testStepArtifact": {
    "testStepId": "0",
    "diagnosis": {
        "verdict": "fan_ok", "type": "PASS",
        "sourceLocation": {"file": "/home/user/ocp-diag-python/test.py", "line": 16}
    }
}, "sequenceNumber": 3, "timestamp": "2023-04-19T20:54:05.653037+01:00"}

{"testStepArtifact": {
    "testStepId": "0",
    "testStepEnd": {"status": "COMPLETE"}
}, "sequenceNumber": 4, "timestamp": "2023-04-19T20:54:05.653167+01:00"}

{"testRunArtifact": {
    "testRunEnd": {"status": "COMPLETE", "result": "PASS"}
}, "sequenceNumber": 5, "timestamp": "2023-04-19T20:54:05.653219+01:00"}
```

For more examples of usage, there are a number available in the [examples folder](https://github.com/opencomputeproject/ocp-diag-python/tree/dev/examples), along with expected outputs.

### Configuration

There are a couple of knobs that can be used to configure the behavior of the `ocptv` library:
- **enable_runtime_checks**: when this is true, the lib code will try to validate the actual types of the data being fed to it against what the specification requires. This may be disable if performance is critical or if it shows any false positives. Default is `True`.
- **timezone**: a `datetime.tzinfo` implementation overriding the default local timezone. Default is `None`, which means local timezone.
- **writer**: a `ocptv.output.Writer` implementation that is used for the lowlevel writing of serialized JSON strings. Default is `ocptv.output.StdoutWriter` which just writes everything to standard output.

To setup any of these aspects:
```py
import ocptv.output as tv
from ocptv.output import StdoutWriter

# signature:
# config(
#     writer: ty.Optional[Writer] = None,
#     enable_runtime_checks: ty.Optional[bool] = None,
#     timezone: ty.Union[tzinfo, None] = _NOT_SET,
# )

# disable the runtime type checks
tv.config(enable_runtime_checks=False)

# change writer and timezone
tv.config(timezone=pytz.UTC, writer=StdoutWriter())
```

When using the configuration endpoint, at the moment of starting a test run, the configuration is considered committed. The settings can still be technically modified, but it might result in unexpected behavior, eg. changing the `writer` will result in a partial output, which is not compliant.

There's also some more advanced configuration in `config.py` and `advanced.py` in the [examples folder](https://github.com/opencomputeproject/ocp-diag-python/tree/dev/examples).

### Examples

The examples in [examples folder](https://github.com/opencomputeproject/ocp-diag-python/tree/dev/examples) are setup to run as a module.

```bash
# run all demos available
$ python -m examples

# list demo names
$ python -m examples list

# run a specific example
$ python -m examples demo_diagnosis
```

The [sample output file](https://github.com/opencomputeproject/ocp-diag-python/tree/dev/examples/sample_output.txt) shows a run of all demos. This is meant as documentation.

### Developer notes

If you would like to contribute, please head over to [developer notes](https://github.com/opencomputeproject/ocp-diag-python/tree/dev/DEVELOPER_NOTES.md) for instructions regarding setting up a development environment and more on submitting code.

### Contact

Feel free to start a new [discussion](https://github.com/opencomputeproject/ocp-diag-python/discussions), or otherwise post an [issue/request](https://github.com/opencomputeproject/ocp-diag-python/issues).

An email contact is also available at: ocp-test-validation@OCP-All.groups.io

<!--
due to https://github.com/pypa/readme_renderer/issues/163 we must use absolute links everywhere
-->