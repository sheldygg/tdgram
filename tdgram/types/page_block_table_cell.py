from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockHorizontalAlignment, PageBlockVerticalAlignment, RichText


@dataclass(kw_only=True)
class PageBlockTableCell(BaseType):
    """
    Represents a cell of a table
    """

    __type__: Literal["pageBlockTableCell"] = "pageBlockTableCell"

    text: RichText | None = None
    """Cell text; may be null. If the text is null, then the cell must be invisible"""
    is_header: bool
    """True, if it is a header cell"""
    colspan: int
    """The number of columns the cell spans"""
    rowspan: int
    """The number of rows the cell spans"""
    align: PageBlockHorizontalAlignment
    """Horizontal cell content alignment"""
    valign: PageBlockVerticalAlignment
    """Vertical cell content alignment"""
