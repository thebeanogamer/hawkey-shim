#!/bin/bash

# fail early
set -e


### test import in virtualenvs

pushd /dnf-shim
tox
popd


### test import on local system

PYTHON=python3
PLATFORM_PYTHON=/usr/libexec/platform-python
if [ ! -x "${PYTHON}" -a -x "${PLATFORM_PYTHON}" ]; then
    # fallback to platform-python
    PYTHON="${PLATFORM_PYTHON}"
fi

${PYTHON} -m build --wheel /dnf-shim
# failure to install is most likely caused by existing DNF bindings, consider it a success
${PYTHON} -m pip install /dnf-shim/dist/*.whl || true
${PYTHON} /dnf-shim/tests/import.py
${PYTHON} -m pip check
