from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class OptionValueEmpty(BaseType):
    """
    Represents an unknown option or an option which has a default value
    """

    __type__: Literal["optionValueEmpty"] = "optionValueEmpty"
