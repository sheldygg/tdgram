from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TextEntities
from .base import BaseMethod


@dataclass(kw_only=True)
class GetTextEntities(BaseMethod):
    """
    Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) found in the text. Can be called synchronously
    """

    __type__: Literal["getTextEntities"] = "getTextEntities"
    __returning_type__ = TextEntities

    text: str
    """The text in which to look for entities"""
