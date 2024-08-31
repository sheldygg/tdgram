from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceFile(BaseType):
    """
    The file contains an error. The error will be considered resolved when the file changes
    """

    __type__: Literal["passportElementErrorSourceFile"] = "passportElementErrorSourceFile"

    file_index: int
    """Index of a file with the error"""
