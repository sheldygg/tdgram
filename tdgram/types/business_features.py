from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessFeature


@dataclass(kw_only=True)
class BusinessFeatures(BaseType):
    """
    Contains information about features, available to Business user accounts
    """

    __type__: Literal["businessFeatures"] = "businessFeatures"

    features: list[BusinessFeature]
    """The list of available business features"""
