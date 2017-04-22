import os
import setuptools
import setuptools.command.install
import shutil
import sys
import json


setuptools.setup(
    name='dellve',
    version='0.1.2',
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'dellve': [
            'data/jinja2/*',
            'data/config.json'
        ]
    },
    install_requires=[
        'click',
        'daemonocle',
        'falcon',
        'gevent',
        'jinja2',
        'pick',
        'requests',
        'stringcase',
        'tqdm'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
    entry_points='''
        [console_scripts]
        dellve=dellve.cli:cli
    '''
)
