from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPassword(BaseMethod):
    """
    Changes the 2-step verification password for the current user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed
    """

    __type__: Literal["setPassword"] = "setPassword"
    __returning_type__ = PasswordState

    old_password: str
    """Previous 2-step verification password of the user"""
    new_password: str | None = None
    """New 2-step verification password of the user; may be empty to remove the password"""
    new_hint: str | None = None
    """New password hint; may be empty"""
    set_recovery_email_address: bool
    """Pass true to change also the recovery email address"""
    new_recovery_email_address: str | None = None
    """New recovery email address; may be empty"""
