from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LocalFile, RemoteFile


@dataclass(kw_only=True)
class File(BaseType):
    """
    Represents a file
    """

    __type__: Literal["file"] = "file"

    id: int
    """Unique file identifier"""
    size: int
    """File size, in bytes; 0 if unknown"""
    expected_size: int
    """Approximate file size in bytes in case the exact file size is unknown. Can be used to show download/upload progress"""
    local: LocalFile
    """Information about the local copy of the file"""
    remote: RemoteFile
    """Information about the remote copy of the file"""
