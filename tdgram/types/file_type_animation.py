from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeAnimation(BaseType):
    """
    The file is an animation
    """

    __type__: Literal["fileTypeAnimation"] = "fileTypeAnimation"
