from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateFileDownloads(BaseType):
    """
    The state of the file download list has changed
    """

    __type__: Literal["updateFileDownloads"] = "updateFileDownloads"

    total_size: int
    """Total size of files in the file download list, in bytes"""
    total_count: int
    """Total number of files in the file download list"""
    downloaded_size: int
    """Total downloaded size of files in the file download list, in bytes"""
