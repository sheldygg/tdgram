from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBoostSource


@dataclass(kw_only=True)
class ChatBoost(BaseType):
    """
    Describes a boost applied to a chat
    """

    __type__: Literal["chatBoost"] = "chatBoost"

    id: str
    """Unique identifier of the boost"""
    count: int
    """The number of identical boosts applied"""
    source: ChatBoostSource
    """Source of the boost"""
    start_date: int
    """Point in time (Unix timestamp) when the chat was boosted"""
    expiration_date: int
    """Point in time (Unix timestamp) when the boost will expire"""
