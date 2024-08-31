from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypePhoto(BaseType):
    """
    The file is a photo
    """

    __type__: Literal["fileTypePhoto"] = "fileTypePhoto"
