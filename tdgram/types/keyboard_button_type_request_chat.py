from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAdministratorRights


@dataclass(kw_only=True)
class KeyboardButtonTypeRequestChat(BaseType):
    """
    A button that requests a chat to be shared by the current user; available only in private chats. Use the method shareChatWithBot to complete the request
    """

    __type__: Literal["keyboardButtonTypeRequestChat"] = "keyboardButtonTypeRequestChat"

    id: int
    """Unique button identifier"""
    chat_is_channel: bool
    """True, if the chat must be a channel; otherwise, a basic group or a supergroup chat is shared"""
    restrict_chat_is_forum: bool
    """True, if the chat must or must not be a forum supergroup"""
    chat_is_forum: bool
    """True, if the chat must be a forum supergroup; otherwise, the chat must not be a forum supergroup. Ignored if restrict_chat_is_forum is false"""
    restrict_chat_has_username: bool
    """True, if the chat must or must not have a username"""
    chat_has_username: bool
    """True, if the chat must have a username; otherwise, the chat must not have a username. Ignored if restrict_chat_has_username is false"""
    chat_is_created: bool
    """True, if the chat must be created by the current user"""
    user_administrator_rights: ChatAdministratorRights | None = None
    """Expected user administrator rights in the chat; may be null if they aren't restricted"""
    bot_administrator_rights: ChatAdministratorRights | None = None
    """Expected bot administrator rights in the chat; may be null if they aren't restricted"""
    bot_is_member: bool
    """True, if the bot must be a member of the chat; for basic group and supergroup chats only"""
    request_title: bool
    """Pass true to request title of the chat; bots only"""
    request_username: bool
    """Pass true to request username of the chat; bots only"""
    request_photo: bool
    """Pass true to request photo of the chat; bots only"""
