from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSendingStatePending(BaseType):
    """
    The message is being sent now, but has not yet been delivered to the server
    """

    __type__: Literal["messageSendingStatePending"] = "messageSendingStatePending"

    sending_id: int
    """Non-persistent message sending identifier, specified by the application"""
