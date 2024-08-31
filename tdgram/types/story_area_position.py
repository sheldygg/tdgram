from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryAreaPosition(BaseType):
    """
    Describes position of a clickable rectangle area on a story media
    """

    __type__: Literal["storyAreaPosition"] = "storyAreaPosition"

    x_percentage: float
    """The abscissa of the rectangle's center, as a percentage of the media width"""
    y_percentage: float
    """The ordinate of the rectangle's center, as a percentage of the media height"""
    width_percentage: float
    """The width of the rectangle, as a percentage of the media width"""
    height_percentage: float
    """The height of the rectangle, as a percentage of the media height"""
    rotation_angle: float
    """Clockwise rotation angle of the rectangle, in degrees; 0-360"""
    corner_radius_percentage: float
    """The radius of the rectangle corner rounding, as a percentage of the media width"""
