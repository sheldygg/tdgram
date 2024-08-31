from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Document


@dataclass(kw_only=True)
class PushMessageContentDocument(BaseType):
    """
    A document message (a general file)
    """

    __type__: Literal["pushMessageContentDocument"] = "pushMessageContentDocument"

    document: Document | None = None
    """Message content; may be null"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
