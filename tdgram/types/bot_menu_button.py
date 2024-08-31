from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotMenuButton(BaseType):
    """
    Describes a button to be shown instead of bot commands menu button
    """

    __type__: Literal["botMenuButton"] = "botMenuButton"

    text: str
    """Text of the button"""
    url: str
    """URL of a Web App to open when the button is pressed. If the link is of the type internalLinkTypeWebApp, then it must be processed accordingly. Otherwise, the link must be passed to openWebApp"""
