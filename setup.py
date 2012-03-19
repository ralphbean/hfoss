"""Setuptools setup file"""

import sys, os
import multiprocessing, logging

from setuptools import setup

setup(
    name='hfoss',
    version='0.1',
    description="Materials for teaching the HFOSS course at RIT",
    install_requires=[
        'Sphinx',
        'cloud_sptheme',
        'pyyaml',
        'feedparser',
    ],
    url = "http://teachingopensource.org/index.php/RIT",
    download_url = "https://github.com/ralphbean/hfoss",
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    license='GPLv3+',
    packages = [],
    namespace_packages = [],
    include_package_data=True,
    zip_safe=False,
    classifiers = [],
)
