from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AttachmentMenuBotColor, File


@dataclass(kw_only=True)
class AttachmentMenuBot(BaseType):
    """
    Represents a bot, which can be added to attachment or side menu
    """

    __type__: Literal["attachmentMenuBot"] = "attachmentMenuBot"

    bot_user_id: int
    """User identifier of the bot"""
    supports_self_chat: bool
    """True, if the bot supports opening from attachment menu in the chat with the bot"""
    supports_user_chats: bool
    """True, if the bot supports opening from attachment menu in private chats with ordinary users"""
    supports_bot_chats: bool
    """True, if the bot supports opening from attachment menu in private chats with other bots"""
    supports_group_chats: bool
    """True, if the bot supports opening from attachment menu in basic group and supergroup chats"""
    supports_channel_chats: bool
    """True, if the bot supports opening from attachment menu in channel chats"""
    request_write_access: bool
    """True, if the user must be asked for the permission to send messages to the bot"""
    is_added: bool
    """True, if the bot was explicitly added by the user. If the bot isn't added, then on the first bot launch toggleBotIsAddedToAttachmentMenu must be called and the bot must be added or removed"""
    show_in_attachment_menu: bool
    """True, if the bot must be shown in the attachment menu"""
    show_in_side_menu: bool
    """True, if the bot must be shown in the side menu"""
    show_disclaimer_in_side_menu: bool
    """True, if a disclaimer, why the bot is shown in the side menu, is needed"""
    name: str
    """Name for the bot in attachment menu"""
    name_color: AttachmentMenuBotColor | None = None
    """Color to highlight selected name of the bot if appropriate; may be null"""
    default_icon: File | None = None
    """Default icon for the bot in SVG format; may be null"""
    ios_static_icon: File | None = None
    """Icon for the bot in SVG format for the official iOS app; may be null"""
    ios_animated_icon: File | None = None
    """Icon for the bot in TGS format for the official iOS app; may be null"""
    ios_side_menu_icon: File | None = None
    """Icon for the bot in PNG format for the official iOS app side menu; may be null"""
    android_icon: File | None = None
    """Icon for the bot in TGS format for the official Android app; may be null"""
    android_side_menu_icon: File | None = None
    """Icon for the bot in SVG format for the official Android app side menu; may be null"""
    macos_icon: File | None = None
    """Icon for the bot in TGS format for the official native macOS app; may be null"""
    macos_side_menu_icon: File | None = None
    """Icon for the bot in PNG format for the official macOS app side menu; may be null"""
    icon_color: AttachmentMenuBotColor | None = None
    """Color to highlight selected icon of the bot if appropriate; may be null"""
    web_app_placeholder: File | None = None
    """Default placeholder for opened Web Apps in SVG format; may be null"""
