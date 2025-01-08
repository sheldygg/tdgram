from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSchedulingStateSendWhenVideoProcessed(BaseType):
    """
    The message will be sent when the video in the message is converted and optimized; can be used only by the server
    """

    __type__: Literal["messageSchedulingStateSendWhenVideoProcessed"] = (
        "messageSchedulingStateSendWhenVideoProcessed"
    )

    send_date: int
    """Approximate point in time (Unix timestamp) when the message is expected to be sent"""
