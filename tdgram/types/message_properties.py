from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageProperties(BaseType):
    """
    Contains properties of a message and describes actions that can be done with the message right now
    """

    __type__: Literal["messageProperties"] = "messageProperties"

    can_be_deleted_only_for_self: bool
    """True, if the message can be deleted only for the current user while other users will continue to see it using the method deleteMessages with revoke == false"""
    can_be_deleted_for_all_users: bool
    """True, if the message can be deleted for all users using the method deleteMessages with revoke == true"""
    can_be_edited: bool
    """True, if the message can be edited using the methods editMessageText, editMessageMedia, editMessageCaption, or editMessageReplyMarkup."""
    can_be_forwarded: bool
    """True, if the message can be forwarded using inputMessageForwarded or forwardMessages"""
    can_be_paid: bool
    """True, if the message can be paid using inputInvoiceMessage"""
    can_be_pinned: bool
    """True, if the message can be pinned or unpinned in the chat using pinChatMessage or unpinChatMessage"""
    can_be_replied: bool
    """True, if the message can be replied in the same chat and forum topic using inputMessageReplyToMessage"""
    can_be_replied_in_another_chat: bool
    """True, if the message can be replied in another chat or forum topic using inputMessageReplyToExternalMessage"""
    can_be_saved: bool
    """True, if content of the message can be saved locally or copied using inputMessageForwarded or forwardMessages with copy options"""
    can_be_shared_in_story: bool
    """True, if the message can be shared in a story using inputStoryAreaTypeMessage"""
    can_edit_scheduling_state: bool
    """True, if scheduling state of the message can be edited"""
    can_get_embedding_code: bool
    """True, if code for message embedding can be received using getMessageEmbeddingCode"""
    can_get_link: bool
    """True, if a link can be generated for the message using getMessageLink"""
    can_get_media_timestamp_links: bool
    """True, if media timestamp links can be generated for media timestamp entities in the message text, caption or link preview description using getMessageLink"""
    can_get_message_thread: bool
    """True, if information about the message thread is available through getMessageThread and getMessageThreadHistory"""
    can_get_read_date: bool
    """True, if read date of the message can be received through getMessageReadDate"""
    can_get_statistics: bool
    """True, if message statistics are available through getMessageStatistics and message forwards can be received using getMessagePublicForwards"""
    can_get_viewers: bool
    """True, if chat members already viewed the message can be received through getMessageViewers"""
    can_recognize_speech: bool
    """True, if speech can be recognized for the message through recognizeSpeech"""
    can_report_chat: bool
    """True, if the message can be reported using reportChat"""
    can_report_reactions: bool
    """True, if reactions on the message can be reported through reportMessageReactions"""
    can_report_supergroup_spam: bool
    """True, if the message can be reported using reportSupergroupSpam"""
    can_set_fact_check: bool
    """True, if fact check for the message can be changed through setMessageFactCheck"""
    need_show_statistics: bool
    """True, if message statistics must be available from context menu of the message"""
