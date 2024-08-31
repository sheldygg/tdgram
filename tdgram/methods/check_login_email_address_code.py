from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmailAddressAuthentication, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckLoginEmailAddressCode(BaseMethod):
    """
    Checks the login email address authentication
    """

    __type__: Literal["checkLoginEmailAddressCode"] = "checkLoginEmailAddressCode"
    __returning_type__ = Ok

    code: EmailAddressAuthentication
    """Email address authentication to check"""
