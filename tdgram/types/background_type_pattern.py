from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BackgroundFill


@dataclass(kw_only=True)
class BackgroundTypePattern(BaseType):
    """
    A PNG or TGV (gzipped subset of SVG with MIME type 'application/x-tgwallpattern') pattern to be combined with the background fill chosen by the user
    """

    __type__: Literal["backgroundTypePattern"] = "backgroundTypePattern"

    fill: BackgroundFill
    """Fill of the background"""
    intensity: int
    """Intensity of the pattern when it is shown above the filled background; 0-100"""
    is_inverted: bool
    """True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only"""
    is_moving: bool
    """True, if the background needs to be slightly moved when device is tilted"""
