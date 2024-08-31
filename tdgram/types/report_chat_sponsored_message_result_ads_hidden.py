from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatSponsoredMessageResultAdsHidden(BaseType):
    """
    Sponsored messages were hidden for the user in all chats
    """

    __type__: Literal["reportChatSponsoredMessageResultAdsHidden"] = (
        "reportChatSponsoredMessageResultAdsHidden"
    )
