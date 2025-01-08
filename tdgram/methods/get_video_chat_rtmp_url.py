from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import RtmpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetVideoChatRtmpUrl(BaseMethod):
    """
    Returns RTMP URL for streaming to the chat; requires can_manage_video_chats administrator right
    """

    __type__: Literal["getVideoChatRtmpUrl"] = "getVideoChatRtmpUrl"
    __returning_type__ = RtmpUrl

    chat_id: int
    """Chat identifier"""
