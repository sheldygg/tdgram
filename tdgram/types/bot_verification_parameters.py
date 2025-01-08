from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class BotVerificationParameters(BaseType):
    """
    Describes parameters of verification that is provided by a bot
    """

    __type__: Literal["botVerificationParameters"] = "botVerificationParameters"

    icon_custom_emoji_id: int
    """Identifier of the custom emoji that is used as the verification sign"""
    organization_name: str
    """Name of the organization that provides verification"""
    default_custom_description: FormattedText | None = None
    """Default custom description of verification reason to be used as placeholder in setMessageSenderBotVerification; may be null if none"""
    can_set_custom_description: bool
    """True, if the bot is allowed to provide custom description for verified entities"""
