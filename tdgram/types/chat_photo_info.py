from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail


@dataclass(kw_only=True)
class ChatPhotoInfo(BaseType):
    """
    Contains basic information about the photo of a chat
    """

    __type__: Literal["chatPhotoInfo"] = "chatPhotoInfo"

    small: File
    """A small (160x160) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed"""
    big: File
    """A big (640x640) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed"""
    minithumbnail: Minithumbnail | None = None
    """Chat photo minithumbnail; may be null"""
    has_animation: bool
    """True, if the photo has animated variant"""
    is_personal: bool
    """True, if the photo is visible only for the current user"""
