from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DownloadedFileCounts(BaseType):
    """
    Contains number of being downloaded and recently downloaded files found
    """

    __type__: Literal["downloadedFileCounts"] = "downloadedFileCounts"

    active_count: int
    """Number of active file downloads found, including paused"""
    paused_count: int
    """Number of paused file downloads found"""
    completed_count: int
    """Number of completed file downloads found"""
