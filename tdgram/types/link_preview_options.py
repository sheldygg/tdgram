from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewOptions(BaseType):
    """
    Options to be used for generation of a link preview
    """

    __type__: Literal["linkPreviewOptions"] = "linkPreviewOptions"

    is_disabled: bool
    """True, if link preview must be disabled"""
    url: str
    """URL to use for link preview. If empty, then the first URL found in the message text will be used"""
    force_small_media: bool
    """True, if shown media preview must be small; ignored in secret chats or if the URL isn't explicitly specified"""
    force_large_media: bool
    """True, if shown media preview must be large; ignored in secret chats or if the URL isn't explicitly specified"""
    show_above_text: bool
    """True, if link preview must be shown above message text; otherwise, the link preview will be shown below the message text; ignored in secret chats"""
