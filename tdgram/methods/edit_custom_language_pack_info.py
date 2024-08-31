from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LanguagePackInfo, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditCustomLanguagePackInfo(BaseMethod):
    """
    Edits information about a custom local language pack in the current localization target. Can be called before authorization
    """

    __type__: Literal["editCustomLanguagePackInfo"] = "editCustomLanguagePackInfo"
    __returning_type__ = Ok

    info: LanguagePackInfo
    """New information about the custom local language pack"""
