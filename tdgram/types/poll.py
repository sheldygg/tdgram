from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, MessageSender, PollOption, PollType


@dataclass(kw_only=True)
class Poll(BaseType):
    """
    Describes a poll
    """

    __type__: Literal["poll"] = "poll"

    id: int
    """Unique poll identifier"""
    question: FormattedText
    """Poll question; 1-300 characters. Only custom emoji entities are allowed"""
    options: list[PollOption]
    """List of poll answer options"""
    total_voter_count: int
    """Total number of voters, participating in the poll"""
    recent_voter_ids: list[MessageSender]
    """Identifiers of recent voters, if the poll is non-anonymous"""
    is_anonymous: bool
    """True, if the poll is anonymous"""
    type: PollType
    """Type of the poll"""
    open_period: int
    """Amount of time the poll will be active after creation, in seconds"""
    close_date: int
    """Point in time (Unix timestamp) when the poll will automatically be closed"""
    is_closed: bool
    """True, if the poll is closed"""
