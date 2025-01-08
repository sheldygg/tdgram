from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportStoryResultTextRequired(BaseType):
    """
    The user must add additional text details to the report
    """

    __type__: Literal["reportStoryResultTextRequired"] = "reportStoryResultTextRequired"

    option_id: bytes
    """Option identifier for the next reportStory request"""
    is_optional: bool
    """True, if the user can skip text adding"""
