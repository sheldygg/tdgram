from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeSticker(BaseType):
    """
    The file is a sticker
    """

    __type__: Literal["fileTypeSticker"] = "fileTypeSticker"
