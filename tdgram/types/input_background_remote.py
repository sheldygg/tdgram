from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputBackgroundRemote(BaseType):
    """
    A background from the server
    """

    __type__: Literal["inputBackgroundRemote"] = "inputBackgroundRemote"

    background_id: int
    """The background identifier"""
