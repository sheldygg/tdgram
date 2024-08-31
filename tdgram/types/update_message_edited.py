from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReplyMarkup


@dataclass(kw_only=True)
class UpdateMessageEdited(BaseType):
    """
    A message was edited. Changes in the message content will come in a separate updateMessageContent
    """

    __type__: Literal["updateMessageEdited"] = "updateMessageEdited"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    edit_date: int
    """Point in time (Unix timestamp) when the message was edited"""
    reply_markup: ReplyMarkup | None = None
    """New message reply markup; may be null"""
