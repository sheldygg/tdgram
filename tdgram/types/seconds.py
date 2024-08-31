from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Seconds(BaseType):
    """
    Contains a value representing a number of seconds
    """

    __type__: Literal["seconds"] = "seconds"

    seconds: float
    """Number of seconds"""
