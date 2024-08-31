from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BackgroundTypeWallpaper(BaseType):
    """
    A wallpaper in JPEG format
    """

    __type__: Literal["backgroundTypeWallpaper"] = "backgroundTypeWallpaper"

    is_blurred: bool
    """True, if the wallpaper must be downscaled to fit in 450x450 square and then box-blurred with radius 12"""
    is_moving: bool
    """True, if the background needs to be slightly moved when device is tilted"""
