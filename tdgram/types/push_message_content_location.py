from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentLocation(BaseType):
    """
    A message with a location
    """

    __type__: Literal["pushMessageContentLocation"] = "pushMessageContentLocation"

    is_live: bool
    """True, if the location is live"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
