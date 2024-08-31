from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmailAddressAuthenticationCodeInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class SetLoginEmailAddress(BaseMethod):
    """
    Changes the login email address of the user. The email address can be changed only if the current user already has login email and passwordState.login_email_address_pattern is non-empty.
    """

    __type__: Literal["setLoginEmailAddress"] = "setLoginEmailAddress"
    __returning_type__ = EmailAddressAuthenticationCodeInfo

    new_login_email_address: str
    """New login email address"""
