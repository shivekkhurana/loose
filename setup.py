#! /usr/bin/python

from setuptools import setup

setup(
    name = 'loose',
    version = '0.0.2a1',
    description = 'Javascript style objects for python',
    url = 'https://github.com/shivekkhurana/loose',
    author = 'Shivek Khurana',
    author_email = 'khuranashivek@gmail.com',
    license = 'MIT',
    py_modules=['loose'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities'
    ],
    test_suite = 'tests',
    keywords = 'loose, js objects'
)