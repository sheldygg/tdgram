from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class CleanFileName(BaseMethod):
    """
    Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. Can be called synchronously
    """

    __type__: Literal["cleanFileName"] = "cleanFileName"
    __returning_type__ = Text

    file_name: str
    """File name or path to the file"""
