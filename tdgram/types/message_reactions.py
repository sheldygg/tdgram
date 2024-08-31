from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageReaction, PaidReactor


@dataclass(kw_only=True)
class MessageReactions(BaseType):
    """
    Contains a list of reactions added to a message
    """

    __type__: Literal["messageReactions"] = "messageReactions"

    reactions: list[MessageReaction]
    """List of added reactions"""
    are_tags: bool
    """True, if the reactions are tags and Telegram Premium users can filter messages by them"""
    paid_reactors: list[PaidReactor]
    """Information about top users that added the paid reaction"""
    can_get_added_reactions: bool
    """True, if the list of added reactions is available using getMessageAddedReactions"""
