from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockListItem


@dataclass(kw_only=True)
class PageBlockList(BaseType):
    """
    A list of data blocks
    """

    __type__: Literal["pageBlockList"] = "pageBlockList"

    items: list[PageBlockListItem]
    """The items of the list"""
