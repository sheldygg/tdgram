from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageLink
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageLink(BaseMethod):
    """
    Returns an HTTPS link to a message in a chat. Available only if messageProperties.can_get_link, or if messageProperties.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request
    """

    __type__: Literal["getMessageLink"] = "getMessageLink"
    __returning_type__ = MessageLink

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    media_timestamp: int
    """If not 0, timestamp from which the video/audio/video note/voice note/story playing must start, in seconds. The media can be in the message content or in its link preview"""
    for_album: bool
    """Pass true to create a link for the whole media album"""
    in_message_thread: bool
    """Pass true to create a link to the message as a channel post comment, in a message thread, or a forum topic"""
