from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageContent, MessageSendingState, ReplyMarkup


@dataclass(kw_only=True)
class QuickReplyMessage(BaseType):
    """
    Describes a message that can be used for quick reply
    """

    __type__: Literal["quickReplyMessage"] = "quickReplyMessage"

    id: int
    """Unique message identifier among all quick replies"""
    sending_state: MessageSendingState | None = None
    """The sending state of the message; may be null if the message isn't being sent and didn't fail to be sent"""
    can_be_edited: bool
    """True, if the message can be edited"""
    reply_to_message_id: int
    """The identifier of the quick reply message to which the message replies; 0 if none"""
    via_bot_user_id: int
    """If non-zero, the user identifier of the bot through which this message was sent"""
    media_album_id: int
    """Unique identifier of an album this message belongs to; 0 if none. Only audios, documents, photos and videos can be grouped together in albums"""
    content: MessageContent
    """Content of the message"""
    reply_markup: ReplyMarkup | None = None
    """Inline keyboard reply markup for the message; may be null if none"""
