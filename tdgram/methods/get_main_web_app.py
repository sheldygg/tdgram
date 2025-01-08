from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MainWebApp, WebAppOpenParameters
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMainWebApp(BaseMethod):
    """
    Returns information needed to open the main Web App of a bot
    """

    __type__: Literal["getMainWebApp"] = "getMainWebApp"
    __returning_type__ = MainWebApp

    chat_id: int
    """Identifier of the chat in which the Web App is opened; pass 0 if none"""
    bot_user_id: int
    """Identifier of the target bot"""
    start_parameter: str
    """Start parameter from internalLinkTypeMainWebApp"""
    parameters: WebAppOpenParameters
    """Parameters to use to open the Web App"""
