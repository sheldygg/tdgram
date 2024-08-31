from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundChatBoosts
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatBoosts(BaseMethod):
    """
    Returns the list of boosts applied to a chat; requires administrator rights in the chat
    """

    __type__: Literal["getChatBoosts"] = "getChatBoosts"
    __returning_type__ = FoundChatBoosts

    chat_id: int
    """Identifier of the chat"""
    only_gift_codes: bool
    """Pass true to receive only boosts received from gift codes and giveaways created by the chat"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of boosts to be returned; up to 100. For optimal performance, the number of returned boosts can be smaller than the specified limit"""
