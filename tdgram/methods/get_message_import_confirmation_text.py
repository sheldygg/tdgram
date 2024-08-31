from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageImportConfirmationText(BaseMethod):
    """
    Returns a confirmation text to be shown to the user before starting message import
    """

    __type__: Literal["getMessageImportConfirmationText"] = "getMessageImportConfirmationText"
    __returning_type__ = Text

    chat_id: int
    """Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info member right"""
