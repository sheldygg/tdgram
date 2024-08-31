from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Point(BaseType):
    """
    A point on a Cartesian plane
    """

    __type__: Literal["point"] = "point"

    x: float
    """The point's first coordinate"""
    y: float
    """The point's second coordinate"""
