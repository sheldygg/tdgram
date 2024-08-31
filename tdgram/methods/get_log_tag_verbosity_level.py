from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LogVerbosityLevel
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLogTagVerbosityLevel(BaseMethod):
    """
    Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously
    """

    __type__: Literal["getLogTagVerbosityLevel"] = "getLogTagVerbosityLevel"
    __returning_type__ = LogVerbosityLevel

    tag: str
    """Logging tag to change verbosity level"""
