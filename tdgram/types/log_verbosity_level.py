from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LogVerbosityLevel(BaseType):
    """
    Contains a TDLib internal log verbosity level
    """

    __type__: Literal["logVerbosityLevel"] = "logVerbosityLevel"

    verbosity_level: int
    """Log verbosity level"""
