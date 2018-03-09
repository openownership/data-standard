# This is a dummy package, which exists so we can run pip twice on readthedocs
import subprocess
from setuptools import setup
setup()

subprocess.call(['pip', 'install', '-r', 'pre_requirements.txt'],
    cwd='..')
subprocess.call(['pip', 'install', '-r', 'requirements.txt'],
    cwd='..')
