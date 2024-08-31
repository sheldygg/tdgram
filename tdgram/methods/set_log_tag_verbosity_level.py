from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetLogTagVerbosityLevel(BaseMethod):
    """
    Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously
    """

    __type__: Literal["setLogTagVerbosityLevel"] = "setLogTagVerbosityLevel"
    __returning_type__ = Ok

    tag: str
    """Logging tag to change verbosity level"""
    new_verbosity_level: int
    """New verbosity level; 1-1024"""
