from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputChatPhoto, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SuggestUserProfilePhoto(BaseMethod):
    """
    Suggests a profile photo to another regular user with common messages
    """

    __type__: Literal["suggestUserProfilePhoto"] = "suggestUserProfilePhoto"
    __returning_type__ = Ok

    user_id: int
    """User identifier"""
    photo: InputChatPhoto
    """Profile photo to suggest; inputChatPhotoPrevious isn't supported in this function"""
