from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BackgroundFill


@dataclass(kw_only=True)
class BackgroundTypeFill(BaseType):
    """
    A filled background
    """

    __type__: Literal["backgroundTypeFill"] = "backgroundTypeFill"

    fill: BackgroundFill
    """The background fill"""
