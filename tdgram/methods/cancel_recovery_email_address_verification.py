from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class CancelRecoveryEmailAddressVerification(BaseMethod):
    """
    Cancels verification of the 2-step verification recovery email address
    """

    __type__: Literal["cancelRecoveryEmailAddressVerification"] = (
        "cancelRecoveryEmailAddressVerification"
    )
    __returning_type__ = PasswordState
