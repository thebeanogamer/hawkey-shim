# libdnf-shim

Python LIBDNF shim module for use in virtalenvs.

## Purpose

LIBDNF Python bindings are tied to system LIBDNF installation and are not available as a Python package (on PyPI or elsewhere). This shim module makes it possible to import and use the bindings in a virtualenv.

There is no point installing this shim module on a bare system, outside of a virtualenv. It should still work, but there is no benefit. If you want to do that anyway, pay attention not to overwrite installed LIBDNF Python bindings.

## Example

Here is a scenario of how this module enables usage of LIBDNF Python bindings in a newly created virtualenv. First commands are run on a host system.

```bash
# make sure LIBDNF Python bindings are installed and functional
$ libdnf -q python3-libdnf
python3-libdnf-0.70.2-1.fc39.x86_64

$ pip list
Package    Version
---------- -------
libdnf        0.70.2

$ python -c "import libdnf; print(libdnf.__version__)"
0.70.2

# let's create a virtualenv
$ python -m venv env
$ source env/bin/activate

# the bindings are not accessible there
(env) $ python -c "import libdnf; print(libdnf.__version__)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'libdnf'

# install the shim module from PyPI
(env) $ pip install libdnf
...
Successfully installed libdnf-0.1.0

# now we can import the bindings
(env) $ python -c "import libdnf; print(libdnf.__version__)"
0.70.2
```
