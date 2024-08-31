from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageCopyOptions


@dataclass(kw_only=True)
class InputMessageForwarded(BaseType):
    """
    A forwarded message
    """

    __type__: Literal["inputMessageForwarded"] = "inputMessageForwarded"

    from_chat_id: int
    """Identifier for the chat this forwarded message came from"""
    message_id: int
    """Identifier of the message to forward. A message can be forwarded only if messageProperties.can_be_forwarded"""
    in_game_share: bool
    """True, if a game message is being shared from a launched game; applies only to game messages"""
    copy_options: MessageCopyOptions | None = None
    """Options to be used to copy content of the message without reference to the original sender; pass null to forward the message as usual"""
