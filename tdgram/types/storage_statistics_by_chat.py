from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StorageStatisticsByFileType


@dataclass(kw_only=True)
class StorageStatisticsByChat(BaseType):
    """
    Contains the storage usage statistics for a specific chat
    """

    __type__: Literal["storageStatisticsByChat"] = "storageStatisticsByChat"

    chat_id: int
    """Chat identifier; 0 if none"""
    size: int
    """Total size of the files in the chat, in bytes"""
    count: int
    """Total number of files in the chat"""
    by_file_type: list[StorageStatisticsByFileType]
    """Statistics split by file types"""
