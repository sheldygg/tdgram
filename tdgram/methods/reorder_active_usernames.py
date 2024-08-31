from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReorderActiveUsernames(BaseMethod):
    """
    Changes order of active usernames of the current user
    """

    __type__: Literal["reorderActiveUsernames"] = "reorderActiveUsernames"
    __returning_type__ = Ok

    usernames: list[str]
    """The new order of active usernames. All currently active usernames must be specified"""
