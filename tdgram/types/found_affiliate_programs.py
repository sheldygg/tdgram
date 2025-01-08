from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FoundAffiliateProgram


@dataclass(kw_only=True)
class FoundAffiliatePrograms(BaseType):
    """
    Represents a list of found affiliate programs
    """

    __type__: Literal["foundAffiliatePrograms"] = "foundAffiliatePrograms"

    total_count: int
    """The total number of found affiliate programs"""
    programs: list[FoundAffiliateProgram]
    """The list of affiliate programs"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""
