from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import UserSupportInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserSupportInfo(BaseMethod):
    """
    Returns support information for the given user; for Telegram support only
    """

    __type__: Literal["getUserSupportInfo"] = "getUserSupportInfo"
    __returning_type__ = UserSupportInfo

    user_id: int
    """User identifier"""
