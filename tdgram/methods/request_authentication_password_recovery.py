from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RequestAuthenticationPasswordRecovery(BaseMethod):
    """
    Requests to send a 2-step verification password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
    """

    __type__: Literal["requestAuthenticationPasswordRecovery"] = (
        "requestAuthenticationPasswordRecovery"
    )
    __returning_type__ = Ok
