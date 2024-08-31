from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAvailableReactions


@dataclass(kw_only=True)
class ChatEventAvailableReactionsChanged(BaseType):
    """
    The chat available reactions were changed
    """

    __type__: Literal["chatEventAvailableReactionsChanged"] = "chatEventAvailableReactionsChanged"

    old_available_reactions: ChatAvailableReactions
    """Previous chat available reactions"""
    new_available_reactions: ChatAvailableReactions
    """New chat available reactions"""
