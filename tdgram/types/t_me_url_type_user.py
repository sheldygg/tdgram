from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TMeUrlTypeUser(BaseType):
    """
    A URL linking to a user
    """

    __type__: Literal["tMeUrlTypeUser"] = "tMeUrlTypeUser"

    user_id: int
    """Identifier of the user"""
