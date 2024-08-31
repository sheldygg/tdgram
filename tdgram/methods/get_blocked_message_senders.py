from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BlockList, MessageSenders
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBlockedMessageSenders(BaseMethod):
    """
    Returns users and chats that were blocked by the current user
    """

    __type__: Literal["getBlockedMessageSenders"] = "getBlockedMessageSenders"
    __returning_type__ = MessageSenders

    block_list: BlockList
    """Block list from which to return users"""
    offset: int
    """Number of users and chats to skip in the result; must be non-negative"""
    limit: int
    """The maximum number of users and chats to return; up to 100"""
