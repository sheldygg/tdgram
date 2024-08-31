from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessMessages, InputMessageContent, InputMessageReplyTo
from .base import BaseMethod


@dataclass(kw_only=True)
class SendBusinessMessageAlbum(BaseMethod):
    """
    Sends 2-10 messages grouped together into an album on behalf of a business account; for bots only. Currently, only audio, document, photo and video messages can be grouped into an album.
    """

    __type__: Literal["sendBusinessMessageAlbum"] = "sendBusinessMessageAlbum"
    __returning_type__ = BusinessMessages

    business_connection_id: str
    """Unique identifier of business connection on behalf of which to send the request"""
    chat_id: int
    """Target chat"""
    reply_to: InputMessageReplyTo | None = None
    """Information about the message to be replied; pass null if none"""
    disable_notification: bool
    """Pass true to disable notification for the message"""
    protect_content: bool
    """Pass true if the content of the message must be protected from forwarding and saving"""
    effect_id: int
    """Identifier of the effect to apply to the message"""
    input_message_contents: list[InputMessageContent]
    """Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media"""
