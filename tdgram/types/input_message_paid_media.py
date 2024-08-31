from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputPaidMedia


@dataclass(kw_only=True)
class InputMessagePaidMedia(BaseType):
    """
    A message with paid media; can be used only in channel chats with supergroupFullInfo.has_paid_media_allowed
    """

    __type__: Literal["inputMessagePaidMedia"] = "inputMessagePaidMedia"

    star_count: int
    """The number of Telegram Stars that must be paid to see the media; 1-getOption('paid_media_message_star_count_max')"""
    paid_media: list[InputPaidMedia]
    """The content of the paid media"""
    caption: FormattedText | None = None
    """Message caption; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the video; otherwise, the caption must be shown below the video; not supported in secret chats"""
