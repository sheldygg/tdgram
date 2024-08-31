from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupHasAggressiveAntiSpamEnabled(BaseMethod):
    """
    Toggles whether aggressive anti-spam checks are enabled in the supergroup. Can be called only if supergroupFullInfo.can_toggle_aggressive_anti_spam == true
    """

    __type__: Literal["toggleSupergroupHasAggressiveAntiSpamEnabled"] = (
        "toggleSupergroupHasAggressiveAntiSpamEnabled"
    )
    __returning_type__ = Ok

    supergroup_id: int
    """The identifier of the supergroup, which isn't a broadcast group"""
    has_aggressive_anti_spam_enabled: bool
    """The new value of has_aggressive_anti_spam_enabled"""
