#!/usr/bin/env python

from setuptools import find_packages, setup
import os

appScriptsName = ['pyrpn']
appScripts = [os.path.join('scripts', scriptname) for scriptname in appScriptsName]

setup(
        name = "pyrpn",
        version = "1.0.0",
        description = "rpn calculator",
        long_description = "solve reverse polish notation expression",
        platforms = ['Linux'],
        author = "Tong Zhang",
        author_email = "zhangtong@sinap.ac.cn",
        license = "MIT",
        url = 'https://github.com/Archman/pyrpn',
        packages = find_packages(exclude=['tests*']),
        scripts = appScripts,
        classifiers=[
            "Programming Language :: Python",
        ],
)
