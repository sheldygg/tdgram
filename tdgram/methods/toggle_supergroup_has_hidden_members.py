from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupHasHiddenMembers(BaseMethod):
    """
    Toggles whether non-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers. Can be called only if supergroupFullInfo.can_hide_members == true
    """

    __type__: Literal["toggleSupergroupHasHiddenMembers"] = "toggleSupergroupHasHiddenMembers"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup"""
    has_hidden_members: bool
    """New value of has_hidden_members"""
