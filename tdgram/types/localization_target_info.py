from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LanguagePackInfo


@dataclass(kw_only=True)
class LocalizationTargetInfo(BaseType):
    """
    Contains information about the current localization target
    """

    __type__: Literal["localizationTargetInfo"] = "localizationTargetInfo"

    language_packs: list[LanguagePackInfo]
    """List of available language packs for this application"""
