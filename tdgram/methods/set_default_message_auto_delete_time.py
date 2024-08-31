from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageAutoDeleteTime, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetDefaultMessageAutoDeleteTime(BaseMethod):
    """
    Changes the default message auto-delete time for new chats
    """

    __type__: Literal["setDefaultMessageAutoDeleteTime"] = "setDefaultMessageAutoDeleteTime"
    __returning_type__ = Ok

    message_auto_delete_time: MessageAutoDeleteTime
    """New default message auto-delete time; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically"""
