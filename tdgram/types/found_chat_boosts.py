from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBoost


@dataclass(kw_only=True)
class FoundChatBoosts(BaseType):
    """
    Contains a list of boosts applied to a chat
    """

    __type__: Literal["foundChatBoosts"] = "foundChatBoosts"

    total_count: int
    """Total number of boosts applied to the chat"""
    boosts: list[ChatBoost]
    """List of boosts"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""
