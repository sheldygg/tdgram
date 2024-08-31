from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DownloadedFileCounts


@dataclass(kw_only=True)
class UpdateFileDownload(BaseType):
    """
    A file download was changed. This update is sent only after file download list is loaded for the first time
    """

    __type__: Literal["updateFileDownload"] = "updateFileDownload"

    file_id: int
    """File identifier"""
    complete_date: int
    """Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed"""
    is_paused: bool
    """True, if downloading of the file is paused"""
    counts: DownloadedFileCounts
    """New number of being downloaded and recently downloaded files found"""
