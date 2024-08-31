from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SavedMessagesTopicTypeMyNotes(BaseType):
    """
    Topic containing messages sent by the current user of forwarded from an unknown chat
    """

    __type__: Literal["savedMessagesTopicTypeMyNotes"] = "savedMessagesTopicTypeMyNotes"
