from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentContact(BaseType):
    """
    A message with a user contact
    """

    __type__: Literal["pushMessageContentContact"] = "pushMessageContentContact"

    name: str
    """Contact's name"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
