from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, Message, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditMessageText(BaseMethod):
    """
    Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side
    """

    __type__: Literal["editMessageText"] = "editMessageText"
    __returning_type__ = Message

    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none; for bots only"""
    input_message_content: InputMessageContent
    """New text content of the message. Must be of type inputMessageText"""
