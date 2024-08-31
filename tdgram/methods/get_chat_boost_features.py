from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatBoostFeatures
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatBoostFeatures(BaseMethod):
    """
    Returns the list of features available for different chat boost levels; this is an offline request
    """

    __type__: Literal["getChatBoostFeatures"] = "getChatBoostFeatures"
    __returning_type__ = ChatBoostFeatures

    is_channel: bool
    """Pass true to get the list of features for channels; pass false to get the list of features for supergroups"""
