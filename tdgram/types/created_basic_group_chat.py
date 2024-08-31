from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FailedToAddMembers


@dataclass(kw_only=True)
class CreatedBasicGroupChat(BaseType):
    """
    Contains information about a newly created basic group chat
    """

    __type__: Literal["createdBasicGroupChat"] = "createdBasicGroupChat"

    chat_id: int
    """Chat identifier"""
    failed_to_add_members: FailedToAddMembers
    """Information about failed to add members"""
