from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UserStatus


@dataclass(kw_only=True)
class UpdateUserStatus(BaseType):
    """
    The user went online or offline
    """

    __type__: Literal["updateUserStatus"] = "updateUserStatus"

    user_id: int
    """User identifier"""
    status: UserStatus
    """New status of the user"""
