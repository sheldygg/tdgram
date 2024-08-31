from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatSponsoredMessageResultPremiumRequired(BaseType):
    """
    The user asked to hide sponsored messages, but Telegram Premium is required for this
    """

    __type__: Literal["reportChatSponsoredMessageResultPremiumRequired"] = (
        "reportChatSponsoredMessageResultPremiumRequired"
    )
