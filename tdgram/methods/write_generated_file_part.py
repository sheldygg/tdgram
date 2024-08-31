from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class WriteGeneratedFilePart(BaseMethod):
    """
    Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file
    """

    __type__: Literal["writeGeneratedFilePart"] = "writeGeneratedFilePart"
    __returning_type__ = Ok

    generation_id: int
    """The identifier of the generation process"""
    offset: int
    """The offset from which to write the data to the file"""
    data: bytes
    """The data to write"""
