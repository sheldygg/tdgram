from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundMessages
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchCallMessages(BaseMethod):
    """
    Searches for call messages. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib
    """

    __type__: Literal["searchCallMessages"] = "searchCallMessages"
    __returning_type__ = FoundMessages

    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit"""
    only_missed: bool
    """Pass true to search only for messages with missed/declined calls"""
