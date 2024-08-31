from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import User
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchUserByToken(BaseMethod):
    """
    Searches a user by a token from the user's link
    """

    __type__: Literal["searchUserByToken"] = "searchUserByToken"
    __returning_type__ = User

    token: str
    """Token to search for"""
