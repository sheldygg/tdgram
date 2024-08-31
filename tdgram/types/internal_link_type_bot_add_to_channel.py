from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAdministratorRights


@dataclass(kw_only=True)
class InternalLinkTypeBotAddToChannel(BaseType):
    """
    The link is a link to a Telegram bot, which is supposed to be added to a channel chat as an administrator. Call searchPublicChat with the given bot username and check that the user is a bot,
    """

    __type__: Literal["internalLinkTypeBotAddToChannel"] = "internalLinkTypeBotAddToChannel"

    bot_username: str
    """Username of the bot"""
    administrator_rights: ChatAdministratorRights
    """Expected administrator rights for the bot"""
