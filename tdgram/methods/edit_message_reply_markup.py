from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditMessageReplyMarkup(BaseMethod):
    """
    Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side
    """

    __type__: Literal["editMessageReplyMarkup"] = "editMessageReplyMarkup"
    __returning_type__ = Message

    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
