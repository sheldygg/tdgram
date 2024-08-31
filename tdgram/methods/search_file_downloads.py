from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundFileDownloads
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchFileDownloads(BaseMethod):
    """
    Searches for files in the file download list or recently downloaded files from the list
    """

    __type__: Literal["searchFileDownloads"] = "searchFileDownloads"
    __returning_type__ = FoundFileDownloads

    query: str | None = None
    """Query to search for; may be empty to return all downloaded files"""
    only_active: bool
    """Pass true to search only for active downloads, including paused"""
    only_completed: bool
    """Pass true to search only for completed downloads"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of files to be returned"""
