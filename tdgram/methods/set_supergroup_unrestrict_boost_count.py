from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetSupergroupUnrestrictBoostCount(BaseMethod):
    """
    Changes the number of times the supergroup must be boosted by a user to ignore slow mode and chat permission restrictions; requires can_restrict_members administrator right
    """

    __type__: Literal["setSupergroupUnrestrictBoostCount"] = "setSupergroupUnrestrictBoostCount"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup"""
    unrestrict_boost_count: int
    """New value of the unrestrict_boost_count supergroup setting; 0-8. Use 0 to remove the setting"""
