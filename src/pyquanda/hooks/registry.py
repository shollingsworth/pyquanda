#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""response hook registry"""

from typing import Dict

from pyquanda.environment import INTERVIEW_CONFIG_REMOTE_FILE
from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks import Hook
from pyquanda.hooks.config import (
    CONFIG_REQS,
    DEST_TYPE_EXECUTABLE,
    DEST_TYPE_SLACK_WEBHOOK,
    DEST_TYPE_WEBHOOK_NO_AUTH,
    HOOK_TYPE_ALL,
    VALID_HOOK_TYPES,
    ASYNC_EMITTER,
    SYNC_EMITTER,
)
from pyquanda.hooks.dest_types.executable import ExecutableDest
from pyquanda.hooks.dest_types.slack_webhook import SlackWebhook
from pyquanda.hooks.dest_types.webhook_no_auth import WebHookNoAuth
from pyquanda.lib.yaml_util import load_from_path

DEST_MAP = {
    DEST_TYPE_EXECUTABLE: ExecutableDest,
    DEST_TYPE_WEBHOOK_NO_AUTH: WebHookNoAuth,
    DEST_TYPE_SLACK_WEBHOOK: SlackWebhook,
}


class HookLoader:
    """Loader."""

    LOADED = False

    @classmethod
    def load(cls):
        """initialize class."""
        if cls.LOADED:
            return
        data = load_from_path(INTERVIEW_CONFIG_REMOTE_FILE)  # type: Dict
        # no hooks defined
        try:
            hooks = data.pop("hooks")
        except KeyError as _e:
            return
        for i in hooks:
            for key in CONFIG_REQS:
                try:
                    i[key]
                except KeyError as _e:
                    raise PreCheckFail(
                        f"{key} is missing from config in"
                        f" {INTERVIEW_CONFIG_REMOTE_FILE}"
                    ) from _e
            config = i["config"]
            evt_type = i["event_type"]
            dtype = i["dest_type"]
            if evt_type not in VALID_HOOK_TYPES:
                msg = ",".join(VALID_HOOK_TYPES)
                raise PreCheckFail(f"{evt_type} is not in {msg}")

            if evt_type == HOOK_TYPE_ALL:
                for z in VALID_HOOK_TYPES:
                    if z == HOOK_TYPE_ALL:
                        continue
                    dest = DEST_MAP[dtype](z, config)  # type: Hook
                    ASYNC_EMITTER.on(z, dest.async_send)
                    SYNC_EMITTER.on(z, dest.send)
            else:
                dest = DEST_MAP[dtype](evt_type, config)  # type: Hook
                ASYNC_EMITTER.on(evt_type, dest.async_send)
                SYNC_EMITTER.on(evt_type, dest.send)
        cls.LOADED = True
