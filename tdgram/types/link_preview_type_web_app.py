from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewTypeWebApp(BaseType):
    """
    The link is a link to a Web App
    """

    __type__: Literal["linkPreviewTypeWebApp"] = "linkPreviewTypeWebApp"

    photo: Photo
    """Web App photo"""
