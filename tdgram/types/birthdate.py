from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Birthdate(BaseType):
    """
    Represents a birthdate of a user
    """

    __type__: Literal["birthdate"] = "birthdate"

    day: int
    """Day of the month; 1-31"""
    month: int
    """Month of the year; 1-12"""
    year: int
    """Birth year; 0 if unknown"""
