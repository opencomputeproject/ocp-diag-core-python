import pytest

import ocptv.output as tv
from ocptv.output import TestStatus
from ocptv.output.emit import ArtifactEmitter

from .checks import IgnoreAssert, assert_json
from .conftest import MockWriter


@pytest.fixture
def emitter(writer: MockWriter) -> ArtifactEmitter:
    return ArtifactEmitter(writer)


def test_step_properties(emitter: ArtifactEmitter):
    step = tv.TestStep(name="step0", step_id=1, emitter=emitter)

    assert step.name == "step0"
    assert step.id == 1


def test_step_error_emits_outcome(writer: MockWriter, emitter: ArtifactEmitter):
    step = tv.TestStep(name="step0", step_id=1, emitter=emitter)

    try:
        with step.scope():
            raise tv.TestStepError(status=TestStatus.SKIP)
    except tv.TestStepError:
        assert False, "step scope failed to catch control exception"

    assert len(writer.lines) == 3
    assert_json(
        writer.lines[2],
        {
            "testStepArtifact": {
                "testStepEnd": {"status": "SKIP"},
                "testStepId": "1",
            },
            "sequenceNumber": 2,
            "timestamp": IgnoreAssert(),
        },
    )
