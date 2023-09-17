#!/bin/bash

# fail early
set -e


### test import in virtualenvs

pushd /libdnf-shim
tox
popd


### test import on local system

PYTHON=python3
PLATFORM_PYTHON=/usr/libexec/platform-python
if [ ! -x "${PYTHON}" -a -x "${PLATFORM_PYTHON}" ]; then
    # fallback to platform-python
    PYTHON="${PLATFORM_PYTHON}"
fi

${PYTHON} -m build --wheel /libdnf-shim
# failure to install is most likely caused by existing LIBDNF bindings, consider it a success
${PYTHON} -m pip install /libdnf-shim/dist/*.whl || true
${PYTHON} /libdnf-shim/tests/import.py
${PYTHON} -m pip check
