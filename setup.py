import re
from pathlib import Path
from setuptools import find_packages, setup

with open(Path(__file__).parent / "kuroutils" / "__init__.py", "r") as fp:
    version = re.search(r"__version__ = \"(\d*\.\d*\.\d*)\"", fp.read()).group(1)

with open("README.md", "r") as fp:
    long_description = fp.read()

with open("requirements.txt") as fp:
    install_requires = fp.read().splitlines()

setup(
    name="Kuro-Utils",
    version=version,
    description="Utils for Kuro-Cogs.",
    long_description=long_description,
    author="Kuro-Rui",
    url="https://github.com/Kuro-Rui/Kuro-Utils",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.8.1",
    install_requires=install_requires,
)
