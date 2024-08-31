from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateSupergroupChat(BaseMethod):
    """
    Returns an existing chat corresponding to a known supergroup or channel
    """

    __type__: Literal["createSupergroupChat"] = "createSupergroupChat"
    __returning_type__ = Chat

    supergroup_id: int
    """Supergroup or channel identifier"""
    force: bool
    """Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect"""
