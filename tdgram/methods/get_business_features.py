from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessFeature, BusinessFeatures
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBusinessFeatures(BaseMethod):
    """
    Returns information about features, available to Business users
    """

    __type__: Literal["getBusinessFeatures"] = "getBusinessFeatures"
    __returning_type__ = BusinessFeatures

    source: BusinessFeature | None = None
    """Source of the request; pass null if the method is called from settings or some non-standard source"""
