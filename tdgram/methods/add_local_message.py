from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, InputMessageReplyTo, Message, MessageSender
from .base import BaseMethod


@dataclass(kw_only=True)
class AddLocalMessage(BaseMethod):
    """
    Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message
    """

    __type__: Literal["addLocalMessage"] = "addLocalMessage"
    __returning_type__ = Message

    chat_id: int
    """Target chat"""
    sender_id: MessageSender
    """Identifier of the sender of the message"""
    reply_to: InputMessageReplyTo | None = None
    """Information about the message or story to be replied; pass null if none"""
    disable_notification: bool
    """Pass true to disable notification for the message"""
    input_message_content: InputMessageContent
    """The content of the message to be added"""
