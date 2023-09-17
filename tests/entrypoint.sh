#!/bin/bash

# fail early
set -e


### test import in virtualenvs

pushd /hawkey-shim
tox
popd


### test import on local system

PYTHON=python3
PLATFORM_PYTHON=/usr/libexec/platform-python
if [ ! -x "${PYTHON}" -a -x "${PLATFORM_PYTHON}" ]; then
    # fallback to platform-python
    PYTHON="${PLATFORM_PYTHON}"
fi

${PYTHON} -m build --wheel /hawkey-shim
# failure to install is most likely caused by existing HAWKEY bindings, consider it a success
${PYTHON} -m pip install /hawkey-shim/dist/*.whl || true
${PYTHON} /hawkey-shim/tests/import.py
${PYTHON} -m pip check
