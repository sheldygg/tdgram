from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DisableAllSupergroupUsernames(BaseMethod):
    """
    Disables all active non-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel
    """

    __type__: Literal["disableAllSupergroupUsernames"] = "disableAllSupergroupUsernames"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup or channel"""
