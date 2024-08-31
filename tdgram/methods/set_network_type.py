from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NetworkType, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetNetworkType(BaseMethod):
    """
    Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks,
    """

    __type__: Literal["setNetworkType"] = "setNetworkType"
    __returning_type__ = Ok

    type: NetworkType | None = None
    """The new network type; pass null to set network type to networkTypeOther"""
