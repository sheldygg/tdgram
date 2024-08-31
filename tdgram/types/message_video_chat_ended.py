from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageVideoChatEnded(BaseType):
    """
    A message with information about an ended video chat
    """

    __type__: Literal["messageVideoChatEnded"] = "messageVideoChatEnded"

    duration: int
    """Call duration, in seconds"""
