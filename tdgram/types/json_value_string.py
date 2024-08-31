from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class JsonValueString(BaseType):
    """
    Represents a string JSON value
    """

    __type__: Literal["jsonValueString"] = "jsonValueString"

    value: str
    """The value"""
