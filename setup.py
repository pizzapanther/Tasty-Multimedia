import sys

from setuptools import setup, find_packages

setup(
    name = "tasty-multimedia",
    version = '12.08',
    description = "3rd Party Armstrong CMS app for embedding multimedia into site.",
    url = "https://github.com/pizzapanther/Tasty-Multimedia",
    author = "Paul Bailey",
    author_email = "paul.m.bailey@gmail.com",
    license = "BSD",
    packages = [
      'multimedia',
      'multimedia.migrations',
      'multimedia.templatetags'
    ],
    include_package_data = True,
)

