#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path

REQS = (
    Path(__file__).parent.joinpath("requirements.txt").read_text().splitlines()
)

setup(
    name="pyquanda",
    scripts=[
        "bin/pyquandacmd",
    ],
    install_requires=REQS,
)
