from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetFileMimeType(BaseMethod):
    """
    Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously
    """

    __type__: Literal["getFileMimeType"] = "getFileMimeType"
    __returning_type__ = Text

    file_name: str
    """The name of the file or path to the file"""
