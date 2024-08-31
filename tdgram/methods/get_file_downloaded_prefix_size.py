from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FileDownloadedPrefixSize
from .base import BaseMethod


@dataclass(kw_only=True)
class GetFileDownloadedPrefixSize(BaseMethod):
    """
    Returns file downloaded prefix size from a given offset, in bytes
    """

    __type__: Literal["getFileDownloadedPrefixSize"] = "getFileDownloadedPrefixSize"
    __returning_type__ = FileDownloadedPrefixSize

    file_id: int
    """Identifier of the file"""
    offset: int
    """Offset from which downloaded prefix size needs to be calculated"""
