from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputFileId(BaseType):
    """
    A file defined by its unique identifier
    """

    __type__: Literal["inputFileId"] = "inputFileId"

    id: int
    """Unique file identifier"""
