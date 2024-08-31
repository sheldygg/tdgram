from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeFirebaseIos(BaseType):
    """
    A digit-only authentication code is delivered via Firebase Authentication to the official iOS application
    """

    __type__: Literal["authenticationCodeTypeFirebaseIos"] = "authenticationCodeTypeFirebaseIos"

    receipt: str
    """Receipt of successful application token validation to compare with receipt from push notification"""
    push_timeout: int
    """Time after the next authentication method is supposed to be used if verification push notification isn't received, in seconds"""
    length: int
    """Length of the code"""
