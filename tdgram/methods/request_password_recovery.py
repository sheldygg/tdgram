from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmailAddressAuthenticationCodeInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class RequestPasswordRecovery(BaseMethod):
    """
    Requests to send a 2-step verification password recovery code to an email address that was previously set up
    """

    __type__: Literal["requestPasswordRecovery"] = "requestPasswordRecovery"
    __returning_type__ = EmailAddressAuthenticationCodeInfo
