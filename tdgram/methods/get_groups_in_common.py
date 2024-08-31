from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGroupsInCommon(BaseMethod):
    """
    Returns a list of common group chats with a given user. Chats are sorted by their type and creation date
    """

    __type__: Literal["getGroupsInCommon"] = "getGroupsInCommon"
    __returning_type__ = Chats

    user_id: int
    """User identifier"""
    offset_chat_id: int
    """Chat identifier starting from which to return chats; use 0 for the first request"""
    limit: int
    """The maximum number of chats to be returned; up to 100"""
