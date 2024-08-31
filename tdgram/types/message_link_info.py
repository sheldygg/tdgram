from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class MessageLinkInfo(BaseType):
    """
    Contains information about a link to a message or a forum topic in a chat
    """

    __type__: Literal["messageLinkInfo"] = "messageLinkInfo"

    is_public: bool
    """True, if the link is a public link for a message or a forum topic in a chat"""
    chat_id: int
    """If found, identifier of the chat to which the link points, 0 otherwise"""
    message_thread_id: int
    """If found, identifier of the message thread in which to open the message, or a forum topic to open if the message is missing"""
    message: Message | None = None
    """If found, the linked message; may be null"""
    media_timestamp: int
    """Timestamp from which the video/audio/video note/voice note/story playing must start, in seconds; 0 if not specified. The media can be in the message content or in its link preview"""
    for_album: bool
    """True, if the whole media album to which the message belongs is linked"""
