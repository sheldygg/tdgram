from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageFileTypeGroup(BaseType):
    """
    The messages were exported from a group chat
    """

    __type__: Literal["messageFileTypeGroup"] = "messageFileTypeGroup"

    title: str | None = None
    """Title of the group chat; may be empty if unrecognized"""
