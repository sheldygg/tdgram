from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GiveawayPrize


@dataclass(kw_only=True)
class MessageGiveawayWinners(BaseType):
    """
    A giveaway with public winners has been completed for the chat
    """

    __type__: Literal["messageGiveawayWinners"] = "messageGiveawayWinners"

    boosted_chat_id: int
    """Identifier of the supergroup or channel chat, which was automatically boosted by the winners of the giveaway"""
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
    prize: GiveawayPrize
    """Prize of the giveaway"""
    prize_description: str
    """Additional description of the giveaway prize"""
    winner_count: int
    """Total number of winners in the giveaway"""
    winner_user_ids: list[int]
    """Up to 100 user identifiers of the winners of the giveaway"""
    unclaimed_prize_count: int
    """Number of undistributed prizes; for Telegram Premium giveaways only"""
