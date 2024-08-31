from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateSavedMessagesTopicCount(BaseType):
    """
    Number of Saved Messages topics has changed
    """

    __type__: Literal["updateSavedMessagesTopicCount"] = "updateSavedMessagesTopicCount"

    topic_count: int
    """Approximate total number of Saved Messages topics"""
