from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhotoInfo


@dataclass(kw_only=True)
class UpdateChatPhoto(BaseType):
    """
    A chat photo was changed
    """

    __type__: Literal["updateChatPhoto"] = "updateChatPhoto"

    chat_id: int
    """Chat identifier"""
    photo: ChatPhotoInfo | None = None
    """The new chat photo; may be null"""
