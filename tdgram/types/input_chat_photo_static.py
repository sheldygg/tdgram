from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputChatPhotoStatic(BaseType):
    """
    A static photo in JPEG format
    """

    __type__: Literal["inputChatPhotoStatic"] = "inputChatPhotoStatic"

    photo: InputFile
    """Photo to be set as profile photo. Only inputFileLocal and inputFileGenerated are allowed"""
