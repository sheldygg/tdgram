from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class RecoveryEmailAddress(BaseType):
    """
    Contains information about the current recovery email address
    """

    __type__: Literal["recoveryEmailAddress"] = "recoveryEmailAddress"

    recovery_email_address: str
    """Recovery email address"""
