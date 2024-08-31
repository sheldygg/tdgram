from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessMessage, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class StopBusinessPoll(BaseMethod):
    """
    Stops a poll sent on behalf of a business account; for bots only
    """

    __type__: Literal["stopBusinessPoll"] = "stopBusinessPoll"
    __returning_type__ = BusinessMessage

    business_connection_id: str
    """Unique identifier of business connection on behalf of which the message with the poll was sent"""
    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message containing the poll"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
