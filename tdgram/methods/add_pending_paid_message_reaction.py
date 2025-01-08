from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddPendingPaidMessageReaction(BaseMethod):
    """
    Adds the paid message reaction to a message. Use getMessageAvailableReactions to check whether the reaction is available for the message
    """

    __type__: Literal["addPendingPaidMessageReaction"] = "addPendingPaidMessageReaction"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    star_count: int
    """Number of Telegram Stars to be used for the reaction. The total number of pending paid reactions must not exceed getOption('paid_reaction_star_count_max')"""
    use_default_is_anonymous: bool
    """Pass true if the user didn't choose anonymity explicitly, for example, the reaction is set from the message bubble"""
    is_anonymous: bool
    """Pass true to make paid reaction of the user on the message anonymous; pass false to make the user's profile visible among top reactors. Ignored if use_default_is_anonymous == true"""
