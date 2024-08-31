from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessMessage, InputMessageContent, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditBusinessMessageText(BaseMethod):
    """
    Edits the text of a text or game message sent on behalf of a business account; for bots only
    """

    __type__: Literal["editBusinessMessageText"] = "editBusinessMessageText"
    __returning_type__ = BusinessMessage

    business_connection_id: str
    """Unique identifier of business connection on behalf of which the message was sent"""
    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
    input_message_content: InputMessageContent
    """New text content of the message. Must be of type inputMessageText"""
