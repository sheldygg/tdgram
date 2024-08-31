from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


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
    is_compact: bool
    """True, if the Web App must be opened in the compact mode instead of the full-size mode"""
