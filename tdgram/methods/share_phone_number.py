from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SharePhoneNumber(BaseMethod):
    """
    Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber
    """

    __type__: Literal["sharePhoneNumber"] = "sharePhoneNumber"
    __returning_type__ = Ok

    user_id: int
    """Identifier of the user with whom to share the phone number. The user must be a mutual contact"""
