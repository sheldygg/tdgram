from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, PassportElementType
from .base import BaseMethod


@dataclass(kw_only=True)
class SendPassportAuthorizationForm(BaseMethod):
    """
    Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused
    """

    __type__: Literal["sendPassportAuthorizationForm"] = "sendPassportAuthorizationForm"
    __returning_type__ = Ok

    authorization_form_id: int
    """Authorization form identifier"""
    types: list[PassportElementType]
    """Types of Telegram Passport elements chosen by user to complete the authorization form"""
