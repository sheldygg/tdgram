from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class UpdatePollAnswer(BaseType):
    """
    A user changed the answer to a poll; for bots only
    """

    __type__: Literal["updatePollAnswer"] = "updatePollAnswer"

    poll_id: int
    """Unique poll identifier"""
    voter_id: MessageSender
    """Identifier of the message sender that changed the answer to the poll"""
    option_ids: list[int]
    """0-based identifiers of answer options, chosen by the user"""
