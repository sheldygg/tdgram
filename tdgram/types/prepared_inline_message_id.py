from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PreparedInlineMessageId(BaseType):
    """
    Represents an inline message that can be sent via the bot
    """

    __type__: Literal["preparedInlineMessageId"] = "preparedInlineMessageId"

    id: str
    """Unique identifier for the message"""
    expiration_date: int
    """Point in time (Unix timestamp) when the message can't be used anymore"""
