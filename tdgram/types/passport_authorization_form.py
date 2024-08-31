from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PassportRequiredElement


@dataclass(kw_only=True)
class PassportAuthorizationForm(BaseType):
    """
    Contains information about a Telegram Passport authorization form that was requested
    """

    __type__: Literal["passportAuthorizationForm"] = "passportAuthorizationForm"

    id: int
    """Unique identifier of the authorization form"""
    required_elements: list[PassportRequiredElement]
    """Telegram Passport elements that must be provided to complete the form"""
    privacy_policy_url: str | None = None
    """URL for the privacy policy of the service; may be empty"""
