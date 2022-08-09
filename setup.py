#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

# Get common version number (https://stackoverflow.com/a/7071358)
import re
VERSIONFILE="scoords/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(name='scoords',
      version = verstr,
      author='COSI Team',
      author_email='imc@umd.edu',
      url='https://github.com/cositools/scoords',
      packages = find_packages(include=["scoords", "scoords.*"]),
      install_requires = ['numpy', 'scipy', 'astropy'],
      description = "Spacecraft coordinates.",
      long_description = long_description,
      long_description_content_type="text/markdown",
      )

