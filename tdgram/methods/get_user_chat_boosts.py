from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundChatBoosts
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserChatBoosts(BaseMethod):
    """
    Returns the list of boosts applied to a chat by a given user; requires administrator rights in the chat; for bots only
    """

    __type__: Literal["getUserChatBoosts"] = "getUserChatBoosts"
    __returning_type__ = FoundChatBoosts

    chat_id: int
    """Identifier of the chat"""
    user_id: int
    """Identifier of the user"""
