from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LanguagePackStringValueOrdinary(BaseType):
    """
    An ordinary language pack string
    """

    __type__: Literal["languagePackStringValueOrdinary"] = "languagePackStringValueOrdinary"

    value: str
    """String value"""
