from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentUpgradedGift(BaseType):
    """
    A message with an upgraded gift
    """

    __type__: Literal["pushMessageContentUpgradedGift"] = "pushMessageContentUpgradedGift"

    is_upgrade: bool
    """True, if the gift was obtained by upgrading of a previously received gift; otherwise, this is a transferred gift"""
