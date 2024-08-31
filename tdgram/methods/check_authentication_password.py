from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckAuthenticationPassword(BaseMethod):
    """
    Checks the 2-step verification password for correctness. Works only when the current authorization state is authorizationStateWaitPassword
    """

    __type__: Literal["checkAuthenticationPassword"] = "checkAuthenticationPassword"
    __returning_type__ = Ok

    password: str
    """The 2-step verification password to check"""
