from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeWallpaper(BaseType):
    """
    The file is a wallpaper or a background pattern
    """

    __type__: Literal["fileTypeWallpaper"] = "fileTypeWallpaper"
