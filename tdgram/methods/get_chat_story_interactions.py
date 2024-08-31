from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ReactionType, StoryInteractions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatStoryInteractions(BaseMethod):
    """
    Returns interactions with a story posted in a chat. Can be used only if story is posted on behalf of a chat and the user is an administrator in the chat
    """

    __type__: Literal["getChatStoryInteractions"] = "getChatStoryInteractions"
    __returning_type__ = StoryInteractions

    story_sender_chat_id: int
    """The identifier of the sender of the story"""
    story_id: int
    """Story identifier"""
    reaction_type: ReactionType | None = None
    """Pass the default heart reaction or a suggested reaction type to receive only interactions with the specified reaction type; pass null to receive all interactions; reactionTypePaid isn't supported"""
    prefer_forwards: bool
    """Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of story interactions to return"""
