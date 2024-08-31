from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckAuthenticationCode(BaseMethod):
    """
    Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode
    """

    __type__: Literal["checkAuthenticationCode"] = "checkAuthenticationCode"
    __returning_type__ = Ok

    code: str
    """Authentication code to check"""
