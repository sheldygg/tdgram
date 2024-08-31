from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TMeUrlTypeSupergroup(BaseType):
    """
    A URL linking to a public supergroup or channel
    """

    __type__: Literal["tMeUrlTypeSupergroup"] = "tMeUrlTypeSupergroup"

    supergroup_id: int
    """Identifier of the supergroup or channel"""
