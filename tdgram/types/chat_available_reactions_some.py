from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionType


@dataclass(kw_only=True)
class ChatAvailableReactionsSome(BaseType):
    """
    Only specific reactions are available in the chat
    """

    __type__: Literal["chatAvailableReactionsSome"] = "chatAvailableReactionsSome"

    reactions: list[ReactionType]
    """The list of reactions"""
    max_reaction_count: int
    """The maximum allowed number of reactions per message; 1-11"""
