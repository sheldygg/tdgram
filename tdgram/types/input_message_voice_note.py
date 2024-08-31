from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputFile, MessageSelfDestructType


@dataclass(kw_only=True)
class InputMessageVoiceNote(BaseType):
    """
    A voice note message
    """

    __type__: Literal["inputMessageVoiceNote"] = "inputMessageVoiceNote"

    voice_note: InputFile
    """Voice note to be sent. The voice note must be encoded with the Opus codec and stored inside an OGG container with a single audio channel, or be in MP3 or M4A format as regular audio"""
    duration: int
    """Duration of the voice note, in seconds"""
    waveform: bytes
    """Waveform representation of the voice note in 5-bit format"""
    caption: FormattedText | None = None
    """Voice note caption; may be null if empty; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""
    self_destruct_type: MessageSelfDestructType | None = None
    """Voice note self-destruct type; may be null if none; pass null if none; private chats only"""
