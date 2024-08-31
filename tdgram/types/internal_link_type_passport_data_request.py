from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypePassportDataRequest(BaseType):
    """
    The link contains a request of Telegram passport data. Call getPassportAuthorizationForm with the given parameters to process the link if the link was received from outside of the application; otherwise, ignore it
    """

    __type__: Literal["internalLinkTypePassportDataRequest"] = (
        "internalLinkTypePassportDataRequest"
    )

    bot_user_id: int
    """User identifier of the service's bot; the corresponding user may be unknown yet"""
    scope: str
    """Telegram Passport element types requested by the service"""
    public_key: str
    """Service's public key"""
    nonce: str
    """Unique request identifier provided by the service"""
    callback_url: str
    """An HTTP URL to open once the request is finished, canceled, or failed with the parameters tg_passport=success, tg_passport=cancel, or tg_passport=error&error=... respectively."""
