from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SentWebAppMessage(BaseType):
    """
    Information about the message sent by answerWebAppQuery
    """

    __type__: Literal["sentWebAppMessage"] = "sentWebAppMessage"

    inline_message_id: str
    """Identifier of the sent inline message, if known"""
