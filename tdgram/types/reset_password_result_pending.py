from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ResetPasswordResultPending(BaseType):
    """
    The password reset request is pending
    """

    __type__: Literal["resetPasswordResultPending"] = "resetPasswordResultPending"

    pending_reset_date: int
    """Point in time (Unix timestamp) after which the password can be reset immediately using resetPassword"""
