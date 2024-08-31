from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class OptionValueString(BaseType):
    """
    Represents a string option
    """

    __type__: Literal["optionValueString"] = "optionValueString"

    value: str
    """The value of the option"""
