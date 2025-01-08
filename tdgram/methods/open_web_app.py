from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageReplyTo, WebAppInfo, WebAppOpenParameters
from .base import BaseMethod


@dataclass(kw_only=True)
class OpenWebApp(BaseMethod):
    """
    Informs TDLib that a Web App is being opened from the attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button.
    """

    __type__: Literal["openWebApp"] = "openWebApp"
    __returning_type__ = WebAppInfo

    chat_id: int
    """Identifier of the chat in which the Web App is opened. The Web App can't be opened in secret chats"""
    bot_user_id: int
    """Identifier of the bot, providing the Web App"""
    url: str
    """The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the message will be sent"""
    reply_to: InputMessageReplyTo | None = None
    """Information about the message or story to be replied in the message sent by the Web App; pass null if none"""
    parameters: WebAppOpenParameters
    """Parameters to use to open the Web App"""
