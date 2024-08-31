from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupJoinByRequest(BaseMethod):
    """
    Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can_restrict_members administrator right
    """

    __type__: Literal["toggleSupergroupJoinByRequest"] = "toggleSupergroupJoinByRequest"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup that isn't a broadcast group"""
    join_by_request: bool
    """New value of join_by_request"""
