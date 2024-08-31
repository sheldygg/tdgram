from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class MessageSuggestProfilePhoto(BaseType):
    """
    A profile photo was suggested to a user in a private chat
    """

    __type__: Literal["messageSuggestProfilePhoto"] = "messageSuggestProfilePhoto"

    photo: ChatPhoto
    """The suggested chat photo. Use the method setProfilePhoto with inputChatPhotoPrevious to apply the photo"""
