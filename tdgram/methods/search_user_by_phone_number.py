from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import User
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchUserByPhoneNumber(BaseMethod):
    """
    Searches a user by their phone number. Returns a 404 error if the user can't be found
    """

    __type__: Literal["searchUserByPhoneNumber"] = "searchUserByPhoneNumber"
    __returning_type__ = User

    phone_number: str
    """Phone number to search for"""
    only_local: bool
    """Pass true to get only locally available information without sending network requests"""
