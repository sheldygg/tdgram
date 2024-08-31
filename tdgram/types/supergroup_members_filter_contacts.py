from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterContacts(BaseType):
    """
    Returns contacts of the user, which are members of the supergroup or channel
    """

    __type__: Literal["supergroupMembersFilterContacts"] = "supergroupMembersFilterContacts"

    query: str
    """Query to search for"""
