from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicIcon, MessageSender


@dataclass(kw_only=True)
class ForumTopicInfo(BaseType):
    """
    Contains basic information about a forum topic
    """

    __type__: Literal["forumTopicInfo"] = "forumTopicInfo"

    message_thread_id: int
    """Message thread identifier of the topic"""
    name: str
    """Name of the topic"""
    icon: ForumTopicIcon
    """Icon of the topic"""
    creation_date: int
    """Point in time (Unix timestamp) when the topic was created"""
    creator_id: MessageSender
    """Identifier of the creator of the topic"""
    is_general: bool
    """True, if the topic is the General topic list"""
    is_outgoing: bool
    """True, if the topic was created by the current user"""
    is_closed: bool
    """True, if the topic is closed"""
    is_hidden: bool
    """True, if the topic is hidden above the topic list and closed; for General topic only"""
