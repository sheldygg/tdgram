from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextSubscript(BaseType):
    """
    A subscript rich text
    """

    __type__: Literal["richTextSubscript"] = "richTextSubscript"

    text: RichText
    """Text"""
