from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockFooter(BaseType):
    """
    The footer of a page
    """

    __type__: Literal["pageBlockFooter"] = "pageBlockFooter"

    footer: RichText
    """Footer"""
