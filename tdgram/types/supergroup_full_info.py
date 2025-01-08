from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BotCommands, BotVerification, ChatInviteLink, ChatLocation, ChatPhoto


@dataclass(kw_only=True)
class SupergroupFullInfo(BaseType):
    """
    Contains full information about a supergroup or channel
    """

    __type__: Literal["supergroupFullInfo"] = "supergroupFullInfo"

    photo: ChatPhoto | None = None
    """Chat photo; may be null if empty or unknown. If non-null, then it is the same photo as in chat.photo"""
    description: str
    """Supergroup or channel description"""
    member_count: int
    """Number of members in the supergroup or channel; 0 if unknown"""
    administrator_count: int
    """Number of privileged users in the supergroup or channel; 0 if unknown"""
    restricted_count: int
    """Number of restricted users in the supergroup; 0 if unknown"""
    banned_count: int
    """Number of users banned from chat; 0 if unknown"""
    linked_chat_id: int
    """Chat identifier of a discussion group for the channel, or a channel, for which the supergroup is the designated discussion group; 0 if none or unknown"""
    slow_mode_delay: int
    """Delay between consecutive sent messages for non-administrator supergroup members, in seconds"""
    slow_mode_delay_expires_in: float
    """Time left before next message can be sent in the supergroup, in seconds. An updateSupergroupFullInfo update is not triggered when value of this field changes, but both new and old values are non-zero"""
    can_enable_paid_reaction: bool
    """True, if paid reaction can be enabled in the channel chat; for channels only"""
    can_get_members: bool
    """True, if members of the chat can be retrieved via getSupergroupMembers or searchChatMembers"""
    has_hidden_members: bool
    """True, if non-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers"""
    can_hide_members: bool
    """True, if non-administrators and non-bots can be hidden in responses to getSupergroupMembers and searchChatMembers for non-administrators"""
    can_set_sticker_set: bool
    """True, if the supergroup sticker set can be changed"""
    can_set_location: bool
    """True, if the supergroup location can be changed"""
    can_get_statistics: bool
    """True, if the supergroup or channel statistics are available"""
    can_get_revenue_statistics: bool
    """True, if the supergroup or channel revenue statistics are available"""
    can_get_star_revenue_statistics: bool
    """True, if the supergroup or channel Telegram Star revenue statistics are available"""
    can_toggle_aggressive_anti_spam: bool
    """True, if aggressive anti-spam checks can be enabled or disabled in the supergroup"""
    is_all_history_available: bool
    """True, if new chat members will have access to old messages. In public, discussion, of forum groups and all channels, old messages are always available,"""
    can_have_sponsored_messages: bool
    """True, if the chat can have sponsored messages. The value of this field is only available to the owner of the chat"""
    has_aggressive_anti_spam_enabled: bool
    """True, if aggressive anti-spam checks are enabled in the supergroup. The value of this field is only available to chat administrators"""
    has_paid_media_allowed: bool
    """True, if paid media can be sent and forwarded to the channel chat; for channels only"""
    has_pinned_stories: bool
    """True, if the supergroup or channel has pinned stories"""
    my_boost_count: int
    """Number of times the current user boosted the supergroup or channel"""
    unrestrict_boost_count: int
    """Number of times the supergroup must be boosted by a user to ignore slow mode and chat permission restrictions; 0 if unspecified"""
    sticker_set_id: int
    """Identifier of the supergroup sticker set that must be shown before user sticker sets; 0 if none"""
    custom_emoji_sticker_set_id: int
    """Identifier of the custom emoji sticker set that can be used in the supergroup without Telegram Premium subscription; 0 if none"""
    location: ChatLocation | None = None
    """Location to which the supergroup is connected; may be null if none"""
    invite_link: ChatInviteLink | None = None
    """Primary invite link for the chat; may be null. For chat administrators with can_invite_users right only"""
    bot_commands: list[BotCommands]
    """List of commands of bots in the group"""
    bot_verification: BotVerification | None = None
    """Information about verification status of the supergroup or the channel provided by a bot; may be null if none or unknown"""
    upgraded_from_basic_group_id: int
    """Identifier of the basic group from which supergroup was upgraded; 0 if none"""
    upgraded_from_max_message_id: int
    """Identifier of the last message in the basic group from which supergroup was upgraded; 0 if none"""
