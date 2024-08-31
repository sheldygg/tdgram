from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, InputMessageReplyTo, Messages, MessageSendOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class SendMessageAlbum(BaseMethod):
    """
    Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album.
    """

    __type__: Literal["sendMessageAlbum"] = "sendMessageAlbum"
    __returning_type__ = Messages

    chat_id: int
    """Target chat"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the messages will be sent"""
    reply_to: InputMessageReplyTo | None = None
    """Information about the message or story to be replied; pass null if none"""
    options: MessageSendOptions | None = None
    """Options to be used to send the messages; pass null to use default options"""
    input_message_contents: list[InputMessageContent]
    """Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media"""
