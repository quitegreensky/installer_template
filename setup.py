
from setuptools import setup, find_packages
import sample_package
requirements_path='requirements.txt'

with open("README.md", "r") as fh:
    long_description = fh.read()

def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements(requirements_path)
setup(
    name=sample_package.__package_name__,
    version=str(sample_package.__version__),
    description=sample_package.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=sample_package.__url__,
    author=sample_package.__author__,
    author_email=sample_package.__email__,
    license='MIT',
    install_requires=parse_requirements(requirements_path) ,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
      )