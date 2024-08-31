from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AuthenticationCodeType


@dataclass(kw_only=True)
class AuthenticationCodeInfo(BaseType):
    """
    Information about the authentication code that was sent
    """

    __type__: Literal["authenticationCodeInfo"] = "authenticationCodeInfo"

    phone_number: str
    """A phone number that is being authenticated"""
    type: AuthenticationCodeType
    """The way the code was sent to the user"""
    next_type: AuthenticationCodeType | None = None
    """The way the next code will be sent to the user; may be null"""
    timeout: int
    """Timeout before the code can be re-sent, in seconds"""
