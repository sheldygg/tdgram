from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AffiliateTypeChannel(BaseType):
    """
    The affiliate is a channel chat where the current user has can_post_messages administrator right
    """

    __type__: Literal["affiliateTypeChannel"] = "affiliateTypeChannel"

    chat_id: int
    """Identifier of the channel chat"""
