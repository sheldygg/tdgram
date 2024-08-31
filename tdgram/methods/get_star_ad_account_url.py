from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl, MessageSender
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarAdAccountUrl(BaseMethod):
    """
    Returns a URL for a Telegram Ad platform account that can be used to set up advertisements for the chat paid in the owned Telegram Stars
    """

    __type__: Literal["getStarAdAccountUrl"] = "getStarAdAccountUrl"
    __returning_type__ = HttpUrl

    owner_id: MessageSender
    """Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat"""
