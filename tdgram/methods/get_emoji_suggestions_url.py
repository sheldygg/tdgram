from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetEmojiSuggestionsUrl(BaseMethod):
    """
    Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation
    """

    __type__: Literal["getEmojiSuggestionsUrl"] = "getEmojiSuggestionsUrl"
    __returning_type__ = HttpUrl

    language_code: str
    """Language code for which the emoji replacements will be suggested"""
