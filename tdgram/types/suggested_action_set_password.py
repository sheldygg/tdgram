from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionSetPassword(BaseType):
    """
    Suggests the user to set a 2-step verification password to be able to log in again
    """

    __type__: Literal["suggestedActionSetPassword"] = "suggestedActionSetPassword"

    authorization_delay: int
    """The number of days to pass between consecutive authorizations if the user declines to set password; if 0, then the user is advised to set the password for security reasons"""
