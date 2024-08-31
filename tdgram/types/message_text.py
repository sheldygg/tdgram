from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, LinkPreview, LinkPreviewOptions


@dataclass(kw_only=True)
class MessageText(BaseType):
    """
    A text message
    """

    __type__: Literal["messageText"] = "messageText"

    text: FormattedText
    """Text of the message"""
    link_preview: LinkPreview | None = None
    """A link preview attached to the message; may be null"""
    link_preview_options: LinkPreviewOptions | None = None
    """Options which were used for generation of the link preview; may be null if default options were used"""
