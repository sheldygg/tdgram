from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeSecretThumbnail(BaseType):
    """
    The file is a thumbnail of a file from a secret chat
    """

    __type__: Literal["fileTypeSecretThumbnail"] = "fileTypeSecretThumbnail"
