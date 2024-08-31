from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventMessageAutoDeleteTimeChanged(BaseType):
    """
    The message auto-delete timer was changed
    """

    __type__: Literal["chatEventMessageAutoDeleteTimeChanged"] = (
        "chatEventMessageAutoDeleteTimeChanged"
    )

    old_message_auto_delete_time: int
    """Previous value of message_auto_delete_time"""
    new_message_auto_delete_time: int
    """New value of message_auto_delete_time"""
