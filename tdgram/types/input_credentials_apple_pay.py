from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputCredentialsApplePay(BaseType):
    """
    Applies if a user enters new credentials using Apple Pay
    """

    __type__: Literal["inputCredentialsApplePay"] = "inputCredentialsApplePay"

    data: str
    """JSON-encoded data with the credential identifier"""
