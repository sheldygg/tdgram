from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddLogMessage(BaseMethod):
    """
    Adds a message to TDLib internal log. Can be called synchronously
    """

    __type__: Literal["addLogMessage"] = "addLogMessage"
    __returning_type__ = Ok

    verbosity_level: int
    """The minimum verbosity level needed for the message to be logged; 0-1023"""
    text: str
    """Text of a message to log"""
