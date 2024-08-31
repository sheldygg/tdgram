from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class PaidMediaPhoto(BaseType):
    """
    The media is a photo
    """

    __type__: Literal["paidMediaPhoto"] = "paidMediaPhoto"

    photo: Photo
    """The photo"""
