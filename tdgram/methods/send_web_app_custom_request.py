from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CustomRequestResult
from .base import BaseMethod


@dataclass(kw_only=True)
class SendWebAppCustomRequest(BaseMethod):
    """
    Sends a custom request from a Web App
    """

    __type__: Literal["sendWebAppCustomRequest"] = "sendWebAppCustomRequest"
    __returning_type__ = CustomRequestResult

    bot_user_id: int
    """Identifier of the bot"""
    method: str
    """The method name"""
    parameters: str
    """JSON-serialized method parameters"""
