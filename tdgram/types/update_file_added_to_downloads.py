from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DownloadedFileCounts, FileDownload


@dataclass(kw_only=True)
class UpdateFileAddedToDownloads(BaseType):
    """
    A file was added to the file download list. This update is sent only after file download list is loaded for the first time
    """

    __type__: Literal["updateFileAddedToDownloads"] = "updateFileAddedToDownloads"

    file_download: FileDownload
    """The added file download"""
    counts: DownloadedFileCounts
    """New number of being downloaded and recently downloaded files found"""
