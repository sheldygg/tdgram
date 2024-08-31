from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageVideoChatStarted(BaseType):
    """
    A newly created video chat
    """

    __type__: Literal["messageVideoChatStarted"] = "messageVideoChatStarted"

    group_call_id: int
    """Identifier of the video chat. The video chat can be received through the method getGroupCall"""
