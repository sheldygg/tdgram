from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageContent, MessageSponsor


@dataclass(kw_only=True)
class SponsoredMessage(BaseType):
    """
    Describes a sponsored message
    """

    __type__: Literal["sponsoredMessage"] = "sponsoredMessage"

    message_id: int
    """Message identifier; unique for the chat to which the sponsored message belongs among both ordinary and sponsored messages"""
    is_recommended: bool
    """True, if the message needs to be labeled as 'recommended' instead of 'sponsored'"""
    can_be_reported: bool
    """True, if the message can be reported to Telegram moderators through reportChatSponsoredMessage"""
    content: MessageContent
    """Content of the message. Currently, can be only of the types messageText, messageAnimation, messagePhoto, or messageVideo. Video messages can be viewed fullscreen"""
    sponsor: MessageSponsor
    """Information about the sponsor of the message"""
    title: str
    """Title of the sponsored message"""
    button_text: str
    """Text for the message action button"""
    accent_color_id: int
    """Identifier of the accent color for title, button text and message background"""
    background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the message background; 0 if none"""
    additional_info: str | None = None
    """If non-empty, additional information about the sponsored message to be shown along with the message"""
