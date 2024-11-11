__version__ = "2.0.0"

import logging
import os
import sys

MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = os.path.dirname(MODULE_PATH)
DATA_PATH = f"{REPO_PATH}/data"

# Configuring logs

logger = logging.getLogger(__name__)
logger.propagate = False
handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter("[%(levelname)5s] %(asctime)-15s  %(filename)-15.15s:%(lineno)03d - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
