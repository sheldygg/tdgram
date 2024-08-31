from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeVideoStory(BaseType):
    """
    The file is a video published as a story
    """

    __type__: Literal["fileTypeVideoStory"] = "fileTypeVideoStory"
