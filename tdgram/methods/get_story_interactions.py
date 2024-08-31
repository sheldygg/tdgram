from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StoryInteractions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStoryInteractions(BaseMethod):
    """
    Returns interactions with a story. The method can be called only for stories posted on behalf of the current user
    """

    __type__: Literal["getStoryInteractions"] = "getStoryInteractions"
    __returning_type__ = StoryInteractions

    story_id: int
    """Story identifier"""
    query: str | None = None
    """Query to search for in names, usernames and titles; may be empty to get all relevant interactions"""
    only_contacts: bool
    """Pass true to get only interactions by contacts; pass false to get all relevant interactions"""
    prefer_forwards: bool
    """Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date"""
    prefer_with_reaction: bool
    """Pass true to get interactions with reaction first; pass false to get interactions sorted just by interaction date. Ignored if prefer_forwards == true"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of story interactions to return"""
