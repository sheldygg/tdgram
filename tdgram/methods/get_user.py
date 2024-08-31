from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import User
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUser(BaseMethod):
    """
    Returns information about a user by their identifier. This is an offline request if the current user is not a bot
    """

    __type__: Literal["getUser"] = "getUser"
    __returning_type__ = User

    user_id: int
    """User identifier"""
