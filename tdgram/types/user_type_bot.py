from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserTypeBot(BaseType):
    """
    A bot (see https://core.telegram.org/bots)
    """

    __type__: Literal["userTypeBot"] = "userTypeBot"

    can_be_edited: bool
    """True, if the bot is owned by the current user and can be edited using the methods toggleBotUsernameIsActive, reorderBotActiveUsernames, setBotProfilePhoto, setBotName, setBotInfoDescription, and setBotInfoShortDescription"""
    can_join_groups: bool
    """True, if the bot can be invited to basic group and supergroup chats"""
    can_read_all_group_messages: bool
    """True, if the bot can read all messages in basic group or supergroup chats and not just those addressed to the bot. In private and channel chats a bot can always read all messages"""
    has_main_web_app: bool
    """True, if the bot has the main Web App"""
    is_inline: bool
    """True, if the bot supports inline queries"""
    inline_query_placeholder: str
    """Placeholder for inline queries (displayed on the application input field)"""
    need_location: bool
    """True, if the location of the user is expected to be sent with every inline query to this bot"""
    can_connect_to_business: bool
    """True, if the bot supports connection to Telegram Business accounts"""
    can_be_added_to_attachment_menu: bool
    """True, if the bot can be added to attachment or side menu"""
    active_user_count: int
    """The number of recently active users of the bot"""
