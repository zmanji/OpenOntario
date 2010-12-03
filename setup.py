#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'OpenOntario',
    version='0.1dev',
    packages=['openontario',],
    license='GNU General Public License V3',
    description="The Open Ontario Project",
    url="https://github.com/zmanji/OpenOntario",
    author="Zameer Manji",
    author_email="zmanji@gmail.com",
    long_description=open('README.rst').read(),
)
