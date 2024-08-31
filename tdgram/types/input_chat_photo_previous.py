from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputChatPhotoPrevious(BaseType):
    """
    A previously used profile photo of the current user
    """

    __type__: Literal["inputChatPhotoPrevious"] = "inputChatPhotoPrevious"

    chat_photo_id: int
    """Identifier of the current user's profile photo to reuse"""
