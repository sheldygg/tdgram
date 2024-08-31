from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessChatLink, InputBusinessChatLink
from .base import BaseMethod


@dataclass(kw_only=True)
class EditBusinessChatLink(BaseMethod):
    """
    Edits a business chat link of the current account. Requires Telegram Business subscription. Returns the edited link
    """

    __type__: Literal["editBusinessChatLink"] = "editBusinessChatLink"
    __returning_type__ = BusinessChatLink

    link: str
    """The link to edit"""
    link_info: InputBusinessChatLink
    """New description of the link"""
