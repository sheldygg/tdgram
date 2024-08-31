from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import RtmpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class ReplaceVideoChatRtmpUrl(BaseMethod):
    """
    Replaces the current RTMP URL for streaming to the chat; requires owner privileges
    """

    __type__: Literal["replaceVideoChatRtmpUrl"] = "replaceVideoChatRtmpUrl"
    __returning_type__ = RtmpUrl

    chat_id: int
    """Chat identifier"""
