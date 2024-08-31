from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FileType


@dataclass(kw_only=True)
class StorageStatisticsByFileType(BaseType):
    """
    Contains the storage usage statistics for a specific file type
    """

    __type__: Literal["storageStatisticsByFileType"] = "storageStatisticsByFileType"

    file_type: FileType
    """File type"""
    size: int
    """Total size of the files, in bytes"""
    count: int
    """Total number of files"""
