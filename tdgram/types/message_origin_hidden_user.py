from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageOriginHiddenUser(BaseType):
    """
    The message was originally sent by a user, which is hidden by their privacy settings
    """

    __type__: Literal["messageOriginHiddenUser"] = "messageOriginHiddenUser"

    sender_name: str
    """Name of the sender"""
