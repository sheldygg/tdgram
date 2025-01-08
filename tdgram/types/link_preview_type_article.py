from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewTypeArticle(BaseType):
    """
    The link is a link to a web site
    """

    __type__: Literal["linkPreviewTypeArticle"] = "linkPreviewTypeArticle"

    photo: Photo | None = None
    """Article's main photo; may be null"""
