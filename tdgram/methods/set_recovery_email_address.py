from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class SetRecoveryEmailAddress(BaseMethod):
    """
    Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed.
    """

    __type__: Literal["setRecoveryEmailAddress"] = "setRecoveryEmailAddress"
    __returning_type__ = PasswordState

    password: str
    """The 2-step verification password of the current user"""
    new_recovery_email_address: str
    """New recovery email address"""
