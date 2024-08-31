from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatFolder


@dataclass(kw_only=True)
class RecommendedChatFolder(BaseType):
    """
    Describes a recommended chat folder
    """

    __type__: Literal["recommendedChatFolder"] = "recommendedChatFolder"

    folder: ChatFolder
    """The chat folder"""
    description: str
    """Chat folder description"""
