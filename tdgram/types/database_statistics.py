from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DatabaseStatistics(BaseType):
    """
    Contains database statistics
    """

    __type__: Literal["databaseStatistics"] = "databaseStatistics"

    statistics: str
    """Database statistics in an unspecified human-readable format"""
