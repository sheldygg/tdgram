from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, Ok, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditInlineMessageText(BaseMethod):
    """
    Edits the text of an inline text or game message sent via a bot; for bots only
    """

    __type__: Literal["editInlineMessageText"] = "editInlineMessageText"
    __returning_type__ = Ok

    inline_message_id: str
    """Inline message identifier"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
    input_message_content: InputMessageContent
    """New text content of the message. Must be of type inputMessageText"""
