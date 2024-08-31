from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatBoostLevelFeatures
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatBoostLevelFeatures(BaseMethod):
    """
    Returns the list of features available on the specific chat boost level; this is an offline request
    """

    __type__: Literal["getChatBoostLevelFeatures"] = "getChatBoostLevelFeatures"
    __returning_type__ = ChatBoostLevelFeatures

    is_channel: bool
    """Pass true to get the list of features for channels; pass false to get the list of features for supergroups"""
    level: int
    """Chat boost level"""
