from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypePremiumFeatures(BaseType):
    """
    The link is a link to the Premium features screen of the application from which the user can subscribe to Telegram Premium. Call getPremiumFeatures with the given referrer to process the link
    """

    __type__: Literal["internalLinkTypePremiumFeatures"] = "internalLinkTypePremiumFeatures"

    referrer: str
    """Referrer specified in the link"""
