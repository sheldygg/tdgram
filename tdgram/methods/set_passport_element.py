from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputPassportElement, PassportElement
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPassportElement(BaseMethod):
    """
    Adds an element to the user's Telegram Passport. May return an error with a message 'PHONE_VERIFICATION_NEEDED' or 'EMAIL_VERIFICATION_NEEDED' if the chosen phone number or the chosen email address must be verified first
    """

    __type__: Literal["setPassportElement"] = "setPassportElement"
    __returning_type__ = PassportElement

    element: InputPassportElement
    """Input Telegram Passport element"""
    password: str
    """The 2-step verification password of the current user"""
