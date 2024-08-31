from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSchedulingStateSendAtDate(BaseType):
    """
    The message will be sent at the specified date
    """

    __type__: Literal["messageSchedulingStateSendAtDate"] = "messageSchedulingStateSendAtDate"

    send_date: int
    """Point in time (Unix timestamp) when the message will be sent. The date must be within 367 days in the future"""
