'''
Created on 19 Dec 2020

@author: semuadmin
'''
import setuptools

from sandpit import version as VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sandpit",
    version=VERSION,
    author="semuadmin",
    author_email="semuadmin@semuconsulting.com",
    description="UBX Protocol Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semuconsulting/sandpit",
    packages=setuptools.find_packages(exclude=['tests']),
    license="BSD 3-Clause 'Modified' License",
    keywords="2020",
    platforms="Windows, MacOS, Linux",
    project_urls={
        "Source Code": "https://github.com/semuconsulting/pyubx2",
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: BSD License',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
)
