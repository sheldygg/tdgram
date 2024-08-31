from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupIsForum(BaseMethod):
    """
    Toggles whether the supergroup is a forum; requires owner privileges in the supergroup. Discussion supergroups can't be converted to forums
    """

    __type__: Literal["toggleSupergroupIsForum"] = "toggleSupergroupIsForum"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup"""
    is_forum: bool
    """New value of is_forum"""
