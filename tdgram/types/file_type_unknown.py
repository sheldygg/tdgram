from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeUnknown(BaseType):
    """
    The file type is not yet known
    """

    __type__: Literal["fileTypeUnknown"] = "fileTypeUnknown"
