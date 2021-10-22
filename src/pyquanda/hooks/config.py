#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""constants for module."""
import asyncio
import sys

from pyee import (  # pylint: disable=import-error
    AsyncIOEventEmitter as _Emitter,
)

# For the shell
ASYNC_EMITTER = _Emitter(asyncio.get_event_loop())
# For ansible mostly
SYNC_EMITTER = _Emitter(asyncio.get_event_loop())

DEST_TYPE_WEBHOOK_NO_AUTH = "webhook_no_auth"
DEST_TYPE_EXECUTABLE = "executable"
DEST_TYPE_SLACK_WEBHOOK = "slack_webhook"

HOOK_TYPE_ALL = "all"
HOOK_TYPE_ANSWER = "xonsh_answer"
HOOK_TYPE_XONSH_COMMAND_ENTERED = "xonsh_command"
HOOK_TYPE_QUESTIONABLE = "questionable_activity"

HOOK_TYPE_NAV_NEXT = "nav_next"
HOOK_TYPE_NAV_PREVIOUS = "nav_previous"

HOOK_TYPE_ANSIBLE_EVENT = "ansible_event"
HOOK_TYPE_ANSIBLE_RUNBOOK_COMPLETE = "runbook_complete"

_MOD = sys.modules[__name__]
VALID_DEST_TYPES = [
    getattr(_MOD, i) for i in dir(_MOD) if i.startswith("DEST_TYPE_")
]
VALID_HOOK_TYPES = [
    getattr(_MOD, i) for i in dir(_MOD) if i.startswith("HOOK_TYPE_")
]

CONFIG_REQS = ["dest_type", "event_type", "config"]
