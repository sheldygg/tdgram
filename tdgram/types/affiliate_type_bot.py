from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AffiliateTypeBot(BaseType):
    """
    The affiliate is a bot owned by the current user
    """

    __type__: Literal["affiliateTypeBot"] = "affiliateTypeBot"

    user_id: int
    """User identifier of the bot"""
