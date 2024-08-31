from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypePremiumGiftCode(BaseType):
    """
    The link is a link with a Telegram Premium gift code. Call checkPremiumGiftCode with the given code to process the link.
    """

    __type__: Literal["internalLinkTypePremiumGiftCode"] = "internalLinkTypePremiumGiftCode"

    code: str
    """The Telegram Premium gift code"""
