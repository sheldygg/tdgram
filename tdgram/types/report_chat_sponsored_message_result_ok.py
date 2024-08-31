from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatSponsoredMessageResultOk(BaseType):
    """
    The message was reported successfully
    """

    __type__: Literal["reportChatSponsoredMessageResultOk"] = "reportChatSponsoredMessageResultOk"
