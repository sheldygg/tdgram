from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeSelfDestructingVideoNote(BaseType):
    """
    The file is a self-destructing video note in a private chat
    """

    __type__: Literal["fileTypeSelfDestructingVideoNote"] = "fileTypeSelfDestructingVideoNote"
