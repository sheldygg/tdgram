from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatDeleteMember(BaseType):
    """
    A chat member was deleted
    """

    __type__: Literal["pushMessageContentChatDeleteMember"] = "pushMessageContentChatDeleteMember"

    member_name: str
    """Name of the deleted member"""
    is_current_user: bool
    """True, if the current user was deleted from the group"""
    is_left: bool
    """True, if the user has left the group themselves"""
