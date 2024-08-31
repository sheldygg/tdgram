from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterRestricted(BaseType):
    """
    Returns restricted supergroup members; can be used only by administrators
    """

    __type__: Literal["supergroupMembersFilterRestricted"] = "supergroupMembersFilterRestricted"

    query: str
    """Query to search for"""
