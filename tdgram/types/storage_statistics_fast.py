from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StorageStatisticsFast(BaseType):
    """
    Contains approximate storage usage statistics, excluding files of unknown file type
    """

    __type__: Literal["storageStatisticsFast"] = "storageStatisticsFast"

    files_size: int
    """Approximate total size of files, in bytes"""
    file_count: int
    """Approximate number of files"""
    database_size: int
    """Size of the database"""
    language_pack_database_size: int
    """Size of the language pack database"""
    log_size: int
    """Size of the TDLib internal log"""
