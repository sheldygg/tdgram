from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LoginUrlInfoRequestConfirmation(BaseType):
    """
    An authorization confirmation dialog needs to be shown to the user
    """

    __type__: Literal["loginUrlInfoRequestConfirmation"] = "loginUrlInfoRequestConfirmation"

    url: str
    """An HTTP URL to be opened"""
    domain: str
    """A domain of the URL"""
    bot_user_id: int
    """User identifier of a bot linked with the website"""
    request_write_access: bool
    """True, if the user must be asked for the permission to the bot to send them messages"""
