from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import DeepLinkInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDeepLinkInfo(BaseMethod):
    """
    Returns information about a tg:// deep link. Use 'tg://need_update_for_some_feature' or 'tg:some_unsupported_feature' for testing. Returns a 404 error for unknown links. Can be called before authorization
    """

    __type__: Literal["getDeepLinkInfo"] = "getDeepLinkInfo"
    __returning_type__ = DeepLinkInfo

    link: str
    """The link"""
