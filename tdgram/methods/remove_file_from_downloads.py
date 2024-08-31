from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveFileFromDownloads(BaseMethod):
    """
    Removes a file from the file download list
    """

    __type__: Literal["removeFileFromDownloads"] = "removeFileFromDownloads"
    __returning_type__ = Ok

    file_id: int
    """Identifier of the downloaded file"""
    delete_from_cache: bool
    """Pass true to delete the file from the TDLib file cache"""
