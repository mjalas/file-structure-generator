# File structure generator tool
[![PyPI version](https://badge.fury.io/py/file-structure-generator.svg)](https://badge.fury.io/py/file-structure-generator)
[![Build Status](https://travis-ci.org/mjalas/file-structure-generator.svg?branch=master)](https://travis-ci.org/mjalas/file-structure-generator)

A simple tool for generating a file structure according to a configuration file.

## Installation

There are currently two different ways of installing the application.

Through pip:
```
pip install file-structure-generator
```

Manually:
```
git clone https://github.com/mjalas/file-structure-generator.git
cd command-line-parser
python setup.py install
```

The application is installed under the name 'structure-generator'

## Usage

The tool generates a folder structure based on a yaml configuration file, example below:
```
hierarchy:
    parent:
        - child1 :
            - grandchild1 : ""
            - grandchild2 : ""
        - child2 :
            - grandchild3 : ""
        - child3 :
            - grandchild4 : ""
            - grandchild5 : ""   
```

To generate the structure in the current location run the following command:
```
structure-generator -f <path/to/example>/example_structure.yml
```

To generate the structure to a different location run the following command:
```
structure-generator -f <path/to/example>/example_structure.yml -o <path/to/output/location>
```