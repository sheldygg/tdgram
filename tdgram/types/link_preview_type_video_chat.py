from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class LinkPreviewTypeVideoChat(BaseType):
    """
    The link is a link to a video chat
    """

    __type__: Literal["linkPreviewTypeVideoChat"] = "linkPreviewTypeVideoChat"

    photo: ChatPhoto | None = None
    """Photo of the chat with the video chat; may be null if none"""
    is_live_stream: bool
    """True, if the video chat is expected to be a live stream in a channel or a broadcast group"""
