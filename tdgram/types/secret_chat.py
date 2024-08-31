from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SecretChatState


@dataclass(kw_only=True)
class SecretChat(BaseType):
    """
    Represents a secret chat
    """

    __type__: Literal["secretChat"] = "secretChat"

    id: int
    """Secret chat identifier"""
    user_id: int
    """Identifier of the chat partner"""
    state: SecretChatState
    """State of the secret chat"""
    is_outbound: bool
    """True, if the chat was created by the current user; false otherwise"""
    key_hash: bytes
    """Hash of the currently used key for comparison with the hash of the chat partner's key. This is a string of 36 little-endian bytes, which must be split into groups of 2 bits, each denoting a pixel of one of 4 colors FFFFFF, D5E6F3, 2D5775, and 2F99C9."""
    layer: int
    """Secret chat layer; determines features supported by the chat partner's application. Nested text entities and underline and strikethrough entities are supported if the layer >= 101,"""
