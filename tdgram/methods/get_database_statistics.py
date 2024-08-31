from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import DatabaseStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDatabaseStatistics(BaseMethod):
    """
    Returns database statistics
    """

    __type__: Literal["getDatabaseStatistics"] = "getDatabaseStatistics"
    __returning_type__ = DatabaseStatistics
