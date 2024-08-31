from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundStories
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchPublicStoriesByVenue(BaseMethod):
    """
    Searches for public stories from the given venue. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    """

    __type__: Literal["searchPublicStoriesByVenue"] = "searchPublicStoriesByVenue"
    __returning_type__ = FoundStories

    venue_provider: str
    """Provider of the venue"""
    venue_id: str
    """Identifier of the venue in the provider database"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit"""
