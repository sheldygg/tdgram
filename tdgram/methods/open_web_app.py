from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageReplyTo, ThemeParameters, WebAppInfo
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
    theme: ThemeParameters | None = None
    """Preferred Web App theme; pass null to use the default theme"""
    application_name: str
    """Short name of the current application; 0-64 English letters, digits, and underscores"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the message will be sent"""
    reply_to: InputMessageReplyTo | None = None
    """Information about the message or story to be replied in the message sent by the Web App; pass null if none"""
