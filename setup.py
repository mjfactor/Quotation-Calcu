import pathlib
import os
import re
import subprocess

from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

# Get latest git tag
# Get latest git tag
raw_version = subprocess.check_output(["git", "describe", "--tags"]).strip().decode("utf-8")

# Make the version PEP 440 compliant
version = raw_version.replace('-', '.', 1).replace('g', '')

# Use the absolute path to the readme.md file
readme_path = os.path.join(HERE, 'readme.md')

# Check if the readme.md file exists
if os.path.exists(readme_path):
    with open(readme_path, encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = ''  # Default description if readme.md does not exist

# ... The rest of the setup script


setup(
    name="quotation",
    version=version,
    author="mjfactor",
    author_email="emjayfactor@gmail.com",
    description="A simple quotation application",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/mjfactor/Quotation-Calcu",
    packages=find_packages(),
    project_urls={
        "Source": "https://github.com/mjfactor/Quotation-Calcu"
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.10",
    include_package_data=True,
)
