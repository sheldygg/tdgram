from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GroupCallVideoSourceGroup(BaseType):
    """
    Describes a group of video synchronization source identifiers
    """

    __type__: Literal["groupCallVideoSourceGroup"] = "groupCallVideoSourceGroup"

    semantics: str
    """The semantics of sources, one of 'SIM' or 'FID'"""
    source_ids: list[int]
    """The list of synchronization source identifiers"""
