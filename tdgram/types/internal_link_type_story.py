from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeStory(BaseType):
    """
    The link is a link to a story. Call searchPublicChat with the given sender username, then call getStory with the received chat identifier and the given story identifier, then show the story if received
    """

    __type__: Literal["internalLinkTypeStory"] = "internalLinkTypeStory"

    story_sender_username: str
    """Username of the sender of the story"""
    story_id: int
    """Story identifier"""
