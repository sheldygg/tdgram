from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Background


@dataclass(kw_only=True)
class UpdateDefaultBackground(BaseType):
    """
    The default background has changed
    """

    __type__: Literal["updateDefaultBackground"] = "updateDefaultBackground"

    for_dark_theme: bool
    """True, if default background for dark theme has changed"""
    background: Background | None = None
    """The new default background; may be null"""
