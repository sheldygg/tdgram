from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import WebAppOpenMode


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
    mode: WebAppOpenMode
    """The mode to be passed to getMainWebApp"""
