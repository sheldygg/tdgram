from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatBoostSlots
from .base import BaseMethod


@dataclass(kw_only=True)
class BoostChat(BaseMethod):
    """
    Boosts a chat and returns the list of available chat boost slots for the current user after the boost
    """

    __type__: Literal["boostChat"] = "boostChat"
    __returning_type__ = ChatBoostSlots

    chat_id: int
    """Identifier of the chat"""
    slot_ids: list[int]
    """Identifiers of boost slots of the current user from which to apply boosts to the chat"""
