from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeAudio(BaseType):
    """
    The file is an audio file
    """

    __type__: Literal["fileTypeAudio"] = "fileTypeAudio"
