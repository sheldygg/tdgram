from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BotMediaPreview


@dataclass(kw_only=True)
class BotMediaPreviews(BaseType):
    """
    Contains a list of media previews of a bot
    """

    __type__: Literal["botMediaPreviews"] = "botMediaPreviews"

    previews: list[BotMediaPreview]
    """List of media previews"""
