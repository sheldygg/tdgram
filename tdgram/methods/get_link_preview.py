from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, LinkPreview, LinkPreviewOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLinkPreview(BaseMethod):
    """
    Returns a link preview by the text of a message. Do not call this function too often. Returns a 404 error if the text has no link preview
    """

    __type__: Literal["getLinkPreview"] = "getLinkPreview"
    __returning_type__ = LinkPreview

    text: FormattedText
    """Message text with formatting"""
    link_preview_options: LinkPreviewOptions | None = None
    """Options to be used for generation of the link preview; pass null to use default link preview options"""
