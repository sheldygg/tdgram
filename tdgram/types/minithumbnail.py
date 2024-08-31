from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Minithumbnail(BaseType):
    """
    Thumbnail image of a very poor quality and low resolution
    """

    __type__: Literal["minithumbnail"] = "minithumbnail"

    width: int
    """Thumbnail width, usually doesn't exceed 40"""
    height: int
    """Thumbnail height, usually doesn't exceed 40"""
    data: bytes
    """The thumbnail in JPEG format"""
