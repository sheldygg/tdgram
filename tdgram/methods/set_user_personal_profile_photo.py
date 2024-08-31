from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputChatPhoto, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetUserPersonalProfilePhoto(BaseMethod):
    """
    Changes a personal profile photo of a contact user
    """

    __type__: Literal["setUserPersonalProfilePhoto"] = "setUserPersonalProfilePhoto"
    __returning_type__ = Ok

    user_id: int
    """User identifier"""
    photo: InputChatPhoto | None = None
    """Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function"""
