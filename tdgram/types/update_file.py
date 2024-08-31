from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File


@dataclass(kw_only=True)
class UpdateFile(BaseType):
    """
    Information about a file was updated
    """

    __type__: Literal["updateFile"] = "updateFile"

    file: File
    """New data about the file"""
