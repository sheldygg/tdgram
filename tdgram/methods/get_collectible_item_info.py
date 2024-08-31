from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CollectibleItemInfo, CollectibleItemType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCollectibleItemInfo(BaseMethod):
    """
    Returns information about a given collectible item that was purchased at https://fragment.com
    """

    __type__: Literal["getCollectibleItemInfo"] = "getCollectibleItemInfo"
    __returning_type__ = CollectibleItemInfo

    type: CollectibleItemType
    """Type of the collectible item. The item must be used by a user and must be visible to the current user"""
