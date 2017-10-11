import os
from setuptools import setup, find_packages

setup(
    name = "hive-thrift-py",
    version = "0.0.1",
    author = "Youngwoo Kim",
    author_email = "warwithin@gmail.com",
    description = ("Hive Python Thrift Libs"),
    long_description="Hive Python Thrift Libs",
    license = "Apache License",
    keywords = "hive hadoop thrift",
    use_2to3 = True,
    url = "http://hive.apache.org",
    packages=find_packages('src/'),
    package_dir = {'':'src'},
    zip_safe = True,
)
