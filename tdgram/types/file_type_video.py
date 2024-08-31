from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeVideo(BaseType):
    """
    The file is a video
    """

    __type__: Literal["fileTypeVideo"] = "fileTypeVideo"
