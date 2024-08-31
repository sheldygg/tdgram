from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatBoostLevelFeatures(BaseType):
    """
    Contains a list of features available on a specific chat boost level
    """

    __type__: Literal["chatBoostLevelFeatures"] = "chatBoostLevelFeatures"

    level: int
    """Target chat boost level"""
    story_per_day_count: int
    """Number of stories that the chat can publish daily"""
    custom_emoji_reaction_count: int
    """Number of custom emoji reactions that can be added to the list of available reactions"""
    title_color_count: int
    """Number of custom colors for chat title"""
    profile_accent_color_count: int
    """Number of custom colors for profile photo background"""
    can_set_profile_background_custom_emoji: bool
    """True, if custom emoji for profile background can be set"""
    accent_color_count: int
    """Number of custom colors for background of empty chat photo, replies to messages and link previews"""
    can_set_background_custom_emoji: bool
    """True, if custom emoji for reply header and link preview background can be set"""
    can_set_emoji_status: bool
    """True, if emoji status can be set"""
    chat_theme_background_count: int
    """Number of chat theme backgrounds that can be set as chat background"""
    can_set_custom_background: bool
    """True, if custom background can be set in the chat for all users"""
    can_set_custom_emoji_sticker_set: bool
    """True, if custom emoji sticker set can be set for the chat"""
    can_recognize_speech: bool
    """True, if speech recognition can be used for video note and voice note messages by all users"""
    can_disable_sponsored_messages: bool
    """True, if sponsored messages can be disabled in the chat"""
