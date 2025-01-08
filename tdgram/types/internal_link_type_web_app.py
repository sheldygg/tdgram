from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import WebAppOpenMode


@dataclass(kw_only=True)
class InternalLinkTypeWebApp(BaseType):
    """
    The link is a link to a Web App. Call searchPublicChat with the given bot username, check that the user is a bot, then call searchWebApp with the received bot and the given web_app_short_name.
    """

    __type__: Literal["internalLinkTypeWebApp"] = "internalLinkTypeWebApp"

    bot_username: str
    """Username of the bot that owns the Web App"""
    web_app_short_name: str
    """Short name of the Web App"""
    start_parameter: str
    """Start parameter to be passed to getWebAppLinkUrl"""
    mode: WebAppOpenMode
    """The mode in which the Web App must be opened"""
