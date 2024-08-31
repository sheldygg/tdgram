from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class ResendRecoveryEmailAddressCode(BaseMethod):
    """
    Resends the 2-step verification recovery email address verification code
    """

    __type__: Literal["resendRecoveryEmailAddressCode"] = "resendRecoveryEmailAddressCode"
    __returning_type__ = PasswordState
