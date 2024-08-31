from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TestString


@dataclass(kw_only=True)
class TestVectorStringObject(BaseType):
    """
    A simple object containing a vector of objects that hold a string; for testing only
    """

    __type__: Literal["testVectorStringObject"] = "testVectorStringObject"

    value: list[TestString]
    """Vector of objects"""
