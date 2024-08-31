from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessFeature


@dataclass(kw_only=True)
class PremiumSourceBusinessFeature(BaseType):
    """
    A user tried to use a Business feature
    """

    __type__: Literal["premiumSourceBusinessFeature"] = "premiumSourceBusinessFeature"

    feature: BusinessFeature | None = None
    """The used feature; pass null if none specific feature was used"""
