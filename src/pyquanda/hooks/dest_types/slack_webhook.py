#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abstract method for other modules."""

import json
from json.decoder import JSONDecodeError
from typing import Any, Dict
from base64 import b64encode

import requests

import aiohttp
import validators  # pylint: disable=import-error
from jinja2 import Template, environment as jenv

from pyquanda.environment import INTERVIEW_CONFIG_REMOTE_FILE, HOOK_DIR
from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks import Hook
from pyquanda.hooks.config import DEST_TYPE_SLACK_WEBHOOK
from pyquanda.environment import LOG

SLACK_HOOK_DIR = HOOK_DIR.joinpath(DEST_TYPE_SLACK_WEBHOOK)


def _json_pp(dct: Dict) -> str:
    """_json_pp.

    Args:
        dct (Dict): dct

    Returns:
        str: pretty dumped json
    """
    return json.dumps(dct, indent=4, separators=(",", " : "))


def _to_b64(inp: str) -> str:
    """_to_b64.

    Args:
        inp (str): inp

    Returns:
        str: base64 encoded str
    """
    return b64encode(inp.encode()).decode()


def _titleize(inp: str) -> str:
    """_titleize.

    Args:
        inp (str): inp

    Returns:
        str: titlized str (i.e foo_bar == Foo Bar)
    """
    arr = inp.split("_")
    return " ".join(i.title() for i in arr)


def _json_str(inp: str) -> str:
    """_json_str.

    Args:
        inp (str): inp

    Returns:
        str: json escaped string
    """
    if not inp:
        return ""
    return json.dumps(inp).strip('"')


def _code_block(inp: str) -> str:
    """_code_block.

    Args:
        inp (str): inp

    Returns:
        str: github style code block
    """
    return "\n".join(
        [
            "```",
            inp,
            "```",
        ]
    )


def _trunc_str(inp: str, slen=50) -> str:
    if not inp:
        return ""
    return f"{inp[:slen]}[...]"


def _retcode(inp: str) -> str:
    inp = str(inp)
    if not inp:
        return ""
    if inp == "0":
        return ":ok:"
    return f":x: {inp}"


jenv.DEFAULT_FILTERS["jstr"] = _json_str  # type: ignore
jenv.DEFAULT_FILTERS["json_pp"] = _json_pp  # type: ignore
jenv.DEFAULT_FILTERS["to_b64"] = _to_b64  # type: ignore
jenv.DEFAULT_FILTERS["titleize"] = _titleize  # type: ignore
jenv.DEFAULT_FILTERS["code"] = _code_block  # type: ignore
jenv.DEFAULT_FILTERS["trunc"] = _trunc_str  # type: ignore
jenv.DEFAULT_FILTERS["rc"] = _retcode  # type: ignore


class SlackSend:
    """Send slack messages to ops-interviews channel."""

    def __init__(self, webhook_url: str):
        """__init__.

        Args:
            webhook_url (str): webhook_url
        """
        self.webhook_url = webhook_url
        self._log = None

    @property
    def log(self):
        """Slack logger."""
        if self._log:
            return self._log
        self._log = LOG.getChild("slack-webhook")
        return self._log

    def send(self, dct: Dict):
        """send.

        Args:
            dct (Dict): dct
        """
        # print(json.dumps(dct, indent=4, separators=(",", " : ")))
        requests.post(self.webhook_url, json=dct)

    async def async_send(self, dct: Dict):
        """Hit send."""
        # print(json.dumps(dct, indent=4, separators=(",", " : ")))
        async with aiohttp.ClientSession() as sess:
            async with sess.post(self.webhook_url, json=dct) as resp:
                await resp.read()


class SlackWebhook(Hook):
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
        self.config = config  # type: Dict

        _url = self._get_config_var("slack_webhook_url")
        if not validators.url(_url):
            raise PreCheckFail(f"{_url} is not a valid url")

        self.url = _url
        self.slack = SlackSend(self.url)

        if not (SLACK_HOOK_DIR.exists() and SLACK_HOOK_DIR.is_dir()):
            raise PreCheckFail(
                f"{SLACK_HOOK_DIR} does not exist, or is not a directory"
            )
        self._template_dir = SLACK_HOOK_DIR
        self.tfile = self._template_dir.joinpath(f"{self.name}.j2.json")
        self.template = self._get_template()

    def _get_template(self) -> Template:
        """_set_templates."""
        self._validate_template()
        return Template(self.tfile.read_text())

    def _validate_template(self):
        """_validate_template."""
        if not self.tfile.exists():
            raise PreCheckFail(
                f"the following hook templates do not exist: {self.tfile}"
            )
        txt = self.tfile.read_text()
        try:
            json.loads(txt)
        except JSONDecodeError as _e:
            raise PreCheckFail(f"malformed json in {self.tfile}") from _e

    def _get_config_var(self, key: str) -> Any:
        """_get_config_var.

        Args:
            key (str): key

        Returns:
            Any: config variable

        Raises:
            PreCheckFail: if configuration error
        """
        if not self.config.get(key):
            raise PreCheckFail(
                f'"{key}" variable is not set in'
                f" {INTERVIEW_CONFIG_REMOTE_FILE} in the hooks section for"
                f" type {DEST_TYPE_SLACK_WEBHOOK}"
            )
        return self.config[key]

    def _getmsg(self, dct: Dict) -> Dict:
        """_getmsg.

        Args:
            dct (Dict): dct

        Returns:
            SlackMessage: slack message
        """
        send_d = self.fmt_json(dct)
        tout = self.template.render(**send_d)
        return json.loads(tout)

    def send(self, dct: Dict):
        """send.

        Args:
            dct (Dict): dct
        """
        msg = self._getmsg(dct)
        self.slack.send(msg)

    async def async_send(self, dct: Dict):
        """send.

        Args:
            dct (Dict): dct
        """
        msg = self._getmsg(dct)
        await self.slack.async_send(msg)
