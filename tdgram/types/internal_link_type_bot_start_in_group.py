from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAdministratorRights


@dataclass(kw_only=True)
class InternalLinkTypeBotStartInGroup(BaseType):
    """
    The link is a link to a Telegram bot, which is supposed to be added to a group chat. Call searchPublicChat with the given bot username, check that the user is a bot and can be added to groups,
    """

    __type__: Literal["internalLinkTypeBotStartInGroup"] = "internalLinkTypeBotStartInGroup"

    bot_username: str
    """Username of the bot"""
    start_parameter: str
    """The parameter to be passed to sendBotStartMessage"""
    administrator_rights: ChatAdministratorRights | None = None
    """Expected administrator rights for the bot; may be null"""
