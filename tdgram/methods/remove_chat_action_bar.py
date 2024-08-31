from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveChatActionBar(BaseMethod):
    """
    Removes a chat action bar without any other action
    """

    __type__: Literal["removeChatActionBar"] = "removeChatActionBar"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
