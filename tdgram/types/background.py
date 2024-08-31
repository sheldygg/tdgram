from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BackgroundType, Document


@dataclass(kw_only=True)
class Background(BaseType):
    """
    Describes a chat background
    """

    __type__: Literal["background"] = "background"

    id: int
    """Unique background identifier"""
    is_default: bool
    """True, if this is one of default backgrounds"""
    is_dark: bool
    """True, if the background is dark and is recommended to be used with dark theme"""
    name: str
    """Unique background name"""
    document: Document | None = None
    """Document with the background; may be null. Null only for filled and chat theme backgrounds"""
    type: BackgroundType
    """Type of the background"""
