from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateBasicGroupChat(BaseMethod):
    """
    Returns an existing chat corresponding to a known basic group
    """

    __type__: Literal["createBasicGroupChat"] = "createBasicGroupChat"
    __returning_type__ = Chat

    basic_group_id: int
    """Basic group identifier"""
    force: bool
    """Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect"""
