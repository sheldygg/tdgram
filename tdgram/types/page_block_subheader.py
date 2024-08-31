from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockSubheader(BaseType):
    """
    A subheader
    """

    __type__: Literal["pageBlockSubheader"] = "pageBlockSubheader"

    subheader: RichText
    """Subheader"""
