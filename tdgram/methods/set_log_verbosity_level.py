from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetLogVerbosityLevel(BaseMethod):
    """
    Sets the verbosity level of the internal logging of TDLib. Can be called synchronously
    """

    __type__: Literal["setLogVerbosityLevel"] = "setLogVerbosityLevel"
    __returning_type__ = Ok

    new_verbosity_level: int
    """New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings,"""
