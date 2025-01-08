from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AffiliateType, ConnectedAffiliatePrograms
from .base import BaseMethod


@dataclass(kw_only=True)
class GetConnectedAffiliatePrograms(BaseMethod):
    """
    Returns affiliate programs that were connected to the given affiliate
    """

    __type__: Literal["getConnectedAffiliatePrograms"] = "getConnectedAffiliatePrograms"
    __returning_type__ = ConnectedAffiliatePrograms

    affiliate: AffiliateType
    """The affiliate to which the affiliate program were connected"""
    offset: str
    """Offset of the first affiliate program to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of affiliate programs to return"""
