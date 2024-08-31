from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckPasswordRecoveryCode(BaseMethod):
    """
    Checks whether a 2-step verification password recovery code sent to an email address is valid
    """

    __type__: Literal["checkPasswordRecoveryCode"] = "checkPasswordRecoveryCode"
    __returning_type__ = Ok

    recovery_code: str
    """Recovery code to check"""
