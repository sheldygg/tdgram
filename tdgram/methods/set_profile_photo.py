from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputChatPhoto, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetProfilePhoto(BaseMethod):
    """
    Changes a profile photo for the current user
    """

    __type__: Literal["setProfilePhoto"] = "setProfilePhoto"
    __returning_type__ = Ok

    photo: InputChatPhoto
    """Profile photo to set"""
    is_public: bool
    """Pass true to set a public photo, which will be visible even the main photo is hidden by privacy settings"""
