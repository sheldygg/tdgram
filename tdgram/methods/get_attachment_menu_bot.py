from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AttachmentMenuBot
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAttachmentMenuBot(BaseMethod):
    """
    Returns information about a bot that can be added to attachment or side menu
    """

    __type__: Literal["getAttachmentMenuBot"] = "getAttachmentMenuBot"
    __returning_type__ = AttachmentMenuBot

    bot_user_id: int
    """Bot's user identifier"""
