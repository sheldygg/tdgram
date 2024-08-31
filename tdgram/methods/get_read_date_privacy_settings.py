from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ReadDatePrivacySettings
from .base import BaseMethod


@dataclass(kw_only=True)
class GetReadDatePrivacySettings(BaseMethod):
    """
    Returns privacy settings for message read date
    """

    __type__: Literal["getReadDatePrivacySettings"] = "getReadDatePrivacySettings"
    __returning_type__ = ReadDatePrivacySettings
