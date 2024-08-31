from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputBackgroundLocal(BaseType):
    """
    A background from a local file
    """

    __type__: Literal["inputBackgroundLocal"] = "inputBackgroundLocal"

    background: InputFile
    """Background file to use. Only inputFileLocal and inputFileGenerated are supported. The file must be in JPEG format for wallpapers and in PNG format for patterns"""
