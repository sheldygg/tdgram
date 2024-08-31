from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockCaption, Photo


@dataclass(kw_only=True)
class PageBlockPhoto(BaseType):
    """
    A photo
    """

    __type__: Literal["pageBlockPhoto"] = "pageBlockPhoto"

    photo: Photo | None = None
    """Photo file; may be null"""
    caption: PageBlockCaption
    """Photo caption"""
    url: str
    """URL that needs to be opened when the photo is clicked"""
