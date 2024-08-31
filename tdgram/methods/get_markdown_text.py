from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMarkdownText(BaseMethod):
    """
    Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously
    """

    __type__: Literal["getMarkdownText"] = "getMarkdownText"
    __returning_type__ = FormattedText

    text: FormattedText
    """The text"""
