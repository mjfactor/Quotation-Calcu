import pathlib
import os
import re
import subprocess

from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

# Check if the current directory is a git repository it has at least one tag
if os.path.exists('.git') and subprocess.call(['git', 'tag'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
    # Get Latest Tag
    git_describe_output = subprocess.check_output(["git", "describe", "--tags"]).strip().decode('utf-8')
    # Extract the tag and the number of additional commits
    match = re.match(r'(\d+\.\d+\.\d+)-(\d+)-g[a-f0-9]+', git_describe_output)
    if match:
        # Use the tag as the version, and append the number of additional commits as a post-release segment
        version = f'{match.group(1)}.post{match.group(2)}'
    else:
        # If the output does not match the expected format, use the whole output as the version
        version = git_describe_output
else:
    version = '0.0.0'  # Default version if not a git repository or no tags

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