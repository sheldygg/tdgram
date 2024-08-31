from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class OptionValueBoolean(BaseType):
    """
    Represents a boolean option
    """

    __type__: Literal["optionValueBoolean"] = "optionValueBoolean"

    value: bool
    """The value of the option"""
