from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LogVerbosityLevel
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLogVerbosityLevel(BaseMethod):
    """
    Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
    """

    __type__: Literal["getLogVerbosityLevel"] = "getLogVerbosityLevel"
    __returning_type__ = LogVerbosityLevel
