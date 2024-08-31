from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class MessageCopyOptions(BaseType):
    """
    Options to be used when a message content is copied without reference to the original sender. Service messages, messages with messageInvoice, messagePaidMedia, messagePremiumGiveaway, or messagePremiumGiveawayWinners content can't be copied
    """

    __type__: Literal["messageCopyOptions"] = "messageCopyOptions"

    send_copy: bool
    """True, if content of the message needs to be copied without reference to the original sender. Always true if the message is forwarded to a secret chat or is local"""
    replace_caption: bool
    """True, if media caption of the message copy needs to be replaced. Ignored if send_copy is false"""
    new_caption: FormattedText | None = None
    """New message caption; pass null to copy message without caption. Ignored if replace_caption is false"""
    new_show_caption_above_media: bool
    """True, if new caption must be shown above the animation; otherwise, new caption must be shown below the animation; not supported in secret chats. Ignored if replace_caption is false"""
