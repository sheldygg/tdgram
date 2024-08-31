from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ResendCodeReason
from .base import BaseMethod


@dataclass(kw_only=True)
class ResendAuthenticationCode(BaseMethod):
    """
    Resends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode, the next_code_type of the result is not null
    """

    __type__: Literal["resendAuthenticationCode"] = "resendAuthenticationCode"
    __returning_type__ = Ok

    reason: ResendCodeReason | None = None
    """Reason of code resending; pass null if unknown"""
