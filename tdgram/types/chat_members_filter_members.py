from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMembersFilterMembers(BaseType):
    """
    Returns all chat members, including restricted chat members
    """

    __type__: Literal["chatMembersFilterMembers"] = "chatMembersFilterMembers"
