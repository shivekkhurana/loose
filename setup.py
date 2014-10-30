#! /usr/bin/python

from setuptools import setup

setup(
    name = 'loose',
    version = '0.0.1',
    description = 'Javascript style objects for python',
    url = 'https://github.com/shivekkhurana/loose',
    author = 'Shivek Khurana',
    author_email = 'khuranashivek@gmail.com',
    license = 'MIT',
    py_modules=['loose'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    test_suite = 'tests',
    keywords = 'loose, js objects'
)