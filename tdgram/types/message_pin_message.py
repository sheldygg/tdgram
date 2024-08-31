from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessagePinMessage(BaseType):
    """
    A message has been pinned
    """

    __type__: Literal["messagePinMessage"] = "messagePinMessage"

    message_id: int
    """Identifier of the pinned message, can be an identifier of a deleted message or 0"""
