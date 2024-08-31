from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeSimilarChatCount(BaseType):
    """
    The maximum number of received similar chats
    """

    __type__: Literal["premiumLimitTypeSimilarChatCount"] = "premiumLimitTypeSimilarChatCount"
