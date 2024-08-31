from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatSponsoredMessageOption(BaseType):
    """
    Describes an option to report a sponsored message
    """

    __type__: Literal["reportChatSponsoredMessageOption"] = "reportChatSponsoredMessageOption"

    id: bytes
    """Unique identifier of the option"""
    text: str
    """Text of the option"""
