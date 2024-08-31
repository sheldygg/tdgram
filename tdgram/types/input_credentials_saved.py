from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputCredentialsSaved(BaseType):
    """
    Applies if a user chooses some previously saved payment credentials. To use their previously saved credentials, the user must have a valid temporary password
    """

    __type__: Literal["inputCredentialsSaved"] = "inputCredentialsSaved"

    saved_credentials_id: str
    """Identifier of the saved credentials"""
