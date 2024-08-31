from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageCustomServiceAction(BaseType):
    """
    A non-standard action has happened in the chat
    """

    __type__: Literal["messageCustomServiceAction"] = "messageCustomServiceAction"

    text: str
    """Message text to be shown in the chat"""
