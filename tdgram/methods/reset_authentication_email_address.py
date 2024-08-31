from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ResetAuthenticationEmailAddress(BaseMethod):
    """
    Resets the login email address. May return an error with a message 'TASK_ALREADY_EXISTS' if reset is still pending.
    """

    __type__: Literal["resetAuthenticationEmailAddress"] = "resetAuthenticationEmailAddress"
    __returning_type__ = Ok
