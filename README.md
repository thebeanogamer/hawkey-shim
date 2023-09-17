# hawkey-shim

Python HAWKEY shim module for use in virtalenvs.

## Purpose

HAWKEY Python bindings are tied to system HAWKEY installation and are not available as a Python package (on PyPI or elsewhere). This shim module makes it possible to import and use the bindings in a virtualenv.

There is no point installing this shim module on a bare system, outside of a virtualenv. It should still work, but there is no benefit. If you want to do that anyway, pay attention not to overwrite installed HAWKEY Python bindings.

## Example

Here is a scenario of how this module enables usage of HAWKEY Python bindings in a newly created virtualenv. First commands are run on a host system.

```bash
# make sure HAWKEY Python bindings are installed and functional
$ hawkey -q python3-hawkey
python3-hawkey-0.70.2-1.fc39.x86_64

$ pip list
Package    Version
---------- -------
hawkey        0.70.2

$ python -c "import hawkey; print(hawkey.__version__)"
0.70.2

# let's create a virtualenv
$ python -m venv env
$ source env/bin/activate

# the bindings are not accessible there
(env) $ python -c "import hawkey; print(hawkey.__version__)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'hawkey'

# install the shim module from PyPI
(env) $ pip install hawkey
...
Successfully installed hawkey-0.1.0

# now we can import the bindings
(env) $ python -c "import hawkey; print(hawkey.__version__)"
0.70.2
```
