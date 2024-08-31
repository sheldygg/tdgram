from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UserFullInfo


@dataclass(kw_only=True)
class UpdateUserFullInfo(BaseType):
    """
    Some data in userFullInfo has been changed
    """

    __type__: Literal["updateUserFullInfo"] = "updateUserFullInfo"

    user_id: int
    """User identifier"""
    user_full_info: UserFullInfo
    """New full information about the user"""
