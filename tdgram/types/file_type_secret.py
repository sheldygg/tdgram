from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeSecret(BaseType):
    """
    The file was sent to a secret chat (the file type is not known to the server)
    """

    __type__: Literal["fileTypeSecret"] = "fileTypeSecret"
