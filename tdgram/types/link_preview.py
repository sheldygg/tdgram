from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, LinkPreviewType


@dataclass(kw_only=True)
class LinkPreview(BaseType):
    """
    Describes a link preview
    """

    __type__: Literal["linkPreview"] = "linkPreview"

    url: str
    """Original URL of the link"""
    display_url: str
    """URL to display"""
    site_name: str
    """Short name of the site (e.g., Google Docs, App Store)"""
    title: str
    """Title of the content"""
    description: FormattedText
    """Description of the content"""
    type: LinkPreviewType
    """Type of the link preview"""
    has_large_media: bool
    """True, if size of media in the preview can be changed"""
    show_large_media: bool
    """True, if large media preview must be shown; otherwise, the media preview must be shown small and only the first frame must be shown for videos"""
    show_media_above_description: bool
    """True, if media must be shown above link preview description; otherwise, the media must be shown below the description"""
    skip_confirmation: bool
    """True, if there is no need to show an ordinary open URL confirmation, when opening the URL from the preview, because the URL is shown in the message text in clear"""
    show_above_text: bool
    """True, if the link preview must be shown above message text; otherwise, the link preview must be shown below the message text"""
    instant_view_version: int
    """Version of instant view (currently, can be 1 or 2) for the web page; 0 if none"""
