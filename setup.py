#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

here = os.path.split(__file__)[0]
bin_dir = os.path.join(here, "pclpy_dependencies", "bin")
package_data = [os.path.join(bin_dir, dll) for dll in os.listdir(bin_dir)]

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
    include_package_data=True,
    keywords='pclpy_dependencies',
    name='pclpy_dependencies',
    packages=find_packages(include=['pclpy_dependencies']),
    package_data={"pclpy_dependencies": package_data},
    python_requires='==3.6.*',
    setup_requires=setup_requirements,
    url='https://github.com/davidcaron/pclpy_dependencies',
    version='0.1.0',
    zip_safe=False,
)
