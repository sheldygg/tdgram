from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GiveawayParameters(BaseType):
    """
    Describes parameters of a giveaway
    """

    __type__: Literal["giveawayParameters"] = "giveawayParameters"

    boosted_chat_id: int
    """Identifier of the supergroup or channel chat, which will be automatically boosted by the winners of the giveaway for duration of the Telegram Premium subscription,"""
    additional_chat_ids: list[int]
    """Identifiers of other supergroup or channel chats that must be subscribed by the users to be eligible for the giveaway. There can be up to getOption('giveaway_additional_chat_count_max') additional chats"""
    winners_selection_date: int
    """Point in time (Unix timestamp) when the giveaway is expected to be performed; must be 60-getOption('giveaway_duration_max') seconds in the future in scheduled giveaways"""
    only_new_members: bool
    """True, if only new members of the chats will be eligible for the giveaway"""
    has_public_winners: bool
    """True, if the list of winners of the giveaway will be available to everyone"""
    country_codes: list[str]
    """The list of two-letter ISO 3166-1 alpha-2 codes of countries, users from which will be eligible for the giveaway. If empty, then all users can participate in the giveaway."""
    prize_description: str
    """Additional description of the giveaway prize; 0-128 characters"""
