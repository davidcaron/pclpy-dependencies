#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from os.path import join

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

here = os.path.abspath(os.path.split(__file__)[0])

version_dict = {}
exec(open(join(here, "pclpy_dependencies", "__version__.py")).read(), version_dict)
version = version_dict["__version__"]

bin_dir = join("pclpy_dependencies", "bin")
absolute_bin_dir = join(here, bin_dir)
package_data = [join(absolute_bin_dir, dll) for dll in os.listdir(absolute_bin_dir)]

setup(
    author="David Caron",
    author_email='dcaron05@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Windows dependencies for pclpy: Python bindings for the Point Cloud Library",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    keywords='pclpy_dependencies',
    name='pclpy_dependencies',
    packages=['pclpy_dependencies'],
    package_data={"pclpy_dependencies": package_data},
    python_requires='==3.6.*',
    setup_requires=setup_requirements,
    url='https://github.com/davidcaron/pclpy_dependencies',
    version=version,
    zip_safe=False,
)
