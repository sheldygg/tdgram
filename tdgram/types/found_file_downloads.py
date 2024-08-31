from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DownloadedFileCounts, FileDownload


@dataclass(kw_only=True)
class FoundFileDownloads(BaseType):
    """
    Contains a list of downloaded files, found by a search
    """

    __type__: Literal["foundFileDownloads"] = "foundFileDownloads"

    total_counts: DownloadedFileCounts
    """Total number of suitable files, ignoring offset"""
    files: list[FileDownload]
    """The list of files"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""
