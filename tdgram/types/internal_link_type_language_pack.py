from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeLanguagePack(BaseType):
    """
    The link is a link to a language pack. Call getLanguagePackInfo with the given language pack identifier to process the link.
    """

    __type__: Literal["internalLinkTypeLanguagePack"] = "internalLinkTypeLanguagePack"

    language_pack_id: str
    """Language pack identifier"""
