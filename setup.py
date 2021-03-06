#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup File py PyQ[u]AndA."""

from pathlib import Path

from setuptools import setup

REQS = (
    Path(__file__).parent.joinpath("requirements.txt").read_text().splitlines()
)

setup(
    name="pyquanda",
    scripts=[
        "bin/pyquanda-cmd",
    ],
    install_requires=REQS,
    extras_require={
        "ansible": [
            "ansible-runner==2.0.3",
            "ansible==4.8.0",
        ],
    },
)
