from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import RecoveryEmailAddress
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecoveryEmailAddress(BaseMethod):
    """
    Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user
    """

    __type__: Literal["getRecoveryEmailAddress"] = "getRecoveryEmailAddress"
    __returning_type__ = RecoveryEmailAddress

    password: str
    """The 2-step verification password for the current user"""
