from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatResultOk(BaseType):
    """
    The chat was reported successfully
    """

    __type__: Literal["reportChatResultOk"] = "reportChatResultOk"
