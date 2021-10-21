#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""constants for module."""
import sys
from pymitter import EventEmitter as _EventEmitter

EMITTER = _EventEmitter()

DEST_TYPE_WEBHOOK_NO_AUTH = "webhook_no_auth"
DEST_TYPE_EXECUTABLE = "executable"

HOOK_TYPE_ALL = "all"
HOOK_TYPE_ANSWER = "xonsh_answer"
HOOK_TYPE_ANSIBLE_EVENT = "ansible_event"
HOOK_TYPE_ANSIBLE_RUNBOOK_COMPLETE = "runbook_complete"
HOOK_TYPE_XONSH_COMMAND_ENTERED = "xonsh_command"
HOOK_TYPE_QUESTIONABLE = "questionable_activity"

_MOD = sys.modules[__name__]
VALID_DEST_TYPES = [
    getattr(_MOD, i) for i in dir(_MOD) if i.startswith("DEST_TYPE_")
]
VALID_HOOK_TYPES = [
    getattr(_MOD, i) for i in dir(_MOD) if i.startswith("HOOK_TYPE_")
]

CONFIG_REQS = ["dest_type", "event_type", "config"]
