from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DraftMessage, Message, SavedMessagesTopicType


@dataclass(kw_only=True)
class SavedMessagesTopic(BaseType):
    """
    Contains information about a Saved Messages topic
    """

    __type__: Literal["savedMessagesTopic"] = "savedMessagesTopic"

    id: int
    """Unique topic identifier"""
    type: SavedMessagesTopicType
    """Type of the topic"""
    is_pinned: bool
    """True, if the topic is pinned"""
    order: int
    """A parameter used to determine order of the topic in the topic list. Topics must be sorted by the order in descending order"""
    last_message: Message | None = None
    """Last message in the topic; may be null if none or unknown"""
    draft_message: DraftMessage | None = None
    """A draft of a message in the topic; may be null if none"""
