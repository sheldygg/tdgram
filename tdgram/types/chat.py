from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        BlockList,
        BusinessBotManageBar,
        ChatActionBar,
        ChatAvailableReactions,
        ChatBackground,
        ChatJoinRequestsInfo,
        ChatList,
        ChatNotificationSettings,
        ChatPermissions,
        ChatPhotoInfo,
        ChatPosition,
        ChatType,
        DraftMessage,
        EmojiStatus,
        Message,
        MessageSender,
        VideoChat,
    )


@dataclass(kw_only=True)
class Chat(BaseType):
    """
    A chat. (Can be a private chat, basic group, supergroup, or secret chat)
    """

    __type__: Literal["chat"] = "chat"

    id: int
    """Chat unique identifier"""
    type: ChatType
    """Type of the chat"""
    title: str
    """Chat title"""
    photo: ChatPhotoInfo | None = None
    """Chat photo; may be null"""
    accent_color_id: int
    """Identifier of the accent color for message sender name, and backgrounds of chat photo, reply header, and link preview"""
    background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the reply header and link preview background for messages sent by the chat; 0 if none"""
    profile_accent_color_id: int
    """Identifier of the profile accent color for the chat's profile; -1 if none"""
    profile_background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the background of the chat's profile; 0 if none"""
    permissions: ChatPermissions
    """Actions that non-administrator chat members are allowed to take in the chat"""
    last_message: Message | None = None
    """Last message in the chat; may be null if none or unknown"""
    positions: list[ChatPosition]
    """Positions of the chat in chat lists"""
    chat_lists: list[ChatList]
    """Chat lists to which the chat belongs. A chat can have a non-zero position in a chat list even it doesn't belong to the chat list and have no position in a chat list even it belongs to the chat list"""
    message_sender_id: MessageSender | None = None
    """Identifier of a user or chat that is selected to send messages in the chat; may be null if the user can't change message sender"""
    block_list: BlockList | None = None
    """Block list to which the chat is added; may be null if none"""
    has_protected_content: bool
    """True, if chat content can't be saved locally, forwarded, or copied"""
    is_translatable: bool
    """True, if translation of all messages in the chat must be suggested to the user"""
    is_marked_as_unread: bool
    """True, if the chat is marked as unread"""
    view_as_topics: bool
    """True, if the chat is a forum supergroup that must be shown in the 'View as topics' mode, or Saved Messages chat that must be shown in the 'View as chats'"""
    has_scheduled_messages: bool
    """True, if the chat has scheduled messages"""
    can_be_deleted_only_for_self: bool
    """True, if the chat messages can be deleted only for the current user while other users will continue to see the messages"""
    can_be_deleted_for_all_users: bool
    """True, if the chat messages can be deleted for all users"""
    can_be_reported: bool
    """True, if the chat can be reported to Telegram moderators through reportChat or reportChatPhoto"""
    default_disable_notification: bool
    """Default value of the disable_notification parameter, used when a message is sent to the chat"""
    unread_count: int
    """Number of unread messages in the chat"""
    last_read_inbox_message_id: int
    """Identifier of the last read incoming message"""
    last_read_outbox_message_id: int
    """Identifier of the last read outgoing message"""
    unread_mention_count: int
    """Number of unread messages with a mention/reply in the chat"""
    unread_reaction_count: int
    """Number of messages with unread reactions in the chat"""
    notification_settings: ChatNotificationSettings
    """Notification settings for the chat"""
    available_reactions: ChatAvailableReactions
    """Types of reaction, available in the chat"""
    message_auto_delete_time: int
    """Current message auto-delete or self-destruct timer setting for the chat, in seconds; 0 if disabled. Self-destruct timer in secret chats starts after the message or its content is viewed. Auto-delete timer in other chats starts from the send date"""
    emoji_status: EmojiStatus | None = None
    """Emoji status to be shown along with chat title; may be null"""
    background: ChatBackground | None = None
    """Background set for the chat; may be null if none"""
    theme_name: str | None = None
    """If non-empty, name of a theme, set for the chat"""
    action_bar: ChatActionBar | None = None
    """Information about actions which must be possible to do through the chat action bar; may be null if none"""
    business_bot_manage_bar: BusinessBotManageBar | None = None
    """Information about bar for managing a business bot in the chat; may be null if none"""
    video_chat: VideoChat
    """Information about video chat of the chat"""
    pending_join_requests: ChatJoinRequestsInfo | None = None
    """Information about pending join requests; may be null if none"""
    reply_markup_message_id: int
    """Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat"""
    draft_message: DraftMessage | None = None
    """A draft of a message in the chat; may be null if none"""
    client_data: str
    """Application-specific data associated with the chat. (For example, the chat scroll position or local chat notification settings can be stored here.) Persistent if the message database is used"""
