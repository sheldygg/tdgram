from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockHeader(BaseType):
    """
    A header
    """

    __type__: Literal["pageBlockHeader"] = "pageBlockHeader"

    header: RichText
    """Header"""
