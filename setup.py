#!usr/bin/env python3

from setuptools import setup

setup(
    name='botwrangler',
    packages=['botwrangler'],
    package_dir={'botwrangler': 'botwrangler'},
    version='1.0.0',
    description='',
    author='cbell504',
    url='https://github.com/cbell504/botwrangler.git',
    author_email='',
    keywords=['botwrangler'],
    entry_points={'console_scripts': [
        'botwrangler = botwrangler.__main__:main',
    ], },
)