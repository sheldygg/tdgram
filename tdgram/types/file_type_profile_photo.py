from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeProfilePhoto(BaseType):
    """
    The file is a profile photo
    """

    __type__: Literal["fileTypeProfilePhoto"] = "fileTypeProfilePhoto"
