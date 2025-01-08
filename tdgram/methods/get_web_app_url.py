from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl, WebAppOpenParameters
from .base import BaseMethod


@dataclass(kw_only=True)
class GetWebAppUrl(BaseMethod):
    """
    Returns an HTTPS URL of a Web App to open from the side menu, a keyboardButtonTypeWebApp button, or an inlineQueryResultsButtonTypeWebApp button
    """

    __type__: Literal["getWebAppUrl"] = "getWebAppUrl"
    __returning_type__ = HttpUrl

    bot_user_id: int
    """Identifier of the target bot"""
    url: str
    """The URL from a keyboardButtonTypeWebApp button, inlineQueryResultsButtonTypeWebApp button, or an empty string when the bot is opened from the side menu"""
    parameters: WebAppOpenParameters
    """Parameters to use to open the Web App"""
