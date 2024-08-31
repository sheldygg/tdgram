from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventVideoChatCreated(BaseType):
    """
    A video chat was created
    """

    __type__: Literal["chatEventVideoChatCreated"] = "chatEventVideoChatCreated"

    group_call_id: int
    """Identifier of the video chat. The video chat can be received through the method getGroupCall"""
