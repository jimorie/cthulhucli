# -*- coding: utf-8 -*-

from setuptools import setup
from cthulhucli.cthulhucli import __version__ as version

setup(
    name="cthulhucli",
    packages=["cthulhucli"],  # this must be the same as the name above
    version=version,
    description="A command-line tool for searching Call of Ctulhu CCG and LCG cards.",
    author="Petter Nyström",
    author_email="jimorie@gmail.com",
    url="https://github.com/jimorie/cthulhucli",  # use the URL to the github repo
    download_url="https://github.com/jimorie/cthulhucli/archive/v{}.tar.gz".format(
        version
    ),
    keywords=["call of cthulhu", "cthulhu", "lcg", "ccg"],  # arbitrary keywords
    classifiers=[],
    install_requires=["click"],
    entry_points={"console_scripts": ["cthulhucli=cthulhucli.cthulhucli:main"]},
    include_package_data=True,
    # data_files=[('cthulhucli', ['cthulhucli/*.data'])],
)
