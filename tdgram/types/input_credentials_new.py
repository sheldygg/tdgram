from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputCredentialsNew(BaseType):
    """
    Applies if a user enters new credentials on a payment provider website
    """

    __type__: Literal["inputCredentialsNew"] = "inputCredentialsNew"

    data: str
    """JSON-encoded data with the credential identifier from the payment provider"""
    allow_save: bool
    """True, if the credential identifier can be saved on the server side"""
