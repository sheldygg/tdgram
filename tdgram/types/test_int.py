from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TestInt(BaseType):
    """
    A simple object containing a number; for testing only
    """

    __type__: Literal["testInt"] = "testInt"

    value: int
    """Number"""
