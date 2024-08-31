from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetCloseFriends(BaseMethod):
    """
    Changes the list of close friends of the current user
    """

    __type__: Literal["setCloseFriends"] = "setCloseFriends"
    __returning_type__ = Ok

    user_ids: list[int]
    """User identifiers of close friends; the users must be contacts of the current user"""
