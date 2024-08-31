from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterRecent(BaseType):
    """
    Returns recently active users in reverse chronological order
    """

    __type__: Literal["supergroupMembersFilterRecent"] = "supergroupMembersFilterRecent"
