from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundPositions
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchStringsByPrefix(BaseMethod):
    """
    Searches specified query by word prefixes in the provided strings. Returns 0-based positions of strings that matched. Can be called synchronously
    """

    __type__: Literal["searchStringsByPrefix"] = "searchStringsByPrefix"
    __returning_type__ = FoundPositions

    strings: list[str]
    """The strings to search in for the query"""
    query: str
    """Query to search for"""
    limit: int
    """The maximum number of objects to return"""
    return_none_for_empty_query: bool
    """Pass true to receive no results for an empty query"""
