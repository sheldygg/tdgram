from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class InlineQueryResultPhoto(BaseType):
    """
    Represents a photo
    """

    __type__: Literal["inlineQueryResultPhoto"] = "inlineQueryResultPhoto"

    id: str
    """Unique identifier of the query result"""
    photo: Photo
    """Photo"""
    title: str
    """Title of the result, if known"""
    description: str
    """A short description of the result, if known"""
