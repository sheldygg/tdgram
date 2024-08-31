from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecentlyOpenedChats(BaseMethod):
    """
    Returns recently opened chats; this is an offline request. Returns chats in the order of last opening
    """

    __type__: Literal["getRecentlyOpenedChats"] = "getRecentlyOpenedChats"
    __returning_type__ = Chats

    limit: int
    """The maximum number of chats to be returned"""
