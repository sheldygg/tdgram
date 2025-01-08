from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ConnectedAffiliateProgram


@dataclass(kw_only=True)
class ConnectedAffiliatePrograms(BaseType):
    """
    Represents a list of affiliate programs that were connected to an affiliate
    """

    __type__: Literal["connectedAffiliatePrograms"] = "connectedAffiliatePrograms"

    total_count: int
    """The total number of affiliate programs that were connected to the affiliate"""
    programs: list[ConnectedAffiliateProgram]
    """The list of connected affiliate programs"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""
