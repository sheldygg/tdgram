from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NetworkStatisticsEntry, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddNetworkStatistics(BaseMethod):
    """
    Adds the specified data to data usage statistics. Can be called before authorization
    """

    __type__: Literal["addNetworkStatistics"] = "addNetworkStatistics"
    __returning_type__ = Ok

    entry: NetworkStatisticsEntry
    """The network statistics entry with the data to be added to statistics"""
