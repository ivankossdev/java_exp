# python setup.py build
# pip install cx_Freeze
from cx_Freeze import setup, Executable

executables = [Executable('main.py', base="Win32GUI", target_name="Board time")]

setup(name='Board time',
      version='2.3.2',
      description='Ivan.Koss_developer',
      executables=executables)