from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageFileTypePrivate(BaseType):
    """
    The messages were exported from a private chat
    """

    __type__: Literal["messageFileTypePrivate"] = "messageFileTypePrivate"

    name: str | None = None
    """Name of the other party; may be empty if unrecognized"""
