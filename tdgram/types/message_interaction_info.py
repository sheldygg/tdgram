from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageReactions, MessageReplyInfo


@dataclass(kw_only=True)
class MessageInteractionInfo(BaseType):
    """
    Contains information about interactions with a message
    """

    __type__: Literal["messageInteractionInfo"] = "messageInteractionInfo"

    view_count: int
    """Number of times the message was viewed"""
    forward_count: int
    """Number of times the message was forwarded"""
    reply_info: MessageReplyInfo | None = None
    """Information about direct or indirect replies to the message; may be null. Currently, available only in channels with a discussion supergroup and discussion supergroups for messages, which are not replies itself"""
    reactions: MessageReactions | None = None
    """The list of reactions or tags added to the message; may be null"""
