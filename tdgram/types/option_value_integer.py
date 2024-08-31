from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class OptionValueInteger(BaseType):
    """
    Represents an integer option
    """

    __type__: Literal["optionValueInteger"] = "optionValueInteger"

    value: int
    """The value of the option"""
