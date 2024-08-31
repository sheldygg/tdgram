from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import (
    InputMessageContent,
    InputMessageReplyTo,
    Message,
    MessageSendOptions,
    ReplyMarkup,
)
from .base import BaseMethod


@dataclass(kw_only=True)
class SendMessage(BaseMethod):
    """
    Sends a message. Returns the sent message
    """

    __type__: Literal["sendMessage"] = "sendMessage"
    __returning_type__ = Message

    chat_id: int
    """Target chat"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the message will be sent"""
    reply_to: InputMessageReplyTo | None = None
    """Information about the message or story to be replied; pass null if none"""
    options: MessageSendOptions | None = None
    """Options to be used to send the message; pass null to use default options"""
    reply_markup: ReplyMarkup | None = None
    """Markup for replying to the message; pass null if none; for bots only"""
    input_message_content: InputMessageContent
    """The content of the message to be sent"""
