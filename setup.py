from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the description from the readme.md
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='cfgtodict',
  version='0.1.0',
  description='A simple class for converting a *.cfg file to a Python Dictionary',
  long_description=long_description,
  url='https://github.com/joelklabo/cfgtodict',
  author='Joel Klabo',
  author_email='joelklabo@gmail.com',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Utility',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4'
  ],
  keywords='config dictionary utilities',
  py_module=['cfgtodict']
)
