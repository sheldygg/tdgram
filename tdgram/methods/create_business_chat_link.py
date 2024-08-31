from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessChatLink, InputBusinessChatLink
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateBusinessChatLink(BaseMethod):
    """
    Creates a business chat link for the current account. Requires Telegram Business subscription. There can be up to getOption('business_chat_link_count_max') links created. Returns the created link
    """

    __type__: Literal["createBusinessChatLink"] = "createBusinessChatLink"
    __returning_type__ = BusinessChatLink

    link_info: InputBusinessChatLink
    """Information about the link to create"""
