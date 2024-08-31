from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAction, MessageSender


@dataclass(kw_only=True)
class UpdateChatAction(BaseType):
    """
    A message sender activity in the chat has changed
    """

    __type__: Literal["updateChatAction"] = "updateChatAction"

    chat_id: int
    """Chat identifier"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the action was performed"""
    sender_id: MessageSender
    """Identifier of a message sender performing the action"""
    action: ChatAction
    """The action"""
