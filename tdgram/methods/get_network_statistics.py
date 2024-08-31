from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NetworkStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetNetworkStatistics(BaseMethod):
    """
    Returns network data usage statistics. Can be called before authorization
    """

    __type__: Literal["getNetworkStatistics"] = "getNetworkStatistics"
    __returning_type__ = NetworkStatistics

    only_current: bool
    """Pass true to get statistics only for the current library launch"""
