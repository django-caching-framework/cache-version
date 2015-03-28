from setuptools import setup, find_packages

setup(name='cache-version',
packages=find_packages(exclude='tests'),
version='0.1.0',
author='Omer Katz',
author_email='omer.drow@gmail.com',
license='BSD3',
include_package_data=True,
)
