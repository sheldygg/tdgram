from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSchedulingState


@dataclass(kw_only=True)
class MessageSendOptions(BaseType):
    """
    Options to be used when a message is sent
    """

    __type__: Literal["messageSendOptions"] = "messageSendOptions"

    disable_notification: bool
    """Pass true to disable notification for the message"""
    from_background: bool
    """Pass true if the message is sent from the background"""
    protect_content: bool
    """Pass true if the content of the message must be protected from forwarding and saving; for bots only"""
    allow_paid_broadcast: bool
    """Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only"""
    update_order_of_installed_sticker_sets: bool
    """Pass true if the user explicitly chosen a sticker or a custom emoji from an installed sticker set; applicable only to sendMessage and sendMessageAlbum"""
    scheduling_state: MessageSchedulingState | None = None
    """Message scheduling state; pass null to send message immediately. Messages sent to a secret chat, live location messages and self-destructing messages can't be scheduled"""
    effect_id: int
    """Identifier of the effect to apply to the message; pass 0 if none; applicable only to sendMessage and sendMessageAlbum in private chats"""
    sending_id: int
    """Non-persistent identifier, which will be returned back in messageSendingStatePending object and can be used to match sent messages and corresponding updateNewMessage updates"""
    only_preview: bool
    """Pass true to get a fake message instead of actually sending them"""
