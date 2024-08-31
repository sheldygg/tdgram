from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class JsonValueBoolean(BaseType):
    """
    Represents a boolean JSON value
    """

    __type__: Literal["jsonValueBoolean"] = "jsonValueBoolean"

    value: bool
    """The value"""
