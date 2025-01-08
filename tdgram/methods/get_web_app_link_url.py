from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl, WebAppOpenParameters
from .base import BaseMethod


@dataclass(kw_only=True)
class GetWebAppLinkUrl(BaseMethod):
    """
    Returns an HTTPS URL of a Web App to open after a link of the type internalLinkTypeWebApp is clicked
    """

    __type__: Literal["getWebAppLinkUrl"] = "getWebAppLinkUrl"
    __returning_type__ = HttpUrl

    chat_id: int
    """Identifier of the chat in which the link was clicked; pass 0 if none"""
    bot_user_id: int
    """Identifier of the target bot"""
    web_app_short_name: str
    """Short name of the Web App"""
    start_parameter: str
    """Start parameter from internalLinkTypeWebApp"""
    allow_write_access: bool
    """Pass true if the current user allowed the bot to send them messages"""
    parameters: WebAppOpenParameters
    """Parameters to use to open the Web App"""
