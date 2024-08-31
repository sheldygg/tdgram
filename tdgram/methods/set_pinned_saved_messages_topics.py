from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPinnedSavedMessagesTopics(BaseMethod):
    """
    Changes the order of pinned Saved Messages topics
    """

    __type__: Literal["setPinnedSavedMessagesTopics"] = "setPinnedSavedMessagesTopics"
    __returning_type__ = Ok

    saved_messages_topic_ids: list[int]
    """Identifiers of the new pinned Saved Messages topics"""
