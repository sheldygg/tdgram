from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportOption(BaseType):
    """
    Describes an option to report an entity to Telegram
    """

    __type__: Literal["reportOption"] = "reportOption"

    id: bytes
    """Unique identifier of the option"""
    text: str
    """Text of the option"""
