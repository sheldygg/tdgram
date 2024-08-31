from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BotMediaPreview


@dataclass(kw_only=True)
class BotMediaPreviewInfo(BaseType):
    """
    Contains a list of media previews of a bot for the given language and the list of languages for which the bot has dedicated previews
    """

    __type__: Literal["botMediaPreviewInfo"] = "botMediaPreviewInfo"

    previews: list[BotMediaPreview]
    """List of media previews"""
    language_codes: list[str]
    """List of language codes for which the bot has dedicated previews"""
