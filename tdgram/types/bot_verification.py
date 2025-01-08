from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class BotVerification(BaseType):
    """
    Describes verification status provided by a bot
    """

    __type__: Literal["botVerification"] = "botVerification"

    bot_user_id: int
    """Identifier of the bot that provided the verification"""
    icon_custom_emoji_id: int
    """Identifier of the custom emoji that is used as the verification sign"""
    custom_description: FormattedText
    """Custom description of verification reason set by the bot"""
