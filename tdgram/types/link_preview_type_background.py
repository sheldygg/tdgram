from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BackgroundType, Document


@dataclass(kw_only=True)
class LinkPreviewTypeBackground(BaseType):
    """
    The link is a link to a background. Link preview title and description are available only for filled backgrounds
    """

    __type__: Literal["linkPreviewTypeBackground"] = "linkPreviewTypeBackground"

    document: Document | None = None
    """Document with the background; may be null for filled backgrounds"""
    background_type: BackgroundType | None = None
    """Type of the background; may be null if unknown"""
