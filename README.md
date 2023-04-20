# ocp-diag-python

The **OCP Test & Validation Initiative** is a collaboration between datacenter hyperscalers having the goal of standardizing aspects of the hardware validation/diagnosis space, along with providing necessary tooling to enable both diagnostic developers and executors to leverage these interfaces.

Specifically, the [ocp-diag-python](https://github.com/opencomputeproject/ocp-diag-python) project makes it easy for developers to use the **OCP Test & Validation specification** artifacts by presenting a pure-python api that can be used to output spec compliant JSON messages.

To start, please see below for [installation instructions](https://github.com/opencomputeproject/ocp-diag-python#installation) and [usage](https://github.com/opencomputeproject/ocp-diag-python#usage).

This project is part of [ocp-diag-core](https://github.com/opencomputeproject/ocp-diag-core) and exists under the same [MIT License Agreement](https://github.com/opencomputeproject/ocp-diag-python/LICENSE).

### Installation

Stable releases of the **ocp-diag-python** codebase are published to **PyPI** under the package name [ocptv](https://pypi.org/project/ocptv/), and can be easily installed with `pip`.

**Minimum python version is currently py37.**

For general usage, the following steps should be sufficient to get the latest stable version:

```bash
# [option 1] install system-wide, from any shell
$ pip install ocptv

# [option 2] inside your python diagnostic rootdir, create a venv and activate it
$ python -m venv env
$ source env/bin/activate
$ pip install ocptv
```

To use the bleeding edge instead of the stable version, the git repository should be cloned.
This assumes that the clone is manually kept up to date by git pulling whenever there are new commits upstream.

```bash
# in order to install system-wide, run
$ git clone https://github.com/opencomputeproject/ocp-diag-python.git
$ cd ocp-diag-python
$ git checkout dev # dev branch has the latest code

# [option 1] install to system, inside the ocp-diag-python dir
$ pip install -e .

# [option 2] for a venv install, inside your python diagnostic rootdir, create and/or activate
$ python -m venv env # optional if already created
$ source env/bin/activate
$ pip install -e path/to/git_cloned/ocp-diag-python
```

The instructions above assume a Linux-type system. However, the steps should be identical on Windows and MacOS platforms.

See [docs.python.org](https://docs.python.org/3/library/venv.html) for more details on how to use python venvs.

### Usage

The specification does not impose any particular level of usage. To be compliant, a diagnostic package just needs output the correct artifact messages in the correct format. However, any particular such diagnostic is free to choose what aspects it needs to use/output; eg. a simple validation test may not output any measurements, opting to just have a final Diagnosis outcome.

**Full API reference is available [here](https://github.com/opencomputeproject/ocp-diag-python/docs/index.md).**

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

### Developer notes

If you would like to contribute, please head over to [developer notes](https://github.com/opencomputeproject/ocp-diag-python/developer_notes.md) for instructions regarding setting up a development environment and more on submitting code.

### Contact

Feel free to start a new [discussion](https://github.com/opencomputeproject/ocp-diag-python/discussions), or otherwise post an [issue/request](https://github.com/opencomputeproject/ocp-diag-python/issues).

An email contact is also available at: ocp-test-validation@OCP-All.groups.io

<!--
due to https://github.com/pypa/readme_renderer/issues/163 we must use absolute links everywhere
-->