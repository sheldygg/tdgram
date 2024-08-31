from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSenderUser(BaseType):
    """
    The message was sent by a known user
    """

    __type__: Literal["messageSenderUser"] = "messageSenderUser"

    user_id: int
    """Identifier of the user that sent the message"""
