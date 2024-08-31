from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupIsAllHistoryAvailable(BaseMethod):
    """
    Toggles whether the message history of a supergroup is available to new members; requires can_change_info member right
    """

    __type__: Literal["toggleSupergroupIsAllHistoryAvailable"] = (
        "toggleSupergroupIsAllHistoryAvailable"
    )
    __returning_type__ = Ok

    supergroup_id: int
    """The identifier of the supergroup"""
    is_all_history_available: bool
    """The new value of is_all_history_available"""
