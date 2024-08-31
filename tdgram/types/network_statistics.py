from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import NetworkStatisticsEntry


@dataclass(kw_only=True)
class NetworkStatistics(BaseType):
    """
    A full list of available network statistic entries
    """

    __type__: Literal["networkStatistics"] = "networkStatistics"

    since_date: int
    """Point in time (Unix timestamp) from which the statistics are collected"""
    entries: list[NetworkStatisticsEntry]
    """Network statistics entries"""
