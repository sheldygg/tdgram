from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventVideoChatEnded(BaseType):
    """
    A video chat was ended
    """

    __type__: Literal["chatEventVideoChatEnded"] = "chatEventVideoChatEnded"

    group_call_id: int
    """Identifier of the video chat. The video chat can be received through the method getGroupCall"""
