from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AuthenticationCodeInfo


@dataclass(kw_only=True)
class AuthorizationStateWaitCode(BaseType):
    """
    TDLib needs the user's authentication code to authorize. Call checkAuthenticationCode to check the code
    """

    __type__: Literal["authorizationStateWaitCode"] = "authorizationStateWaitCode"

    code_info: AuthenticationCodeInfo
    """Information about the authorization code that was sent"""
