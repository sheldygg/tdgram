from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FailedToAddMember


@dataclass(kw_only=True)
class FailedToAddMembers(BaseType):
    """
    Represents a list of users that has failed to be added to a chat
    """

    __type__: Literal["failedToAddMembers"] = "failedToAddMembers"

    failed_to_add_members: list[FailedToAddMember]
    """Information about users that weren't added to the chat"""
