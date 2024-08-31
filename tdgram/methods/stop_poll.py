from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class StopPoll(BaseMethod):
    """
    Stops a poll
    """

    __type__: Literal["stopPoll"] = "stopPoll"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the poll belongs"""
    message_id: int
    """Identifier of the message containing the poll. Use messageProperties.can_be_edited to check whether the poll can be stopped"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none; for bots only"""
