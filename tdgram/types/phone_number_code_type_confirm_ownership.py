from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PhoneNumberCodeTypeConfirmOwnership(BaseType):
    """
    Confirms ownership of a phone number to prevent account deletion while handling links of the type internalLinkTypePhoneNumberConfirmation
    """

    __type__: Literal["phoneNumberCodeTypeConfirmOwnership"] = (
        "phoneNumberCodeTypeConfirmOwnership"
    )

    hash: str
    """Hash value from the link"""
