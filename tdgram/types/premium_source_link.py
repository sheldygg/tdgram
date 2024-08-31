from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumSourceLink(BaseType):
    """
    A user opened an internal link of the type internalLinkTypePremiumFeatures
    """

    __type__: Literal["premiumSourceLink"] = "premiumSourceLink"

    referrer: str
    """The referrer from the link"""
