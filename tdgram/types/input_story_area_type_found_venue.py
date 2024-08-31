from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputStoryAreaTypeFoundVenue(BaseType):
    """
    An area pointing to a venue found by the bot getOption('venue_search_bot_username')
    """

    __type__: Literal["inputStoryAreaTypeFoundVenue"] = "inputStoryAreaTypeFoundVenue"

    query_id: int
    """Identifier of the inline query, used to found the venue"""
    result_id: str
    """Identifier of the inline query result"""
