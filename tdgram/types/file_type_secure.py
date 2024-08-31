from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeSecure(BaseType):
    """
    The file is a file from Secure storage used for storing Telegram Passport files
    """

    __type__: Literal["fileTypeSecure"] = "fileTypeSecure"
