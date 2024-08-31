from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import OptionValue


@dataclass(kw_only=True)
class UpdateOption(BaseType):
    """
    An option changed its value
    """

    __type__: Literal["updateOption"] = "updateOption"

    name: str
    """The option name"""
    value: OptionValue
    """The new option value"""
