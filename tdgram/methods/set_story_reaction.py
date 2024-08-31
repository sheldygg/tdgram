from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class SetStoryReaction(BaseMethod):
    """
    Changes chosen reaction on a story that has already been sent
    """

    __type__: Literal["setStoryReaction"] = "setStoryReaction"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """The identifier of the sender of the story"""
    story_id: int
    """The identifier of the story"""
    reaction_type: ReactionType | None = None
    """Type of the reaction to set; pass null to remove the reaction. Custom emoji reactions can be used only by Telegram Premium users. Paid reactions can't be set"""
    update_recent_reactions: bool
    """Pass true if the reaction needs to be added to recent reactions"""
