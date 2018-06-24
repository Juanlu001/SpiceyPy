"""
The MIT License (MIT)

Copyright (c) [2015-2019] [Andrew Annex]

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
from setuptools import setup
from setuptools.command.test import test as TestCommand
import ssl
import sys


__author__ = 'AndrewAnnex'

TEST_DEPENDENCIES = ['numpy>=1.12.0', 'six>=1.9.0', 'pytest>=2.9.0']
DEPENDENCIES = ['numpy>=1.12.0', 'six>=1.9.0', 'certifi>=2017.1.23']
REQUIRES = ['numpy', 'six']

# If we have an old version of OpenSSL, CSPICE will be downloaded
# (if required) using urllib3.  Extend the list of required packages.
if ssl.OPENSSL_VERSION < 'OpenSSL 1.0.1g':
    DEPENDENCIES.extend(['urllib3[secure]>=1.22', 'pyOpenSSL>=17.3.0'])


class PyTest(TestCommand):
    # py.test integration from pytest.org
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


cmdclass = {
             'test': PyTest}


readme = open('README.rst', 'r')
readmetext = readme.read()
readme.close()

setup(
    name='spiceypy',
    version='2.2.0',
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
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: Microsoft :: Windows"
    ],
    packages=['spiceypy', 'spiceypy.utils'],
    include_package_data=True,
    zip_safe=False,
    package_data={'spiceypy': ['utils/*.so', "utils/*.dll"]},
    install_requires=DEPENDENCIES,
    requires=REQUIRES,
    tests_require=TEST_DEPENDENCIES,
    cmdclass=cmdclass,
    test_suite='spiceypy.tests.test_wrapper.py',
    extras_require={'testing': ['pytest']}
)
