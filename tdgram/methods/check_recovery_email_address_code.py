from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckRecoveryEmailAddressCode(BaseMethod):
    """
    Checks the 2-step verification recovery email address verification code
    """

    __type__: Literal["checkRecoveryEmailAddressCode"] = "checkRecoveryEmailAddressCode"
    __returning_type__ = PasswordState

    code: str
    """Verification code to check"""
