from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeAuthenticationCode(BaseType):
    """
    The link contains an authentication code. Call checkAuthenticationCode with the code if the current authorization state is authorizationStateWaitCode
    """

    __type__: Literal["internalLinkTypeAuthenticationCode"] = "internalLinkTypeAuthenticationCode"

    code: str
    """The authentication code"""
