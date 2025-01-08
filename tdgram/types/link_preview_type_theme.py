from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Document, ThemeSettings


@dataclass(kw_only=True)
class LinkPreviewTypeTheme(BaseType):
    """
    The link is a link to a cloud theme. TDLib has no theme support yet
    """

    __type__: Literal["linkPreviewTypeTheme"] = "linkPreviewTypeTheme"

    documents: list[Document]
    """The list of files with theme description"""
    settings: ThemeSettings | None = None
    """Settings for the cloud theme; may be null if unknown"""
