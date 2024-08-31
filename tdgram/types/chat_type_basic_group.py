from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatTypeBasicGroup(BaseType):
    """
    A basic group (a chat with 0-200 other users)
    """

    __type__: Literal["chatTypeBasicGroup"] = "chatTypeBasicGroup"

    basic_group_id: int
    """Basic group identifier"""
