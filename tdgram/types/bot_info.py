from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        Animation,
        BotCommand,
        BotMenuButton,
        ChatAdministratorRights,
        InternalLinkType,
        Photo,
    )


@dataclass(kw_only=True)
class BotInfo(BaseType):
    """
    Contains information about a bot
    """

    __type__: Literal["botInfo"] = "botInfo"

    short_description: str
    """The text that is shown on the bot's profile page and is sent together with the link when users share the bot"""
    description: str
    """The text shown in the chat with the bot if the chat is empty"""
    photo: Photo | None = None
    """Photo shown in the chat with the bot if the chat is empty; may be null"""
    animation: Animation | None = None
    """Animation shown in the chat with the bot if the chat is empty; may be null"""
    menu_button: BotMenuButton | None = None
    """Information about a button to show instead of the bot commands menu button; may be null if ordinary bot commands menu must be shown"""
    commands: list[BotCommand]
    """List of the bot commands"""
    privacy_policy_url: str
    """The HTTP link to the privacy policy of the bot. If empty, then /privacy command must be used if supported by the bot. If the command isn't supported, then https://telegram.org/privacy-tpa must be opened"""
    default_group_administrator_rights: ChatAdministratorRights | None = None
    """Default administrator rights for adding the bot to basic group and supergroup chats; may be null"""
    default_channel_administrator_rights: ChatAdministratorRights | None = None
    """Default administrator rights for adding the bot to channels; may be null"""
    has_media_previews: bool
    """True, if the bot has media previews"""
    edit_commands_link: InternalLinkType | None = None
    """The internal link, which can be used to edit bot commands; may be null"""
    edit_description_link: InternalLinkType | None = None
    """The internal link, which can be used to edit bot description; may be null"""
    edit_description_media_link: InternalLinkType | None = None
    """The internal link, which can be used to edit the photo or animation shown in the chat with the bot if the chat is empty; may be null"""
    edit_settings_link: InternalLinkType | None = None
    """The internal link, which can be used to edit bot settings; may be null"""
