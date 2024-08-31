from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlock


@dataclass(kw_only=True)
class PageBlockCover(BaseType):
    """
    A page cover
    """

    __type__: Literal["pageBlockCover"] = "pageBlockCover"

    cover: PageBlock
    """Cover"""
