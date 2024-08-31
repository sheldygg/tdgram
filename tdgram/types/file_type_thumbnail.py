from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeThumbnail(BaseType):
    """
    The file is a thumbnail of another file
    """

    __type__: Literal["fileTypeThumbnail"] = "fileTypeThumbnail"
