import pathlib
import setuptools
import subprocess


# Get the current version
version = subprocess.run(["git", "tag"], check=True, stdout=subprocess.PIPE)

setuptools.setup(
    name="quotation",
    version=version.stdout.decode("utf-8").strip(),
    author="mjfactor",
    author_email="emjayfactor@gmail.com",
    description="A simple quotation application",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/mjfactor/Quotation-Calcu",
    packages=setuptools.find_packages(),
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