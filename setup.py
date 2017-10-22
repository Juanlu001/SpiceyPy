"""
The MIT License (MIT)

Copyright (c) [2015-2017] [Andrew Annex]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

__author__ = 'AndrewAnnex'


TEST_DEPENDENCIES = ['pytest>=2.9.0', 'six>=1.9.0']
DEPENDENCIES      = ['numpy>=1.8.0', 'six>=1.9.0']

# py.test integration from pytest.org
class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


readme = open('README.rst', 'r')
readmetext = readme.read()
readme.close()

setup(
    name='spiceypy',
    version='2.0.0',
    license='MIT',
    author='Andrew Annex',
    author_email='ama6fy@virginia.edu',
    description='A Python Wrapper for the NAIF CSPICE Toolkit',
    long_description=readmetext,
    keywords=['spiceypy', 'spice', 'naif', 'jpl', 'space', 'geometry'],
    url='https://github.com/AndrewAnnex/SpiceyPy',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows"
    ],
    packages=find_packages(exclude=["*.tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    cmdclass={'test': PyTest},
    test_suite='spiceypy.tests.test_wrapper.py',
    extras_require={'testing': ['pytest']}
)
