from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockTableCell, RichText


@dataclass(kw_only=True)
class PageBlockTable(BaseType):
    """
    A table
    """

    __type__: Literal["pageBlockTable"] = "pageBlockTable"

    caption: RichText
    """Table caption"""
    cells: list[list[PageBlockTableCell]]
    """Table cells"""
    is_bordered: bool
    """True, if the table is bordered"""
    is_striped: bool
    """True, if the table is striped"""
