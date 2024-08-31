from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LanguagePackInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLanguagePackInfo(BaseMethod):
    """
    Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization
    """

    __type__: Literal["getLanguagePackInfo"] = "getLanguagePackInfo"
    __returning_type__ = LanguagePackInfo

    language_pack_id: str
    """Language pack identifier"""
