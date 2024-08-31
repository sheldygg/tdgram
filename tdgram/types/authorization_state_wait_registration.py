from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TermsOfService


@dataclass(kw_only=True)
class AuthorizationStateWaitRegistration(BaseType):
    """
    The user is unregistered and need to accept terms of service and enter their first name and last name to finish registration. Call registerUser to accept the terms of service and provide the data
    """

    __type__: Literal["authorizationStateWaitRegistration"] = "authorizationStateWaitRegistration"

    terms_of_service: TermsOfService
    """Telegram terms of service"""
