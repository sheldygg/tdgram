from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecommendedChats(BaseMethod):
    """
    Returns a list of channel chats recommended to the current user
    """

    __type__: Literal["getRecommendedChats"] = "getRecommendedChats"
    __returning_type__ = Chats
