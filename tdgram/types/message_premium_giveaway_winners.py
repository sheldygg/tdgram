from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessagePremiumGiveawayWinners(BaseType):
    """
    A Telegram Premium giveaway with public winners has been completed for the chat
    """

    __type__: Literal["messagePremiumGiveawayWinners"] = "messagePremiumGiveawayWinners"

    boosted_chat_id: int
    """Identifier of the channel chat, which was automatically boosted by the winners of the giveaway for duration of the Premium subscription"""
    giveaway_message_id: int
    """Identifier of the message with the giveaway in the boosted chat"""
    additional_chat_count: int
    """Number of other chats that participated in the giveaway"""
    actual_winners_selection_date: int
    """Point in time (Unix timestamp) when the winners were selected. May be bigger than winners selection date specified in parameters of the giveaway"""
    only_new_members: bool
    """True, if only new members of the chats were eligible for the giveaway"""
    was_refunded: bool
    """True, if the giveaway was canceled and was fully refunded"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation"""
    prize_description: str
    """Additional description of the giveaway prize"""
    winner_count: int
    """Total number of winners in the giveaway"""
    winner_user_ids: list[int]
    """Up to 100 user identifiers of the winners of the giveaway"""
    unclaimed_prize_count: int
    """Number of undistributed prizes"""
