from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveAllFilesFromDownloads(BaseMethod):
    """
    Removes all files from the file download list
    """

    __type__: Literal["removeAllFilesFromDownloads"] = "removeAllFilesFromDownloads"
    __returning_type__ = Ok

    only_active: bool
    """Pass true to remove only active downloads, including paused"""
    only_completed: bool
    """Pass true to remove only completed downloads"""
    delete_from_cache: bool
    """Pass true to delete the file from the TDLib file cache"""
