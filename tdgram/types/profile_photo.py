from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail


@dataclass(kw_only=True)
class ProfilePhoto(BaseType):
    """
    Describes a user profile photo
    """

    __type__: Literal["profilePhoto"] = "profilePhoto"

    id: int
    """Photo identifier; 0 for an empty photo. Can be used to find a photo in a list of user profile photos"""
    small: File
    """A small (160x160) user profile photo. The file can be downloaded only before the photo is changed"""
    big: File
    """A big (640x640) user profile photo. The file can be downloaded only before the photo is changed"""
    minithumbnail: Minithumbnail | None = None
    """User profile photo minithumbnail; may be null"""
    has_animation: bool
    """True, if the photo has animated variant"""
    is_personal: bool
    """True, if the photo is visible only for the current user"""
