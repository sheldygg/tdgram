from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeDocument(BaseType):
    """
    The file is a document
    """

    __type__: Literal["fileTypeDocument"] = "fileTypeDocument"
