from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class InputBusinessChatLink(BaseType):
    """
    Describes a business chat link to create or edit
    """

    __type__: Literal["inputBusinessChatLink"] = "inputBusinessChatLink"

    text: FormattedText
    """Message draft text that will be added to the input field"""
    title: str
    """Link title"""
