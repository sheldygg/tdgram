from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputBusinessStartPage(BaseType):
    """
    Describes settings for a business account start page to set
    """

    __type__: Literal["inputBusinessStartPage"] = "inputBusinessStartPage"

    title: str
    """Title text of the start page; 0-getOption('business_start_page_title_length_max') characters"""
    message: str
    """Message text of the start page; 0-getOption('business_start_page_message_length_max') characters"""
    sticker: InputFile | None = None
    """Greeting sticker of the start page; pass null if none. The sticker must belong to a sticker set and must not be a custom emoji"""
