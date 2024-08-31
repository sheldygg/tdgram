from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GroupCallId
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateVideoChat(BaseMethod):
    """
    Creates a video chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_video_chats administrator right
    """

    __type__: Literal["createVideoChat"] = "createVideoChat"
    __returning_type__ = GroupCallId

    chat_id: int
    """Identifier of a chat in which the video chat will be created"""
    title: str
    """Group call title; if empty, chat title will be used"""
    start_date: int
    """Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 to start the video chat immediately. The date must be at least 10 seconds and at most 8 days in the future"""
    is_rtmp_stream: bool
    """Pass true to create an RTMP stream instead of an ordinary video chat; requires owner privileges"""
