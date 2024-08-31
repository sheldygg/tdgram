from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, OptionValue
from .base import BaseMethod


@dataclass(kw_only=True)
class SetOption(BaseMethod):
    """
    Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization
    """

    __type__: Literal["setOption"] = "setOption"
    __returning_type__ = Ok

    name: str
    """The name of the option"""
    value: OptionValue | None = None
    """The new value of the option; pass null to reset option value to a default value"""
