from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, Photo


@dataclass(kw_only=True)
class ProductInfo(BaseType):
    """
    Contains information about a product that can be paid with invoice
    """

    __type__: Literal["productInfo"] = "productInfo"

    title: str
    """Product title"""
    description: FormattedText
    """Product description"""
    photo: Photo | None = None
    """Product photo; may be null"""
