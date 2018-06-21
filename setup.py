from setuptools import setup
from irk.util.version import VERSION_STRING


with open("requirements.txt") as f:
    requirements = f.read().splitlines(False)


setup(
    packages=["irk"],
    name="irk",
    version=VERSION_STRING,
    install_requires=requirements,

    author="mincrmatt12",
    description="A meta package manager",
    license="GPLv3",
    url="https://github.com/mincrmatt12/irk",
    entry_points={
        'console_scripts': [
            "irk = irk.main:main"
        ]
    }
)
