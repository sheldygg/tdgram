from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypePhoneNumberConfirmation(BaseType):
    """
    The link can be used to confirm ownership of a phone number to prevent account deletion. Call sendPhoneNumberCode with the given phone number and with phoneNumberCodeTypeConfirmOwnership with the given hash to process the link.
    """

    __type__: Literal["internalLinkTypePhoneNumberConfirmation"] = (
        "internalLinkTypePhoneNumberConfirmation"
    )

    hash: str
    """Hash value from the link"""
    phone_number: str
    """Phone number value from the link"""
