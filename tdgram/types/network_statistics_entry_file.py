from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FileType, NetworkType


@dataclass(kw_only=True)
class NetworkStatisticsEntryFile(BaseType):
    """
    Contains information about the total amount of data that was used to send and receive files
    """

    __type__: Literal["networkStatisticsEntryFile"] = "networkStatisticsEntryFile"

    file_type: FileType | None = None
    """Type of the file the data is part of; pass null if the data isn't related to files"""
    network_type: NetworkType
    """Type of the network the data was sent through. Call setNetworkType to maintain the actual network type"""
    sent_bytes: int
    """Total number of bytes sent"""
    received_bytes: int
    """Total number of bytes received"""
