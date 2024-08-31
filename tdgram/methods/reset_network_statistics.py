from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ResetNetworkStatistics(BaseMethod):
    """
    Resets all network data usage statistics to zero. Can be called before authorization
    """

    __type__: Literal["resetNetworkStatistics"] = "resetNetworkStatistics"
    __returning_type__ = Ok
