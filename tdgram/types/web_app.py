from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation, Photo


@dataclass(kw_only=True)
class WebApp(BaseType):
    """
    Describes a Web App. Use getInternalLink with internalLinkTypeWebApp to share the Web App
    """

    __type__: Literal["webApp"] = "webApp"

    short_name: str
    """Web App short name"""
    title: str
    """Web App title"""
    description: str
    """Web App description"""
    photo: Photo
    """Web App photo"""
    animation: Animation | None = None
    """Web App animation; may be null"""
