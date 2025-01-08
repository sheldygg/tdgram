from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageVideoChatScheduled(BaseType):
    """
    A new video chat was scheduled
    """

    __type__: Literal["messageVideoChatScheduled"] = "messageVideoChatScheduled"

    group_call_id: int
    """Identifier of the video chat. The video chat can be received through the method getGroupCall"""
    start_date: int
    """Point in time (Unix timestamp) when the group call is expected to be started by an administrator"""
