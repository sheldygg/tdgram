from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RecommendedChatFolder


@dataclass(kw_only=True)
class RecommendedChatFolders(BaseType):
    """
    Contains a list of recommended chat folders
    """

    __type__: Literal["recommendedChatFolders"] = "recommendedChatFolders"

    chat_folders: list[RecommendedChatFolder]
    """List of recommended chat folders"""
