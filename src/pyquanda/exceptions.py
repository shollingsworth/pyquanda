#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exceptions for application."""


class PreCheckFail(Exception):
    """Throw if Terraform precheck fails."""


class ErrorBadConfig(Exception):
    """Throw if the main configuration is bad."""
