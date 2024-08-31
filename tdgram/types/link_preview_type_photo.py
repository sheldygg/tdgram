from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewTypePhoto(BaseType):
    """
    The link is a link to a photo
    """

    __type__: Literal["linkPreviewTypePhoto"] = "linkPreviewTypePhoto"

    photo: Photo
    """The photo"""
    author: str
    """Author of the photo"""
