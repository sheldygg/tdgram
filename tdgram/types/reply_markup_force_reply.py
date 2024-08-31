from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReplyMarkupForceReply(BaseType):
    """
    Instructs application to force a reply to this message
    """

    __type__: Literal["replyMarkupForceReply"] = "replyMarkupForceReply"

    is_personal: bool
    """True, if a forced reply must automatically be shown to the current user. For outgoing messages, specify true to show the forced reply only for the mentioned users and for the target user of a reply"""
    input_field_placeholder: str | None = None
    """If non-empty, the placeholder to be shown in the input field when the reply is active; 0-64 characters"""
