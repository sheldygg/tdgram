from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockTitle(BaseType):
    """
    The title of a page
    """

    __type__: Literal["pageBlockTitle"] = "pageBlockTitle"

    title: RichText
    """Title"""
