from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StorageStatisticsByChat


@dataclass(kw_only=True)
class StorageStatistics(BaseType):
    """
    Contains the exact storage usage statistics split by chats and file type
    """

    __type__: Literal["storageStatistics"] = "storageStatistics"

    size: int
    """Total size of files, in bytes"""
    count: int
    """Total number of files"""
    by_chat: list[StorageStatisticsByChat]
    """Statistics split by chats"""
