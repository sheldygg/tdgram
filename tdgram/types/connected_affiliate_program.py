from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AffiliateProgramParameters


@dataclass(kw_only=True)
class ConnectedAffiliateProgram(BaseType):
    """
    Describes an affiliate program that was connected to an affiliate
    """

    __type__: Literal["connectedAffiliateProgram"] = "connectedAffiliateProgram"

    url: str
    """The link that can be used to refer users if the program is still active"""
    bot_user_id: int
    """User identifier of the bot created the program"""
    parameters: AffiliateProgramParameters
    """The parameters of the affiliate program"""
    connection_date: int
    """Point in time (Unix timestamp) when the affiliate program was connected"""
    is_disconnected: bool
    """True, if the program was canceled by the bot, or disconnected by the chat owner and isn't available anymore"""
    user_count: int
    """The number of users that used the affiliate program"""
    revenue_star_count: int
    """The number of Telegram Stars that were earned by the affiliate program"""
