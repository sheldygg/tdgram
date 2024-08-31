from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LocalizationTargetInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLocalizationTargetInfo(BaseMethod):
    """
    Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization
    """

    __type__: Literal["getLocalizationTargetInfo"] = "getLocalizationTargetInfo"
    __returning_type__ = LocalizationTargetInfo

    only_local: bool
    """Pass true to get only locally available information without sending network requests"""
