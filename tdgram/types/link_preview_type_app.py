from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewTypeApp(BaseType):
    """
    The link is a link to an app at App Store or Google Play
    """

    __type__: Literal["linkPreviewTypeApp"] = "linkPreviewTypeApp"

    photo: Photo
    """Photo for the app"""
