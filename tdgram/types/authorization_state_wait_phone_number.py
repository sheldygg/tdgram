from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateWaitPhoneNumber(BaseType):
    """
    TDLib needs the user's phone number to authorize. Call setAuthenticationPhoneNumber to provide the phone number, or use requestQrCodeAuthentication or checkAuthenticationBotToken for other authentication options
    """

    __type__: Literal["authorizationStateWaitPhoneNumber"] = "authorizationStateWaitPhoneNumber"
