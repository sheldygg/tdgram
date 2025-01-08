from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BackgroundFillFreeformGradient(BaseType):
    """
    Describes a freeform gradient fill of a background
    """

    __type__: Literal["backgroundFillFreeformGradient"] = "backgroundFillFreeformGradient"

    colors: list[int]
    """A list of 3 or 4 colors of the freeform gradient in the RGB format"""
