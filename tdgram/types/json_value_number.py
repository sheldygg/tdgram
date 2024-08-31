from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class JsonValueNumber(BaseType):
    """
    Represents a numeric JSON value
    """

    __type__: Literal["jsonValueNumber"] = "jsonValueNumber"

    value: float
    """The value"""
