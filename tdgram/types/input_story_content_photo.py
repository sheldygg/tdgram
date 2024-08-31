from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputStoryContentPhoto(BaseType):
    """
    A photo story
    """

    __type__: Literal["inputStoryContentPhoto"] = "inputStoryContentPhoto"

    photo: InputFile
    """Photo to send. The photo must be at most 10 MB in size. The photo size must be 1080x1920"""
    added_sticker_file_ids: list[int]
    """File identifiers of the stickers added to the photo, if applicable"""
