from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FileType, StorageStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class OptimizeStorage(BaseMethod):
    """
    Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted
    """

    __type__: Literal["optimizeStorage"] = "optimizeStorage"
    __returning_type__ = StorageStatistics

    size: int
    """Limit on the total size of files after deletion, in bytes. Pass -1 to use the default limit"""
    ttl: int
    """Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit"""
    count: int
    """Limit on the total number of files after deletion. Pass -1 to use the default limit"""
    immunity_delay: int
    """The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value"""
    file_types: list[FileType] | None = None
    """If non-empty, only files with the given types are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted"""
    chat_ids: list[int] | None = None
    """If non-empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)"""
    exclude_chat_ids: list[int] | None = None
    """If non-empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)"""
    return_deleted_file_statistics: bool
    """Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics"""
    chat_limit: int
    """Same as in getStorageStatistics. Affects only returned statistics"""
