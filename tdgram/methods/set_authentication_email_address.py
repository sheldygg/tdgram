from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetAuthenticationEmailAddress(BaseMethod):
    """
    Sets the email address of the user and sends an authentication code to the email address. Works only when the current authorization state is authorizationStateWaitEmailAddress
    """

    __type__: Literal["setAuthenticationEmailAddress"] = "setAuthenticationEmailAddress"
    __returning_type__ = Ok

    email_address: str
    """The email address of the user"""
