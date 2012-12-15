import os
from setuptools import setup

from csdl import __version__

setup(
    name = "datasift_csdl_parser",
    version = __version__,
    author = "Nino Walker",
    author_email = "nino.walker@gmail.com",
    description = ("A parser for Datasift's CSDL grammar. See http://dev.datasift.com/csdl"),
    url='https://github.com/ninowalker/datasift-csdl-parser',
    license = "BSD",
    packages=['csdl'],
    long_description=open('README.md').read(),
    install_requires=['pyparsing',],
    setup_requires=['nose>=1.0', 'coverage', 'nosexcover', 'pyyaml'],
    test_suite = 'nose.collector',
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
