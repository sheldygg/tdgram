from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File


@dataclass(kw_only=True)
class DatedFile(BaseType):
    """
    File with the date it was uploaded
    """

    __type__: Literal["datedFile"] = "datedFile"

    file: File
    """The file"""
    date: int
    """Point in time (Unix timestamp) when the file was uploaded"""
