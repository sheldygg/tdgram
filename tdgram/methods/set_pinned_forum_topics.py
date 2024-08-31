from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPinnedForumTopics(BaseMethod):
    """
    Changes the order of pinned forum topics; requires can_manage_topics right in the supergroup
    """

    __type__: Literal["setPinnedForumTopics"] = "setPinnedForumTopics"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_thread_ids: list[int]
    """The new list of pinned forum topics"""
