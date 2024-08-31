from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, SpeechRecognitionResult


@dataclass(kw_only=True)
class VoiceNote(BaseType):
    """
    Describes a voice note
    """

    __type__: Literal["voiceNote"] = "voiceNote"

    duration: int
    """Duration of the voice note, in seconds; as defined by the sender"""
    waveform: bytes
    """A waveform representation of the voice note in 5-bit format"""
    mime_type: str
    """MIME type of the file; as defined by the sender. Usually, one of 'audio/ogg' for Opus in an OGG container, 'audio/mpeg' for an MP3 audio, or 'audio/mp4' for an M4A audio"""
    speech_recognition_result: SpeechRecognitionResult | None = None
    """Result of speech recognition in the voice note; may be null"""
    voice: File
    """File containing the voice note"""
