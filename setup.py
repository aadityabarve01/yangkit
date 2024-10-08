import sys
from setuptools import setup, find_packages

from yangkit.__version__ import __version__

INSTALL_REQUIREMENTS = [
    'pyang==2.5.3',
    'Jinja2==3.0.3'
]

INSTALL_REQUIREMENTS.append('lxml==4.9.3') 

setup(
    name='yangkit',
    version=__version__,
    description='Yang Kit Package',
    author='Cafy',
    author_email='cafy-support@cisco.com',
    url='https://github.com/yang-infra/yangkit',
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages()
)
