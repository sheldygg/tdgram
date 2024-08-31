from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageOriginUser(BaseType):
    """
    The message was originally sent by a known user
    """

    __type__: Literal["messageOriginUser"] = "messageOriginUser"

    sender_user_id: int
    """Identifier of the user that originally sent the message"""
