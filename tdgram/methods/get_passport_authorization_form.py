from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PassportAuthorizationForm
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPassportAuthorizationForm(BaseMethod):
    """
    Returns a Telegram Passport authorization form for sharing data with a service
    """

    __type__: Literal["getPassportAuthorizationForm"] = "getPassportAuthorizationForm"
    __returning_type__ = PassportAuthorizationForm

    bot_user_id: int
    """User identifier of the service's bot"""
    scope: str
    """Telegram Passport element types requested by the service"""
    public_key: str
    """Service's public key"""
    nonce: str
    """Unique request identifier provided by the service"""
