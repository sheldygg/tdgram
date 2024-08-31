from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddPaidMessageReaction(BaseMethod):
    """
    Adds the paid message reaction to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message
    """

    __type__: Literal["addPaidMessageReaction"] = "addPaidMessageReaction"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    star_count: int
    """Number of Telegram Stars to be used for the reaction; 1-getOption('paid_reaction_star_count_max')"""
    is_anonymous: bool
    """Pass true to make paid reaction of the user on the message anonymous; pass false to make the user's profile visible among top reactors"""
