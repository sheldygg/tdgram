from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BlockList, MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetMessageSenderBlockList(BaseMethod):
    """
    Changes the block list of a message sender. Currently, only users and supergroup chats can be blocked
    """

    __type__: Literal["setMessageSenderBlockList"] = "setMessageSenderBlockList"
    __returning_type__ = Ok

    sender_id: MessageSender
    """Identifier of a message sender to block/unblock"""
    block_list: BlockList | None = None
    """New block list for the message sender; pass null to unblock the message sender"""
