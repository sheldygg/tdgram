from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PublicForwards
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStoryPublicForwards(BaseMethod):
    """
    Returns forwards of a story as a message to public chats and reposts by public channels. Can be used only if the story is posted on behalf of the current user or story.can_get_statistics == true.
    """

    __type__: Literal["getStoryPublicForwards"] = "getStoryPublicForwards"
    __returning_type__ = PublicForwards

    story_sender_chat_id: int
    """The identifier of the sender of the story"""
    story_id: int
    """The identifier of the story"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of messages and stories to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit"""
