from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        FactCheck,
        MessageContent,
        MessageForwardInfo,
        MessageImportInfo,
        MessageInteractionInfo,
        MessageReplyTo,
        MessageSchedulingState,
        MessageSelfDestructType,
        MessageSender,
        MessageSendingState,
        ReplyMarkup,
        UnreadReaction,
    )


@dataclass(kw_only=True)
class Message(BaseType):
    """
    Describes a message
    """

    __type__: Literal["message"] = "message"

    id: int
    """Message identifier; unique for the chat to which the message belongs"""
    sender_id: MessageSender
    """Identifier of the sender of the message"""
    chat_id: int
    """Chat identifier"""
    sending_state: MessageSendingState | None = None
    """The sending state of the message; may be null if the message isn't being sent and didn't fail to be sent"""
    scheduling_state: MessageSchedulingState | None = None
    """The scheduling state of the message; may be null if the message isn't scheduled"""
    is_outgoing: bool
    """True, if the message is outgoing"""
    is_pinned: bool
    """True, if the message is pinned"""
    is_from_offline: bool
    """True, if the message was sent because of a scheduled action by the message sender, for example, as away, or greeting service message"""
    can_be_saved: bool
    """True, if content of the message can be saved locally or copied using inputMessageForwarded or forwardMessages with copy options"""
    has_timestamped_media: bool
    """True, if media timestamp entities refers to a media in this message as opposed to a media in the replied message"""
    is_channel_post: bool
    """True, if the message is a channel post. All messages to channels are channel posts, all other messages are not channel posts"""
    is_topic_message: bool
    """True, if the message is a forum topic message"""
    contains_unread_mention: bool
    """True, if the message contains an unread mention for the current user"""
    date: int
    """Point in time (Unix timestamp) when the message was sent; 0 for scheduled messages"""
    edit_date: int
    """Point in time (Unix timestamp) when the message was last edited; 0 for scheduled messages"""
    forward_info: MessageForwardInfo | None = None
    """Information about the initial message sender; may be null if none or unknown"""
    import_info: MessageImportInfo | None = None
    """Information about the initial message for messages created with importMessages; may be null if the message isn't imported"""
    interaction_info: MessageInteractionInfo | None = None
    """Information about interactions with the message; may be null if none"""
    unread_reactions: list[UnreadReaction]
    """Information about unread reactions added to the message"""
    fact_check: FactCheck | None = None
    """Information about fact-check added to the message; may be null if none"""
    reply_to: MessageReplyTo | None = None
    """Information about the message or the story this message is replying to; may be null if none"""
    message_thread_id: int
    """If non-zero, the identifier of the message thread the message belongs to; unique within the chat to which the message belongs"""
    saved_messages_topic_id: int
    """Identifier of the Saved Messages topic for the message; 0 for messages not from Saved Messages"""
    self_destruct_type: MessageSelfDestructType | None = None
    """The message's self-destruct type; may be null if none"""
    self_destruct_in: float
    """Time left before the message self-destruct timer expires, in seconds; 0 if self-destruction isn't scheduled yet"""
    auto_delete_in: float
    """Time left before the message will be automatically deleted by message_auto_delete_time setting of the chat, in seconds; 0 if never"""
    via_bot_user_id: int
    """If non-zero, the user identifier of the inline bot through which this message was sent"""
    sender_business_bot_user_id: int
    """If non-zero, the user identifier of the business bot that sent this message"""
    sender_boost_count: int
    """Number of times the sender of the message boosted the supergroup at the time the message was sent; 0 if none or unknown. For messages sent by the current user, supergroupFullInfo.my_boost_count must be used instead"""
    author_signature: str
    """For channel posts and anonymous group messages, optional author signature"""
    media_album_id: int
    """Unique identifier of an album this message belongs to; 0 if none. Only audios, documents, photos and videos can be grouped together in albums"""
    effect_id: int
    """Unique identifier of the effect added to the message; 0 if none"""
    has_sensitive_content: bool
    """True, if media content of the message must be hidden with 18+ spoiler"""
    restriction_reason: str | None = None
    """If non-empty, contains a human-readable description of the reason why access to this message must be restricted"""
    content: MessageContent
    """Content of the message"""
    reply_markup: ReplyMarkup | None = None
    """Reply markup for the message; may be null if none"""
