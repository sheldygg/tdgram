from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BackgroundFillGradient(BaseType):
    """
    Describes a gradient fill of a background
    """

    __type__: Literal["backgroundFillGradient"] = "backgroundFillGradient"

    top_color: int
    """A top color of the background in the RGB24 format"""
    bottom_color: int
    """A bottom color of the background in the RGB24 format"""
    rotation_angle: int
    """Clockwise rotation angle of the gradient, in degrees; 0-359. Must always be divisible by 45"""
