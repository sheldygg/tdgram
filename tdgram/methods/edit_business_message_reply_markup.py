from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessMessage, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditBusinessMessageReplyMarkup(BaseMethod):
    """
    Edits the reply markup of a message sent on behalf of a business account; for bots only
    """

    __type__: Literal["editBusinessMessageReplyMarkup"] = "editBusinessMessageReplyMarkup"
    __returning_type__ = BusinessMessage

    business_connection_id: str
    """Unique identifier of business connection on behalf of which the message was sent"""
    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
