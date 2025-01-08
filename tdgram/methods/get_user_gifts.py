from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import UserGifts
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserGifts(BaseMethod):
    """
    Returns gifts saved to profile by the given user
    """

    __type__: Literal["getUserGifts"] = "getUserGifts"
    __returning_type__ = UserGifts

    user_id: int
    """Identifier of the user"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of gifts to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit"""
