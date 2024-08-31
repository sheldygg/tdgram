from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RecoverAuthenticationPassword(BaseMethod):
    """
    Recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
    """

    __type__: Literal["recoverAuthenticationPassword"] = "recoverAuthenticationPassword"
    __returning_type__ = Ok

    recovery_code: str
    """Recovery code to check"""
    new_password: str | None = None
    """New 2-step verification password of the user; may be empty to remove the password"""
    new_hint: str | None = None
    """New password hint; may be empty"""
