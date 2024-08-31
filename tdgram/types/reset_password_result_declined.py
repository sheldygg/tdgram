from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ResetPasswordResultDeclined(BaseType):
    """
    The password reset request was declined
    """

    __type__: Literal["resetPasswordResultDeclined"] = "resetPasswordResultDeclined"

    retry_date: int
    """Point in time (Unix timestamp) when the password reset can be retried"""
