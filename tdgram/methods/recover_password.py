from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class RecoverPassword(BaseMethod):
    """
    Recovers the 2-step verification password using a recovery code sent to an email address that was previously set up
    """

    __type__: Literal["recoverPassword"] = "recoverPassword"
    __returning_type__ = PasswordState

    recovery_code: str
    """Recovery code to check"""
    new_password: str | None = None
    """New 2-step verification password of the user; may be empty to remove the password"""
    new_hint: str | None = None
    """New password hint; may be empty"""
