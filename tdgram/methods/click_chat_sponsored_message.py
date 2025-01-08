from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClickChatSponsoredMessage(BaseMethod):
    """
    Informs TDLib that the user opened the sponsored chat via the button, the name, the chat photo, a mention in the sponsored message text, or the media in the sponsored message
    """

    __type__: Literal["clickChatSponsoredMessage"] = "clickChatSponsoredMessage"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier of the sponsored message"""
    message_id: int
    """Identifier of the sponsored message"""
    is_media_click: bool
    """Pass true if the media was clicked in the sponsored message"""
    from_fullscreen: bool
    """Pass true if the user expanded the video from the sponsored message fullscreen before the click"""
