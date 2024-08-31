from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StorageStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStorageStatistics(BaseMethod):
    """
    Returns storage usage statistics. Can be called before authorization
    """

    __type__: Literal["getStorageStatistics"] = "getStorageStatistics"
    __returning_type__ = StorageStatistics

    chat_limit: int
    """The maximum number of chats with the largest storage usage for which separate statistics need to be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0"""
