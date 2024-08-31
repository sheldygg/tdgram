from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import UserFullInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserFullInfo(BaseMethod):
    """
    Returns full information about a user by their identifier
    """

    __type__: Literal["getUserFullInfo"] = "getUserFullInfo"
    __returning_type__ = UserFullInfo

    user_id: int
    """User identifier"""
