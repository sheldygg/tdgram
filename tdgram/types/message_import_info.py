from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageImportInfo(BaseType):
    """
    Contains information about a message created with importMessages
    """

    __type__: Literal["messageImportInfo"] = "messageImportInfo"

    sender_name: str
    """Name of the original sender"""
    date: int
    """Point in time (Unix timestamp) when the message was originally sent"""
