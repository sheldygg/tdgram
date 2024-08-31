from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleUsernameIsActive(BaseMethod):
    """
    Changes active state for a username of the current user. The editable username can't be disabled. May return an error with a message 'USERNAMES_ACTIVE_TOO_MUCH' if the maximum number of active usernames has been reached
    """

    __type__: Literal["toggleUsernameIsActive"] = "toggleUsernameIsActive"
    __returning_type__ = Ok

    username: str
    """The username to change"""
    is_active: bool
    """Pass true to activate the username; pass false to disable it"""
