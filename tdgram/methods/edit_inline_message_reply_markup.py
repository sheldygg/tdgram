from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditInlineMessageReplyMarkup(BaseMethod):
    """
    Edits the reply markup of an inline message sent via a bot; for bots only
    """

    __type__: Literal["editInlineMessageReplyMarkup"] = "editInlineMessageReplyMarkup"
    __returning_type__ = Ok

    inline_message_id: str
    """Inline message identifier"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
