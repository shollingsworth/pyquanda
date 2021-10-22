#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Executable type."""

from typing import Dict
import requests
import aiohttp
import validators  # pylint: disable=import-error
from pyquanda.environment import INTERVIEW_CONFIG_REMOTE_FILE
from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks import Hook
from pyquanda.hooks.config import DEST_TYPE_WEBHOOK_NO_AUTH


class WebHookNoAuth(Hook):
    """WebHookNoAuth."""

    def __init__(self, name: str, config: Dict) -> None:
        """__init__.

        Args:
            config (Dict): config

        Returns:
            None:

        Raises:
            PreCheckFail: on validation error
        """
        super().__init__(name, config)
        if not config.get("url"):
            raise PreCheckFail(
                '"url" variable is not set in'
                f" {INTERVIEW_CONFIG_REMOTE_FILE} in the hooks section for"
                f" type {DEST_TYPE_WEBHOOK_NO_AUTH}"
            )
        _url = config["url"]
        if not validators.url(_url):
            raise PreCheckFail(f"{_url} is not a valid url")
        self.url = _url

    async def async_send(self, dct: Dict):
        async with aiohttp.ClientSession() as sess:
            await sess.post(self.url, json=self.fmt_json(dct))

    def send(self, dct: Dict):
        """send.

        Args:
            dct (Dict): dct
        """
        requests.post(self.url, json=self.fmt_json(dct))
