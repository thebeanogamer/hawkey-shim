# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

"""
HAWKEY shim module for use in virtualenvs
"""

import importlib
import json
import logging
import platform
import subprocess
import sys
from pathlib import Path
from typing import List

PROJECT_NAME = "hawkey-shim"
MODULE_NAME = "hawkey"

logger = logging.getLogger(PROJECT_NAME)


class ShimAlreadyInitializingError(Exception):
    pass


def get_system_sitepackages() -> List[str]:
    """
    Gets a list of sitepackages directories of system Python interpreter(s).

    Returns:
        List of paths.
    """

    def get_sitepackages(interpreter):
        command = [
            interpreter,
            "-c",
            "import json, site; print(json.dumps(site.getsitepackages()))",
        ]
        output = subprocess.check_output(command)
        return json.loads(output.decode())

    majorver, *_ = platform.python_version_tuple()
    # try platform-python first (it could be the only interpreter present on the system)
    interpreters = ["/usr/libexec/platform-python", f"/usr/bin/python{majorver}"]
    result = []
    for interpreter in interpreters:
        if not Path(interpreter).is_file():
            continue
        sitepackages = get_sitepackages(interpreter)
        formatted_list = "\n".join(sitepackages)
        logger.debug(f"Collected sitepackages for {interpreter}:\n{formatted_list}")
        result.extend(sitepackages)
    return result


def try_path(path: str) -> bool:
    """
    Tries to load system HAWKEY module from the specified path.

    Returns:
        True if successful, False otherwise.
    """
    if not (Path(path) / MODULE_NAME).is_dir():
        return False
    sys.path.insert(0, path)
    try:
        importlib.reload(sys.modules[__name__])
        # sanity check
        basearch = sys.modules[__name__].detect_arch()
        return basearch is not None
    finally:
        del sys.path[0]
    return False


def initialize() -> None:
    """
    Initializes the shim. Tries to load system HAWKEY module and replace itself with it.
    """
    for path in get_system_sitepackages():
        logger.debug(f"Trying {path}")
        try:
            if try_path(path):
                logger.debug("Import successfull")
                return
        except ShimAlreadyInitializingError:
            continue
        except Exception as e:
            logger.debug(f"Exception: {type(e)}: {e}")
            continue
    else:
        raise ImportError(
            "Failed to import system HAWKEY module. "
            "Make sure HAWKEY Python bindings are installed on your system."
        )


_shim_module_initializing_ = False

if not _shim_module_initializing_:
    _shim_module_initializing_ = True
    initialize()
else:
    raise ShimAlreadyInitializingError
