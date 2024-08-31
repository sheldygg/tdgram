from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputCredentialsGooglePay(BaseType):
    """
    Applies if a user enters new credentials using Google Pay
    """

    __type__: Literal["inputCredentialsGooglePay"] = "inputCredentialsGooglePay"

    data: str
    """JSON-encoded data with the credential identifier"""
