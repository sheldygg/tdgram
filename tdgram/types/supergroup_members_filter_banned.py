from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterBanned(BaseType):
    """
    Returns users banned from the supergroup or channel; can be used only by administrators
    """

    __type__: Literal["supergroupMembersFilterBanned"] = "supergroupMembersFilterBanned"

    query: str
    """Query to search for"""
