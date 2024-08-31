from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileDownloadedPrefixSize(BaseType):
    """
    Contains size of downloaded prefix of a file
    """

    __type__: Literal["fileDownloadedPrefixSize"] = "fileDownloadedPrefixSize"

    size: int
    """The prefix size, in bytes"""
