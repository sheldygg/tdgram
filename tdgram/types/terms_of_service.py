from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class TermsOfService(BaseType):
    """
    Contains Telegram terms of service
    """

    __type__: Literal["termsOfService"] = "termsOfService"

    text: FormattedText
    """Text of the terms of service"""
    min_user_age: int
    """The minimum age of a user to be able to accept the terms; 0 if age isn't restricted"""
    show_popup: bool
    """True, if a blocking popup with terms of service must be shown to the user"""
