from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatResultMessagesRequired(BaseType):
    """
    The user must choose messages to report and repeat the reportChat request with the chosen messages
    """

    __type__: Literal["reportChatResultMessagesRequired"] = "reportChatResultMessagesRequired"
