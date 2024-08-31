from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FilePart(BaseType):
    """
    Contains a part of a file
    """

    __type__: Literal["filePart"] = "filePart"

    data: bytes
    """File bytes"""
