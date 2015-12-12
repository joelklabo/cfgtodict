from distutils.core import setup

setup(
  name='cfgtodict',
  version='0.1.3',
  description='A simple class for converting a *.cfg file to a Python Dictionary',
  url='https://github.com/joelklabo/cfgtodict',
  author='Joel Klabo',
  author_email='joelklabo@gmail.com',
  license='MIT',
  classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries"
  ],
  install_requires=[
    'configparser'
  ]
)
