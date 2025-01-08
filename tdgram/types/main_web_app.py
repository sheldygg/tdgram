from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import WebAppOpenMode


@dataclass(kw_only=True)
class MainWebApp(BaseType):
    """
    Contains information about the main Web App of a bot
    """

    __type__: Literal["mainWebApp"] = "mainWebApp"

    url: str
    """URL of the Web App to open"""
    mode: WebAppOpenMode
    """The mode in which the Web App must be opened"""
