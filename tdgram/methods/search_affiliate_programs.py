from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AffiliateProgramSortOrder, AffiliateType, FoundAffiliatePrograms
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchAffiliatePrograms(BaseMethod):
    """
    Searches affiliate programs that can be connected to the given affiliate
    """

    __type__: Literal["searchAffiliatePrograms"] = "searchAffiliatePrograms"
    __returning_type__ = FoundAffiliatePrograms

    affiliate: AffiliateType
    """The affiliate for which affiliate programs are searched for"""
    sort_order: AffiliateProgramSortOrder
    """Sort order for the results"""
    offset: str
    """Offset of the first affiliate program to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of affiliate programs to return"""
