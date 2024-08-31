from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatSponsoredMessageResultFailed(BaseType):
    """
    The sponsored message is too old or not found
    """

    __type__: Literal["reportChatSponsoredMessageResultFailed"] = (
        "reportChatSponsoredMessageResultFailed"
    )
