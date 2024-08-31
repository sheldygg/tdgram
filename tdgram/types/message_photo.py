from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, Photo


@dataclass(kw_only=True)
class MessagePhoto(BaseType):
    """
    A photo message
    """

    __type__: Literal["messagePhoto"] = "messagePhoto"

    photo: Photo
    """The photo"""
    caption: FormattedText
    """Photo caption"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the photo; otherwise, the caption must be shown below the photo"""
    has_spoiler: bool
    """True, if the photo preview must be covered by a spoiler animation"""
    is_secret: bool
    """True, if the photo must be blurred and must be shown only while tapped"""
