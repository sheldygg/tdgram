from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetMessageFactCheck(BaseMethod):
    """
    Changes the fact-check of a message. Can be only used if messageProperties.can_set_fact_check == true
    """

    __type__: Literal["setMessageFactCheck"] = "setMessageFactCheck"
    __returning_type__ = Ok

    chat_id: int
    """The channel chat the message belongs to"""
    message_id: int
    """Identifier of the message"""
    text: FormattedText | None = None
    """New text of the fact-check; 0-getOption('fact_check_length_max') characters; pass null to remove it. Only Bold, Italic, and TextUrl entities with https://t.me/ links are supported"""
