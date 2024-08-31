from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPosition, DraftMessage


@dataclass(kw_only=True)
class UpdateChatDraftMessage(BaseType):
    """
    A chat draft has changed. Be aware that the update may come in the currently opened chat but with old content of the draft. If the user has changed the content of the draft, this update mustn't be applied
    """

    __type__: Literal["updateChatDraftMessage"] = "updateChatDraftMessage"

    chat_id: int
    """Chat identifier"""
    draft_message: DraftMessage | None = None
    """The new draft message; may be null if none"""
    positions: list[ChatPosition]
    """The new chat positions in the chat lists"""
