from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeSelfDestructingPhoto(BaseType):
    """
    The file is a self-destructing photo in a private chat
    """

    __type__: Literal["fileTypeSelfDestructingPhoto"] = "fileTypeSelfDestructingPhoto"
