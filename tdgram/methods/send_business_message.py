from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessMessage, InputMessageContent, InputMessageReplyTo, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class SendBusinessMessage(BaseMethod):
    """
    Sends a message on behalf of a business account; for bots only. Returns the message after it was sent
    """

    __type__: Literal["sendBusinessMessage"] = "sendBusinessMessage"
    __returning_type__ = BusinessMessage

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
    reply_markup: ReplyMarkup | None = None
    """Markup for replying to the message; pass null if none"""
    input_message_content: InputMessageContent
    """The content of the message to be sent"""
