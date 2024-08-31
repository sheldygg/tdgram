from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupUsernameIsActive(BaseMethod):
    """
    Changes active state for a username of a supergroup or channel, requires owner privileges in the supergroup or channel. The editable username can't be disabled.
    """

    __type__: Literal["toggleSupergroupUsernameIsActive"] = "toggleSupergroupUsernameIsActive"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup or channel"""
    username: str
    """The username to change"""
    is_active: bool
    """Pass true to activate the username; pass false to disable it"""
