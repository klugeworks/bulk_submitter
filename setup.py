try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

VERSION = 1.0
config = {
    'description': 'KlugeBS',
    'author': 'Mr. Kluge',
    'author_email': 'kluge@nowhere.com',
    'version': VERSION,
    'install_requires': ['protobuf', 'redis'],
    'packages': ['kluge_bs', 'kluge_bs.io'],
    'name': 'kluge_bs',
    'scripts': ['scripts/submitter.py'],
}

setup(**config)