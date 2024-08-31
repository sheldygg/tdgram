from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageReplyTo, Message, MessageSendOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class SendInlineQueryResultMessage(BaseMethod):
    """
    Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message
    """

    __type__: Literal["sendInlineQueryResultMessage"] = "sendInlineQueryResultMessage"
    __returning_type__ = Message

    chat_id: int
    """Target chat"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the message will be sent"""
    reply_to: InputMessageReplyTo | None = None
    """Information about the message or story to be replied; pass null if none"""
    options: MessageSendOptions | None = None
    """Options to be used to send the message; pass null to use default options"""
    query_id: int
    """Identifier of the inline query"""
    result_id: str
    """Identifier of the inline query result"""
    hide_via_bot: bool
    """Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption('animation_search_bot_username'), getOption('photo_search_bot_username'), and getOption('venue_search_bot_username')"""
