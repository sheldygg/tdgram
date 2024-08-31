from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReadDatePrivacySettings
from .base import BaseMethod


@dataclass(kw_only=True)
class SetReadDatePrivacySettings(BaseMethod):
    """
    Changes privacy settings for message read date
    """

    __type__: Literal["setReadDatePrivacySettings"] = "setReadDatePrivacySettings"
    __returning_type__ = Ok

    settings: ReadDatePrivacySettings
    """New settings"""
