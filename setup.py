from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
#long_description = ""

#try:
#    from pypandoc import convert
#    if path.exists(path.join(here, 'README.md')):
#        long_description = convert('README.md', 'rst')
#except ImportError:
#    print("warning: pypandoc module not found, could not convert Markdown to RST")

setup(
    name='file-structure-generator',
    version='0.0.1',
    description='A folder structure generator tool.',
    #long_description=long_description,
    url='https://github.com/mjalas/command-line-parser',
    author='Mats Jalas',
    author_email='mats.jalas@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='folder-generator',
    setup_requires=[
        'command-line-parser>=0.0.3',
        'PyYAML==3.12', 'nose>=1.0',
        'coverage>=4.0.3',
        'pypandoc>=1.1.3'
    ],
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'structure-generator=src.__main__:main'
        ]
    }
)