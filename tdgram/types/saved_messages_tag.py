from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionType


@dataclass(kw_only=True)
class SavedMessagesTag(BaseType):
    """
    Represents a tag used in Saved Messages or a Saved Messages topic
    """

    __type__: Literal["savedMessagesTag"] = "savedMessagesTag"

    tag: ReactionType
    """The tag"""
    label: str
    """Label of the tag; 0-12 characters. Always empty if the tag is returned for a Saved Messages topic"""
    count: int
    """Number of times the tag was used; may be 0 if the tag has non-empty label"""
