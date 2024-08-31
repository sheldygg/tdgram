from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PassportElement, PassportElementType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPassportElement(BaseMethod):
    """
    Returns one of the available Telegram Passport elements
    """

    __type__: Literal["getPassportElement"] = "getPassportElement"
    __returning_type__ = PassportElement

    type: PassportElementType
    """Telegram Passport element type"""
    password: str
    """The 2-step verification password of the current user"""
