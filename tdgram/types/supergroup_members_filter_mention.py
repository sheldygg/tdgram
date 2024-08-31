from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterMention(BaseType):
    """
    Returns users which can be mentioned in the supergroup
    """

    __type__: Literal["supergroupMembersFilterMention"] = "supergroupMembersFilterMention"

    query: str
    """Query to search for"""
    message_thread_id: int
    """If non-zero, the identifier of the current message thread"""
