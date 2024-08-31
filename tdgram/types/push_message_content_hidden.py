from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentHidden(BaseType):
    """
    A general message with hidden content
    """

    __type__: Literal["pushMessageContentHidden"] = "pushMessageContentHidden"

    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
