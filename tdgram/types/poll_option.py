from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class PollOption(BaseType):
    """
    Describes one answer option of a poll
    """

    __type__: Literal["pollOption"] = "pollOption"

    text: FormattedText
    """Option text; 1-100 characters. Only custom emoji entities are allowed"""
    voter_count: int
    """Number of voters for this option, available only for closed or voted polls"""
    vote_percentage: int
    """The percentage of votes for this option; 0-100"""
    is_chosen: bool
    """True, if the option was chosen by the user"""
    is_being_chosen: bool
    """True, if the option is being chosen by a pending setPollAnswer request"""
