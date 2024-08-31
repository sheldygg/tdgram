from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeVoiceNote(BaseType):
    """
    The file is a voice note
    """

    __type__: Literal["fileTypeVoiceNote"] = "fileTypeVoiceNote"
