from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeNone(BaseType):
    """
    The data is not a file
    """

    __type__: Literal["fileTypeNone"] = "fileTypeNone"
