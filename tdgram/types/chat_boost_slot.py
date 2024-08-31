from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatBoostSlot(BaseType):
    """
    Describes a slot for chat boost
    """

    __type__: Literal["chatBoostSlot"] = "chatBoostSlot"

    slot_id: int
    """Unique identifier of the slot"""
    currently_boosted_chat_id: int
    """Identifier of the currently boosted chat; 0 if none"""
    start_date: int
    """Point in time (Unix timestamp) when the chat was boosted; 0 if none"""
    expiration_date: int
    """Point in time (Unix timestamp) when the boost will expire"""
    cooldown_until_date: int
    """Point in time (Unix timestamp) after which the boost can be used for another chat"""
