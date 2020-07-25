
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['tcl86t.dll', 'tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('Main.py', base=base)
]

setup(name='editor',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)