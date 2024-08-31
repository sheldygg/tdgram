from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetAlarm(BaseMethod):
    """
    Succeeds after a specified amount of time has passed. Can be called before initialization
    """

    __type__: Literal["setAlarm"] = "setAlarm"
    __returning_type__ = Ok

    seconds: float
    """Number of seconds before the function returns"""
