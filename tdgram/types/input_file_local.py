from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputFileLocal(BaseType):
    """
    A file defined by a local path
    """

    __type__: Literal["inputFileLocal"] = "inputFileLocal"

    path: str
    """Local path to the file"""
