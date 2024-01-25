# https://packaging.python.org/tutorials/packaging-projects/
# https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html

import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hypertext Toolbox",
    version=0.1,
    author="David Chappell",
    author_email="David.Chappell@trincoll.edu",
    description="Utilities for creating web pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/david672orford/hypertext-toolbox",
    #packages=['hypertext_toolbox'],
	scripts=glob("bin/[a-z]*"),
    classifiers=[
		"Topic :: Text Processing :: Markup :: HTML",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[ 'lxml', 'scss', 'rcssmin', 'rjsmin', 'Pillow' ],
)

