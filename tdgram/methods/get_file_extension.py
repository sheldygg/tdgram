from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetFileExtension(BaseMethod):
    """
    Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously
    """

    __type__: Literal["getFileExtension"] = "getFileExtension"
    __returning_type__ = Text

    mime_type: str
    """The MIME type of the file"""
