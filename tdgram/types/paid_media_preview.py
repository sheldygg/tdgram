from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Minithumbnail


@dataclass(kw_only=True)
class PaidMediaPreview(BaseType):
    """
    The media is hidden until the invoice is paid
    """

    __type__: Literal["paidMediaPreview"] = "paidMediaPreview"

    width: int
    """Media width; 0 if unknown"""
    height: int
    """Media height; 0 if unknown"""
    duration: int
    """Media duration, in seconds; 0 if unknown"""
    minithumbnail: Minithumbnail | None = None
    """Media minithumbnail; may be null"""
