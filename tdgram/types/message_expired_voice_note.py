from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageExpiredVoiceNote(BaseType):
    """
    A self-destructed voice note message
    """

    __type__: Literal["messageExpiredVoiceNote"] = "messageExpiredVoiceNote"
