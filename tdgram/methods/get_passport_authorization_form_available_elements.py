from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PassportElementsWithErrors
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPassportAuthorizationFormAvailableElements(BaseMethod):
    """
    Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form
    """

    __type__: Literal["getPassportAuthorizationFormAvailableElements"] = (
        "getPassportAuthorizationFormAvailableElements"
    )
    __returning_type__ = PassportElementsWithErrors

    authorization_form_id: int
    """Authorization form identifier"""
    password: str
    """The 2-step verification password of the current user"""
