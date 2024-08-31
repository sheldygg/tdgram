from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Count
from .base import BaseMethod


@dataclass(kw_only=True)
class GetImportedContactCount(BaseMethod):
    """
    Returns the total number of imported contacts
    """

    __type__: Literal["getImportedContactCount"] = "getImportedContactCount"
    __returning_type__ = Count
