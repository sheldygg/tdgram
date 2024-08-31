from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FilePart
from .base import BaseMethod


@dataclass(kw_only=True)
class ReadFilePart(BaseMethod):
    """
    Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file
    """

    __type__: Literal["readFilePart"] = "readFilePart"
    __returning_type__ = FilePart

    file_id: int
    """Identifier of the file. The file must be located in the TDLib file cache"""
    offset: int
    """The offset from which to read the file"""
    count: int
    """Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position"""
