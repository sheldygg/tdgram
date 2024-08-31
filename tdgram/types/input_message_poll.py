from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, PollType


@dataclass(kw_only=True)
class InputMessagePoll(BaseType):
    """
    A message with a poll. Polls can't be sent to secret chats. Polls can be sent only to a private chat with a bot
    """

    __type__: Literal["inputMessagePoll"] = "inputMessagePoll"

    question: FormattedText
    """Poll question; 1-255 characters (up to 300 characters for bots). Only custom emoji entities are allowed to be added and only by Premium users"""
    options: list[FormattedText]
    """List of poll answer options, 2-10 strings 1-100 characters each. Only custom emoji entities are allowed to be added and only by Premium users"""
    is_anonymous: bool
    """True, if the poll voters are anonymous. Non-anonymous polls can't be sent or forwarded to channels"""
    type: PollType
    """Type of the poll"""
    open_period: int
    """Amount of time the poll will be active after creation, in seconds; for bots only"""
    close_date: int
    """Point in time (Unix timestamp) when the poll will automatically be closed; for bots only"""
    is_closed: bool
    """True, if the poll needs to be sent already closed; for bots only"""
