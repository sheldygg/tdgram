from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Users
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCloseFriends(BaseMethod):
    """
    Returns all close friends of the current user
    """

    __type__: Literal["getCloseFriends"] = "getCloseFriends"
    __returning_type__ = Users
