from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class ChatFolderName(BaseType):
    """
    Describes name of a chat folder
    """

    __type__: Literal["chatFolderName"] = "chatFolderName"

    text: FormattedText
    """The text of the chat folder name; 1-12 characters without line feeds. May contain only CustomEmoji entities"""
    animate_custom_emoji: bool
    """True, if custom emoji in the name must be animated"""
