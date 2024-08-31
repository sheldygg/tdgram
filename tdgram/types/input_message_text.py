from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, LinkPreviewOptions


@dataclass(kw_only=True)
class InputMessageText(BaseType):
    """
    A text message
    """

    __type__: Literal["inputMessageText"] = "inputMessageText"

    text: FormattedText
    """Formatted text to be sent; 0-getOption('message_text_length_max') characters. Only Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, BlockQuote, ExpandableBlockQuote,"""
    link_preview_options: LinkPreviewOptions | None = None
    """Options to be used for generation of a link preview; may be null if none; pass null to use default link preview options"""
    clear_draft: bool
    """True, if a chat message draft must be deleted"""
