from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import NetworkType


@dataclass(kw_only=True)
class NetworkStatisticsEntryCall(BaseType):
    """
    Contains information about the total amount of data that was used for calls
    """

    __type__: Literal["networkStatisticsEntryCall"] = "networkStatisticsEntryCall"

    network_type: NetworkType
    """Type of the network the data was sent through. Call setNetworkType to maintain the actual network type"""
    sent_bytes: int
    """Total number of bytes sent"""
    received_bytes: int
    """Total number of bytes received"""
    duration: float
    """Total call duration, in seconds"""
