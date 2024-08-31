from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, PaidMedia


@dataclass(kw_only=True)
class MessagePaidMedia(BaseType):
    """
    A message with paid media
    """

    __type__: Literal["messagePaidMedia"] = "messagePaidMedia"

    star_count: int
    """Number of Telegram Stars needed to buy access to the media in the message"""
    media: list[PaidMedia]
    """Information about the media"""
    caption: FormattedText
    """Media caption"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the media; otherwise, the caption must be shown below the media"""
