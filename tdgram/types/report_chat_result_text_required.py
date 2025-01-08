from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportChatResultTextRequired(BaseType):
    """
    The user must add additional text details to the report
    """

    __type__: Literal["reportChatResultTextRequired"] = "reportChatResultTextRequired"

    option_id: bytes
    """Option identifier for the next reportChat request"""
    is_optional: bool
    """True, if the user can skip text adding"""
