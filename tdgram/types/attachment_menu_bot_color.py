from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AttachmentMenuBotColor(BaseType):
    """
    Describes a color to highlight a bot added to attachment menu
    """

    __type__: Literal["attachmentMenuBotColor"] = "attachmentMenuBotColor"

    light_color: int
    """Color in the RGB format for light themes"""
    dark_color: int
    """Color in the RGB format for dark themes"""
