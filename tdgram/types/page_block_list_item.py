from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlock


@dataclass(kw_only=True)
class PageBlockListItem(BaseType):
    """
    Describes an item of a list page block
    """

    __type__: Literal["pageBlockListItem"] = "pageBlockListItem"

    label: str
    """Item label"""
    page_blocks: list[PageBlock]
    """Item blocks"""
