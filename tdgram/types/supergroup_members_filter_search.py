from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterSearch(BaseType):
    """
    Used to search for supergroup or channel members via a (string) query
    """

    __type__: Literal["supergroupMembersFilterSearch"] = "supergroupMembersFilterSearch"

    query: str
    """Query to search for"""
