from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import RecommendedChatFolders
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecommendedChatFolders(BaseMethod):
    """
    Returns recommended chat folders for the current user
    """

    __type__: Literal["getRecommendedChatFolders"] = "getRecommendedChatFolders"
    __returning_type__ = RecommendedChatFolders
