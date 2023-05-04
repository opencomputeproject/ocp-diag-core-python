import sys
from pathlib import Path

# add the local lib to sys.path for discovery
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from . import DEMOS

# basically import for side-effects; the decorator `demo`
# registers the functions into the DEMOS dict
from .advanced import *
from .config import *
from .extension import *
from .external import *
from .measurements import *
from .simple import *


def list_demos():
    for k in DEMOS.keys():
        print(k)


if len(sys.argv) >= 2:
    # user wanted a specific demo, or listing
    name = sys.argv[1]
    if name in DEMOS.keys():
        DEMOS[name](banner=False)
    elif name == "list":
        list_demos()
else:
    # run all demos
    for v in DEMOS.values():
        v()
