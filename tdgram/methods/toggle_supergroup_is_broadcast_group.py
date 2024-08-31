from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupIsBroadcastGroup(BaseMethod):
    """
    Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup
    """

    __type__: Literal["toggleSupergroupIsBroadcastGroup"] = "toggleSupergroupIsBroadcastGroup"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup"""
