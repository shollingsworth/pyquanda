#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aws API Gateway Hook"""
import json
from typing import Dict

import aiohttp
import boto3
import requests

import validators  # pylint: disable=import-error
from botocore import auth, awsrequest
from pyquanda.environment import INTERVIEW_CONFIG_REMOTE_FILE
from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks import Hook
from pyquanda.hooks.config import DEST_TYPE_AWS_API_GATEWAY


class WebHookAwsApiGw(Hook):
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
                f" type {DEST_TYPE_AWS_API_GATEWAY}"
            )
        _url = config["url"]
        if not validators.url(_url):
            raise PreCheckFail(f"{_url} is not a valid url")
        self.url = _url
        self._credentials = boto3.Session().get_credentials()

    def sign_headers(self, payload: Dict):
        """Sign AWS API request headers."""
        service = "execute-api"
        region = "us-east-2"
        request = awsrequest.AWSRequest(
            method="POST",
            url=self.url,
            data=json.dumps(payload),
        )
        auth.SigV4Auth(self._credentials, service, region).add_auth(request)
        return dict(request.headers.items())

    async def async_send(self, dct: Dict):
        """async_send.

        Args:
            dct (Dict): dct
        """
        dct = self.fmt_json(dct)
        s_headers = self.sign_headers(dct)
        async with aiohttp.ClientSession(
            headers=s_headers,
        ) as sess:
            return await sess.post(self.url, json=dct)

    def send(self, dct: Dict):
        """send.

        Args:
            dct (Dict): dct
        """
        dct = self.fmt_json(dct)
        s_headers = self.sign_headers(dct)
        print(s_headers, dct)
        return requests.post(self.url, headers=s_headers, json=dct)


#
#  async def amain(hook: WebHookAwsApiGw, dct: Dict):
#      """Run main function."""
#      dct = dct.copy()
#      dct["foo"] = "bar"
#      req = await hook.async_send(dct)
#      print("async", await req.content.read())
#
#
#  def main():
#      """Run main function."""
#      HOST = "https://hdzbfthug8.execute-api.us-east-2.amazonaws.com/api"
#      config = {"url": f"{HOST}/pq_event"}
#      send = {"test": "hello world", "blarg": True}
#      hook = WebHookAwsApiGw(name="testing", config=config)
#      req = hook.send(send)
#      print(req.content)
#
#      # Async
#      asyncio.run(amain(hook, send))
#
#
#  if __name__ == "__main__":
#      import asyncio
#
#      main()
