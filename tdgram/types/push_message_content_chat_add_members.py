from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatAddMembers(BaseType):
    """
    New chat members were invited to a group
    """

    __type__: Literal["pushMessageContentChatAddMembers"] = "pushMessageContentChatAddMembers"

    member_name: str
    """Name of the added member"""
    is_current_user: bool
    """True, if the current user was added to the group"""
    is_returned: bool
    """True, if the user has returned to the group themselves"""
