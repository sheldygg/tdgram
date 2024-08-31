from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AutoDownloadSettings(BaseType):
    """
    Contains auto-download settings
    """

    __type__: Literal["autoDownloadSettings"] = "autoDownloadSettings"

    is_auto_download_enabled: bool
    """True, if the auto-download is enabled"""
    max_photo_file_size: int
    """The maximum size of a photo file to be auto-downloaded, in bytes"""
    max_video_file_size: int
    """The maximum size of a video file to be auto-downloaded, in bytes"""
    max_other_file_size: int
    """The maximum size of other file types to be auto-downloaded, in bytes"""
    video_upload_bitrate: int
    """The maximum suggested bitrate for uploaded videos, in kbit/s"""
    preload_large_videos: bool
    """True, if the beginning of video files needs to be preloaded for instant playback"""
    preload_next_audio: bool
    """True, if the next audio track needs to be preloaded while the user is listening to an audio file"""
    preload_stories: bool
    """True, if stories needs to be preloaded"""
    use_less_data_for_calls: bool
    """True, if 'use less data for calls' option needs to be enabled"""
