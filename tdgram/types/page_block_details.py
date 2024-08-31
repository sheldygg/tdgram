from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlock, RichText


@dataclass(kw_only=True)
class PageBlockDetails(BaseType):
    """
    A collapsible block
    """

    __type__: Literal["pageBlockDetails"] = "pageBlockDetails"

    header: RichText
    """Always visible heading for the block"""
    page_blocks: list[PageBlock]
    """Block contents"""
    is_open: bool
    """True, if the block is open by default"""
