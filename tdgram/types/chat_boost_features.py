from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBoostLevelFeatures


@dataclass(kw_only=True)
class ChatBoostFeatures(BaseType):
    """
    Contains a list of features available on the first chat boost levels
    """

    __type__: Literal["chatBoostFeatures"] = "chatBoostFeatures"

    features: list[ChatBoostLevelFeatures]
    """The list of features"""
    min_profile_background_custom_emoji_boost_level: int
    """The minimum boost level required to set custom emoji for profile background"""
    min_background_custom_emoji_boost_level: int
    """The minimum boost level required to set custom emoji for reply header and link preview background; for channel chats only"""
    min_emoji_status_boost_level: int
    """The minimum boost level required to set emoji status"""
    min_chat_theme_background_boost_level: int
    """The minimum boost level required to set a chat theme background as chat background"""
    min_custom_background_boost_level: int
    """The minimum boost level required to set custom chat background"""
    min_custom_emoji_sticker_set_boost_level: int
    """The minimum boost level required to set custom emoji sticker set for the chat; for supergroup chats only"""
    min_speech_recognition_boost_level: int
    """The minimum boost level allowing to recognize speech in video note and voice note messages for non-Premium users; for supergroup chats only"""
    min_sponsored_message_disable_boost_level: int
    """The minimum boost level allowing to disable sponsored messages in the chat; for channel chats only"""
