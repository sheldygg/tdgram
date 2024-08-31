from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSenders
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPollVoters(BaseMethod):
    """
    Returns message senders voted for the specified option in a non-anonymous polls. For optimal performance, the number of returned users is chosen by TDLib
    """

    __type__: Literal["getPollVoters"] = "getPollVoters"
    __returning_type__ = MessageSenders

    chat_id: int
    """Identifier of the chat to which the poll belongs"""
    message_id: int
    """Identifier of the message containing the poll"""
    option_id: int
    """0-based identifier of the answer option"""
    offset: int
    """Number of voters to skip in the result; must be non-negative"""
    limit: int
    """The maximum number of voters to be returned; must be positive and can't be greater than 50. For optimal performance, the number of returned voters is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached"""
