from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPollAnswer(BaseMethod):
    """
    Changes the user answer to a poll. A poll in quiz mode can be answered only once
    """

    __type__: Literal["setPollAnswer"] = "setPollAnswer"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the poll belongs"""
    message_id: int
    """Identifier of the message containing the poll"""
    option_ids: list[int]
    """0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers"""
