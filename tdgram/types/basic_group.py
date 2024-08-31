from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMemberStatus


@dataclass(kw_only=True)
class BasicGroup(BaseType):
    """
    Represents a basic group of 0-200 users (must be upgraded to a supergroup to accommodate more than 200 users)
    """

    __type__: Literal["basicGroup"] = "basicGroup"

    id: int
    """Group identifier"""
    member_count: int
    """Number of members in the group"""
    status: ChatMemberStatus
    """Status of the current user in the group"""
    is_active: bool
    """True, if the group is active"""
    upgraded_to_supergroup_id: int
    """Identifier of the supergroup to which this group was upgraded; 0 if none"""
