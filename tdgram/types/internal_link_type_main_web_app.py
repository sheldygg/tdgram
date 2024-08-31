from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeMainWebApp(BaseType):
    """
    The link is a link to the main Web App of a bot. Call searchPublicChat with the given bot username, check that the user is a bot and has the main Web App.
    """

    __type__: Literal["internalLinkTypeMainWebApp"] = "internalLinkTypeMainWebApp"

    bot_username: str
    """Username of the bot"""
    start_parameter: str
    """Start parameter to be passed to getMainWebApp"""
    is_compact: bool
    """True, if the Web App must be opened in the compact mode instead of the full-size mode"""
