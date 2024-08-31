from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DownloadedFileCounts


@dataclass(kw_only=True)
class UpdateFileRemovedFromDownloads(BaseType):
    """
    A file was removed from the file download list. This update is sent only after file download list is loaded for the first time
    """

    __type__: Literal["updateFileRemovedFromDownloads"] = "updateFileRemovedFromDownloads"

    file_id: int
    """File identifier"""
    counts: DownloadedFileCounts
    """New number of being downloaded and recently downloaded files found"""
