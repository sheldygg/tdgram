from typing import TypeVar

from .methods import (
    AcceptCall,
    AcceptTermsOfService,
    ActivateStoryStealthMode,
    AddBotMediaPreview,
    AddChatFolderByInviteLink,
    AddChatMember,
    AddChatMembers,
    AddChatToList,
    AddContact,
    AddCustomServerLanguagePack,
    AddFavoriteSticker,
    AddFileToDownloads,
    AddLocalMessage,
    AddLogMessage,
    AddMessageReaction,
    AddNetworkStatistics,
    AddPaidMessageReaction,
    AddProxy,
    AddQuickReplyShortcutInlineQueryResultMessage,
    AddQuickReplyShortcutMessage,
    AddQuickReplyShortcutMessageAlbum,
    AddRecentlyFoundChat,
    AddRecentSticker,
    AddSavedAnimation,
    AddSavedNotificationSound,
    AddStickerToSet,
    AllowBotToSendMessages,
    AnswerCallbackQuery,
    AnswerCustomQuery,
    AnswerInlineQuery,
    AnswerPreCheckoutQuery,
    AnswerShippingQuery,
    AnswerWebAppQuery,
    ApplyPremiumGiftCode,
    AssignAppStoreTransaction,
    AssignGooglePlayTransaction,
    BanChatMember,
    BaseMethod,
    BlockMessageSenderFromReplies,
    BoostChat,
    CanBotSendMessages,
    CancelDownloadFile,
    CancelPasswordReset,
    CancelPreliminaryUploadFile,
    CancelRecoveryEmailAddressVerification,
    CanPurchaseFromStore,
    CanSendMessageToUser,
    CanSendStory,
    CanTransferOwnership,
    ChangeImportedContacts,
    ChangeStickerSet,
    CheckAuthenticationBotToken,
    CheckAuthenticationCode,
    CheckAuthenticationEmailCode,
    CheckAuthenticationPassword,
    CheckAuthenticationPasswordRecoveryCode,
    CheckChatFolderInviteLink,
    CheckChatInviteLink,
    CheckChatUsername,
    CheckCreatedPublicChatsLimit,
    CheckEmailAddressVerificationCode,
    CheckLoginEmailAddressCode,
    CheckPasswordRecoveryCode,
    CheckPhoneNumberCode,
    CheckPremiumGiftCode,
    CheckQuickReplyShortcutName,
    CheckRecoveryEmailAddressCode,
    CheckStickerSetName,
    CleanFileName,
    ClearAllDraftMessages,
    ClearAutosaveSettingsExceptions,
    ClearImportedContacts,
    ClearRecentEmojiStatuses,
    ClearRecentlyFoundChats,
    ClearRecentReactions,
    ClearRecentStickers,
    ClearSearchedForTags,
    ClickAnimatedEmojiMessage,
    ClickChatSponsoredMessage,
    ClickPremiumSubscriptionButton,
    Close,
    CloseChat,
    CloseSecretChat,
    CloseStory,
    CloseWebApp,
    ConfirmQrCodeAuthentication,
    ConfirmSession,
    CreateBasicGroupChat,
    CreateBusinessChatLink,
    CreateCall,
    CreateChatFolder,
    CreateChatFolderInviteLink,
    CreateChatInviteLink,
    CreateChatSubscriptionInviteLink,
    CreateForumTopic,
    CreateInvoiceLink,
    CreateNewBasicGroupChat,
    CreateNewSecretChat,
    CreateNewStickerSet,
    CreateNewSupergroupChat,
    CreatePrivateChat,
    CreateSecretChat,
    CreateSupergroupChat,
    CreateTemporaryPassword,
    CreateVideoChat,
    DeleteAccount,
    DeleteAllCallMessages,
    DeleteAllRevokedChatInviteLinks,
    DeleteBotMediaPreviews,
    DeleteBusinessChatLink,
    DeleteBusinessConnectedBot,
    DeleteChat,
    DeleteChatBackground,
    DeleteChatFolder,
    DeleteChatFolderInviteLink,
    DeleteChatHistory,
    DeleteChatMessagesByDate,
    DeleteChatMessagesBySender,
    DeleteChatReplyMarkup,
    DeleteCommands,
    DeleteDefaultBackground,
    DeleteFile,
    DeleteForumTopic,
    DeleteLanguagePack,
    DeleteMessages,
    DeletePassportElement,
    DeleteProfilePhoto,
    DeleteQuickReplyShortcut,
    DeleteQuickReplyShortcutMessages,
    DeleteRevokedChatInviteLink,
    DeleteSavedCredentials,
    DeleteSavedMessagesTopicHistory,
    DeleteSavedMessagesTopicMessagesByDate,
    DeleteSavedOrderInfo,
    DeleteStickerSet,
    DeleteStory,
    Destroy,
    DisableAllSupergroupUsernames,
    DisableProxy,
    DiscardCall,
    DisconnectAllWebsites,
    DisconnectWebsite,
    DownloadFile,
    EditBotMediaPreview,
    EditBusinessChatLink,
    EditBusinessMessageCaption,
    EditBusinessMessageLiveLocation,
    EditBusinessMessageMedia,
    EditBusinessMessageReplyMarkup,
    EditBusinessMessageText,
    EditChatFolder,
    EditChatFolderInviteLink,
    EditChatInviteLink,
    EditChatSubscriptionInviteLink,
    EditCustomLanguagePackInfo,
    EditForumTopic,
    EditInlineMessageCaption,
    EditInlineMessageLiveLocation,
    EditInlineMessageMedia,
    EditInlineMessageReplyMarkup,
    EditInlineMessageText,
    EditMessageCaption,
    EditMessageLiveLocation,
    EditMessageMedia,
    EditMessageReplyMarkup,
    EditMessageSchedulingState,
    EditMessageText,
    EditProxy,
    EditQuickReplyMessage,
    EditStarSubscription,
    EditStory,
    EditStoryCover,
    EnableProxy,
    EndGroupCall,
    EndGroupCallRecording,
    EndGroupCallScreenSharing,
    FinishFileGeneration,
    ForwardMessages,
    GetAccountTtl,
    GetActiveSessions,
    GetAllPassportElements,
    GetAllStickerEmojis,
    GetAnimatedEmoji,
    GetApplicationConfig,
    GetApplicationDownloadLink,
    GetArchiveChatListSettings,
    GetArchivedStickerSets,
    GetAttachedStickerSets,
    GetAttachmentMenuBot,
    GetAuthorizationState,
    GetAutoDownloadSettingsPresets,
    GetAutosaveSettings,
    GetAvailableChatBoostSlots,
    GetBackgroundUrl,
    GetBankCardInfo,
    GetBasicGroup,
    GetBasicGroupFullInfo,
    GetBlockedMessageSenders,
    GetBotInfoDescription,
    GetBotInfoShortDescription,
    GetBotMediaPreviewInfo,
    GetBotMediaPreviews,
    GetBotName,
    GetBusinessChatLinkInfo,
    GetBusinessChatLinks,
    GetBusinessConnectedBot,
    GetBusinessConnection,
    GetBusinessFeatures,
    GetCallbackQueryAnswer,
    GetCallbackQueryMessage,
    GetChat,
    GetChatActiveStories,
    GetChatAdministrators,
    GetChatArchivedStories,
    GetChatAvailableMessageSenders,
    GetChatBoostFeatures,
    GetChatBoostLevelFeatures,
    GetChatBoostLink,
    GetChatBoostLinkInfo,
    GetChatBoosts,
    GetChatBoostStatus,
    GetChatEventLog,
    GetChatFolder,
    GetChatFolderChatCount,
    GetChatFolderChatsToLeave,
    GetChatFolderDefaultIconName,
    GetChatFolderInviteLinks,
    GetChatFolderNewChats,
    GetChatHistory,
    GetChatInviteLink,
    GetChatInviteLinkCounts,
    GetChatInviteLinkMembers,
    GetChatInviteLinks,
    GetChatJoinRequests,
    GetChatListsToAddChat,
    GetChatMember,
    GetChatMessageByDate,
    GetChatMessageCalendar,
    GetChatMessageCount,
    GetChatMessagePosition,
    GetChatNotificationSettingsExceptions,
    GetChatPinnedMessage,
    GetChatPostedToChatPageStories,
    GetChatRevenueStatistics,
    GetChatRevenueTransactions,
    GetChatRevenueWithdrawalUrl,
    GetChats,
    GetChatScheduledMessages,
    GetChatsForChatFolderInviteLink,
    GetChatSimilarChatCount,
    GetChatSimilarChats,
    GetChatSparseMessagePositions,
    GetChatSponsoredMessages,
    GetChatStatistics,
    GetChatStoryInteractions,
    GetChatsToSendStories,
    GetCloseFriends,
    GetCollectibleItemInfo,
    GetCommands,
    GetConnectedWebsites,
    GetContacts,
    GetCountries,
    GetCountryCode,
    GetCountryFlagEmoji,
    GetCreatedPublicChats,
    GetCurrentState,
    GetCurrentWeather,
    GetCustomEmojiReactionAnimations,
    GetCustomEmojiStickers,
    GetDatabaseStatistics,
    GetDeepLinkInfo,
    GetDefaultBackgroundCustomEmojiStickers,
    GetDefaultChatEmojiStatuses,
    GetDefaultChatPhotoCustomEmojiStickers,
    GetDefaultEmojiStatuses,
    GetDefaultMessageAutoDeleteTime,
    GetDefaultProfilePhotoCustomEmojiStickers,
    GetDisallowedChatEmojiStatuses,
    GetEmojiCategories,
    GetEmojiReaction,
    GetEmojiSuggestionsUrl,
    GetExternalLink,
    GetExternalLinkInfo,
    GetFavoriteStickers,
    GetFile,
    GetFileDownloadedPrefixSize,
    GetFileExtension,
    GetFileMimeType,
    GetForumTopic,
    GetForumTopicDefaultIcons,
    GetForumTopicLink,
    GetForumTopics,
    GetGameHighScores,
    GetGreetingStickers,
    GetGroupCall,
    GetGroupCallInviteLink,
    GetGroupCallStreams,
    GetGroupCallStreamSegment,
    GetGroupsInCommon,
    GetImportedContactCount,
    GetInactiveSupergroupChats,
    GetInlineGameHighScores,
    GetInlineQueryResults,
    GetInstalledBackgrounds,
    GetInstalledStickerSets,
    GetInternalLink,
    GetInternalLinkType,
    GetJsonString,
    GetJsonValue,
    GetKeywordEmojis,
    GetLanguagePackInfo,
    GetLanguagePackString,
    GetLanguagePackStrings,
    GetLinkPreview,
    GetLocalizationTargetInfo,
    GetLoginUrl,
    GetLoginUrlInfo,
    GetLogStream,
    GetLogTags,
    GetLogTagVerbosityLevel,
    GetLogVerbosityLevel,
    GetMainWebApp,
    GetMapThumbnailFile,
    GetMarkdownText,
    GetMe,
    GetMenuButton,
    GetMessage,
    GetMessageAddedReactions,
    GetMessageAvailableReactions,
    GetMessageEffect,
    GetMessageEmbeddingCode,
    GetMessageFileType,
    GetMessageImportConfirmationText,
    GetMessageLink,
    GetMessageLinkInfo,
    GetMessageLocally,
    GetMessageProperties,
    GetMessagePublicForwards,
    GetMessageReadDate,
    GetMessages,
    GetMessageStatistics,
    GetMessageThread,
    GetMessageThreadHistory,
    GetMessageViewers,
    GetNetworkStatistics,
    GetNewChatPrivacySettings,
    GetOption,
    GetOwnedStickerSets,
    GetPassportAuthorizationForm,
    GetPassportAuthorizationFormAvailableElements,
    GetPassportElement,
    GetPasswordState,
    GetPaymentForm,
    GetPaymentReceipt,
    GetPhoneNumberInfo,
    GetPhoneNumberInfoSync,
    GetPollVoters,
    GetPopularWebAppBots,
    GetPreferredCountryLanguage,
    GetPremiumFeatures,
    GetPremiumGiftCodePaymentOptions,
    GetPremiumGiveawayInfo,
    GetPremiumLimit,
    GetPremiumState,
    GetPremiumStickerExamples,
    GetPremiumStickers,
    GetProxies,
    GetProxyLink,
    GetPushReceiverId,
    GetReadDatePrivacySettings,
    GetRecentEmojiStatuses,
    GetRecentInlineBots,
    GetRecentlyOpenedChats,
    GetRecentlyVisitedTMeUrls,
    GetRecentStickers,
    GetRecommendedChatFolders,
    GetRecommendedChats,
    GetRecoveryEmailAddress,
    GetRemoteFile,
    GetRepliedMessage,
    GetSavedAnimations,
    GetSavedMessagesTags,
    GetSavedMessagesTopicHistory,
    GetSavedMessagesTopicMessageByDate,
    GetSavedNotificationSound,
    GetSavedNotificationSounds,
    GetSavedOrderInfo,
    GetScopeNotificationSettings,
    GetSearchedForTags,
    GetSecretChat,
    GetStarAdAccountUrl,
    GetStarGiftPaymentOptions,
    GetStarPaymentOptions,
    GetStarRevenueStatistics,
    GetStarSubscriptions,
    GetStarTransactions,
    GetStarWithdrawalUrl,
    GetStatisticalGraph,
    GetStickerEmojis,
    GetStickers,
    GetStickerSet,
    GetStorageStatistics,
    GetStorageStatisticsFast,
    GetStory,
    GetStoryAvailableReactions,
    GetStoryInteractions,
    GetStoryNotificationSettingsExceptions,
    GetStoryPublicForwards,
    GetStoryStatistics,
    GetSuggestedFileName,
    GetSuggestedStickerSetName,
    GetSuitableDiscussionChats,
    GetSuitablePersonalChats,
    GetSupergroup,
    GetSupergroupFullInfo,
    GetSupergroupMembers,
    GetSupportName,
    GetSupportUser,
    GetTemporaryPasswordState,
    GetTextEntities,
    GetThemedChatEmojiStatuses,
    GetThemedEmojiStatuses,
    GetThemeParametersJsonString,
    GetTimeZones,
    GetTopChats,
    GetTrendingStickerSets,
    GetUser,
    GetUserChatBoosts,
    GetUserFullInfo,
    GetUserLink,
    GetUserPrivacySettingRules,
    GetUserProfilePhotos,
    GetUserSupportInfo,
    GetVideoChatAvailableParticipants,
    GetVideoChatRtmpUrl,
    GetWebAppLinkUrl,
    GetWebAppUrl,
    GetWebPageInstantView,
    HideContactCloseBirthdays,
    HideSuggestedAction,
    ImportContacts,
    ImportMessages,
    InviteGroupCallParticipants,
    JoinChat,
    JoinChatByInviteLink,
    JoinGroupCall,
    LaunchPrepaidPremiumGiveaway,
    LeaveChat,
    LeaveGroupCall,
    LoadActiveStories,
    LoadChats,
    LoadGroupCallParticipants,
    LoadQuickReplyShortcutMessages,
    LoadQuickReplyShortcuts,
    LoadSavedMessagesTopics,
    LogOut,
    OpenChat,
    OpenChatSimilarChat,
    OpenMessageContent,
    OpenStory,
    OpenWebApp,
    OptimizeStorage,
    ParseMarkdown,
    ParseTextEntities,
    PinChatMessage,
    PingProxy,
    PreliminaryUploadFile,
    ProcessChatFolderNewChats,
    ProcessChatJoinRequest,
    ProcessChatJoinRequests,
    ProcessPushNotification,
    RateSpeechRecognition,
    ReadAllChatMentions,
    ReadAllChatReactions,
    ReadAllMessageThreadMentions,
    ReadAllMessageThreadReactions,
    ReadChatList,
    ReaddQuickReplyShortcutMessages,
    ReadFilePart,
    RecognizeSpeech,
    RecoverAuthenticationPassword,
    RecoverPassword,
    RefundStarPayment,
    RegisterDevice,
    RegisterUser,
    RemoveAllFilesFromDownloads,
    RemoveBusinessConnectedBotFromChat,
    RemoveChatActionBar,
    RemoveContacts,
    RemoveFavoriteSticker,
    RemoveFileFromDownloads,
    RemoveInstalledBackground,
    RemoveMessageReaction,
    RemoveNotification,
    RemoveNotificationGroup,
    RemovePendingPaidMessageReactions,
    RemoveProxy,
    RemoveRecentHashtag,
    RemoveRecentlyFoundChat,
    RemoveRecentSticker,
    RemoveSavedAnimation,
    RemoveSavedNotificationSound,
    RemoveSearchedForTag,
    RemoveStickerFromSet,
    RemoveTopChat,
    ReorderActiveUsernames,
    ReorderBotActiveUsernames,
    ReorderBotMediaPreviews,
    ReorderChatFolders,
    ReorderInstalledStickerSets,
    ReorderQuickReplyShortcuts,
    ReorderSupergroupActiveUsernames,
    ReplacePrimaryChatInviteLink,
    ReplaceStickerInSet,
    ReplaceVideoChatRtmpUrl,
    ReportAuthenticationCodeMissing,
    ReportChat,
    ReportChatPhoto,
    ReportChatSponsoredMessage,
    ReportMessageReactions,
    ReportPhoneNumberCodeMissing,
    ReportStory,
    ReportSupergroupAntiSpamFalsePositive,
    ReportSupergroupSpam,
    RequestAuthenticationPasswordRecovery,
    RequestPasswordRecovery,
    RequestQrCodeAuthentication,
    ResendAuthenticationCode,
    ResendEmailAddressVerificationCode,
    ResendLoginEmailAddressCode,
    ResendMessages,
    ResendPhoneNumberCode,
    ResendRecoveryEmailAddressCode,
    ResetAllNotificationSettings,
    ResetAuthenticationEmailAddress,
    ResetInstalledBackgrounds,
    ResetNetworkStatistics,
    ResetPassword,
    ReuseStarSubscription,
    RevokeChatInviteLink,
    RevokeGroupCallInviteLink,
    SaveApplicationLogEvent,
    SearchBackground,
    SearchCallMessages,
    SearchChatMembers,
    SearchChatMessages,
    SearchChatRecentLocationMessages,
    SearchChats,
    SearchChatsNearby,
    SearchChatsOnServer,
    SearchContacts,
    SearchEmojis,
    SearchFileDownloads,
    SearchHashtags,
    SearchInstalledStickerSets,
    SearchMessages,
    SearchOutgoingDocumentMessages,
    SearchPublicChat,
    SearchPublicChats,
    SearchPublicMessagesByTag,
    SearchPublicStoriesByLocation,
    SearchPublicStoriesByTag,
    SearchPublicStoriesByVenue,
    SearchQuote,
    SearchRecentlyFoundChats,
    SearchSavedMessages,
    SearchSecretMessages,
    SearchStickers,
    SearchStickerSet,
    SearchStickerSets,
    SearchStringsByPrefix,
    SearchUserByPhoneNumber,
    SearchUserByToken,
    SearchWebApp,
    SendAuthenticationFirebaseSms,
    SendBotStartMessage,
    SendBusinessMessage,
    SendBusinessMessageAlbum,
    SendCallDebugInformation,
    SendCallLog,
    SendCallRating,
    SendCallSignalingData,
    SendChatAction,
    SendCustomRequest,
    SendEmailAddressVerificationCode,
    SendInlineQueryResultMessage,
    SendMessage,
    SendMessageAlbum,
    SendPassportAuthorizationForm,
    SendPaymentForm,
    SendPhoneNumberCode,
    SendPhoneNumberFirebaseSms,
    SendQuickReplyShortcutMessages,
    SendStory,
    SendWebAppCustomRequest,
    SendWebAppData,
    SetAccentColor,
    SetAccountTtl,
    SetAlarm,
    SetApplicationVerificationToken,
    SetArchiveChatListSettings,
    SetAuthenticationEmailAddress,
    SetAuthenticationPhoneNumber,
    SetAutoDownloadSettings,
    SetAutosaveSettings,
    SetBio,
    SetBirthdate,
    SetBotInfoDescription,
    SetBotInfoShortDescription,
    SetBotName,
    SetBotProfilePhoto,
    SetBotUpdatesStatus,
    SetBusinessAwayMessageSettings,
    SetBusinessConnectedBot,
    SetBusinessGreetingMessageSettings,
    SetBusinessLocation,
    SetBusinessMessageIsPinned,
    SetBusinessOpeningHours,
    SetBusinessStartPage,
    SetChatAccentColor,
    SetChatActiveStoriesList,
    SetChatAvailableReactions,
    SetChatBackground,
    SetChatClientData,
    SetChatDescription,
    SetChatDiscussionGroup,
    SetChatDraftMessage,
    SetChatEmojiStatus,
    SetChatLocation,
    SetChatMemberStatus,
    SetChatMessageAutoDeleteTime,
    SetChatMessageSender,
    SetChatNotificationSettings,
    SetChatPermissions,
    SetChatPhoto,
    SetChatPinnedStories,
    SetChatProfileAccentColor,
    SetChatSlowModeDelay,
    SetChatTheme,
    SetChatTitle,
    SetCloseFriends,
    SetCommands,
    SetCustomEmojiStickerSetThumbnail,
    SetCustomLanguagePack,
    SetCustomLanguagePackString,
    SetDatabaseEncryptionKey,
    SetDefaultBackground,
    SetDefaultChannelAdministratorRights,
    SetDefaultGroupAdministratorRights,
    SetDefaultMessageAutoDeleteTime,
    SetDefaultReactionType,
    SetEmojiStatus,
    SetFileGenerationProgress,
    SetForumTopicNotificationSettings,
    SetGameScore,
    SetGroupCallParticipantIsSpeaking,
    SetGroupCallParticipantVolumeLevel,
    SetGroupCallTitle,
    SetInactiveSessionTtl,
    SetInlineGameScore,
    SetLocation,
    SetLoginEmailAddress,
    SetLogStream,
    SetLogTagVerbosityLevel,
    SetLogVerbosityLevel,
    SetMenuButton,
    SetMessageFactCheck,
    SetMessageReactions,
    SetMessageSenderBlockList,
    SetName,
    SetNetworkType,
    SetNewChatPrivacySettings,
    SetOption,
    SetPassportElement,
    SetPassportElementErrors,
    SetPassword,
    SetPersonalChat,
    SetPinnedChats,
    SetPinnedForumTopics,
    SetPinnedSavedMessagesTopics,
    SetPollAnswer,
    SetProfileAccentColor,
    SetProfilePhoto,
    SetQuickReplyShortcutName,
    SetReactionNotificationSettings,
    SetReadDatePrivacySettings,
    SetRecoveryEmailAddress,
    SetSavedMessagesTagLabel,
    SetScopeNotificationSettings,
    SetStickerEmojis,
    SetStickerKeywords,
    SetStickerMaskPosition,
    SetStickerPositionInSet,
    SetStickerSetThumbnail,
    SetStickerSetTitle,
    SetStoryPrivacySettings,
    SetStoryReaction,
    SetSupergroupCustomEmojiStickerSet,
    SetSupergroupStickerSet,
    SetSupergroupUnrestrictBoostCount,
    SetSupergroupUsername,
    SetTdlibParameters,
    SetUsername,
    SetUserPersonalProfilePhoto,
    SetUserPrivacySettingRules,
    SetUserSupportInfo,
    SetVideoChatDefaultParticipant,
    ShareChatWithBot,
    SharePhoneNumber,
    ShareUsersWithBot,
    StartGroupCallRecording,
    StartGroupCallScreenSharing,
    StartScheduledGroupCall,
    StopBusinessPoll,
    StopPoll,
    SuggestUserProfilePhoto,
    SynchronizeLanguagePack,
    TerminateAllOtherSessions,
    TerminateSession,
    TestCallBytes,
    TestCallEmpty,
    TestCallString,
    TestCallVectorInt,
    TestCallVectorIntObject,
    TestCallVectorString,
    TestCallVectorStringObject,
    TestGetDifference,
    TestNetwork,
    TestProxy,
    TestReturnError,
    TestSquareInt,
    TestUseUpdate,
    ToggleAllDownloadsArePaused,
    ToggleBotIsAddedToAttachmentMenu,
    ToggleBotUsernameIsActive,
    ToggleBusinessConnectedBotChatIsPaused,
    ToggleChatDefaultDisableNotification,
    ToggleChatFolderTags,
    ToggleChatHasProtectedContent,
    ToggleChatIsMarkedAsUnread,
    ToggleChatIsPinned,
    ToggleChatIsTranslatable,
    ToggleChatViewAsTopics,
    ToggleDownloadIsPaused,
    ToggleForumTopicIsClosed,
    ToggleForumTopicIsPinned,
    ToggleGeneralForumTopicIsHidden,
    ToggleGroupCallEnabledStartNotification,
    ToggleGroupCallIsMyVideoEnabled,
    ToggleGroupCallIsMyVideoPaused,
    ToggleGroupCallMuteNewParticipants,
    ToggleGroupCallParticipantIsHandRaised,
    ToggleGroupCallParticipantIsMuted,
    ToggleGroupCallScreenSharingIsPaused,
    ToggleHasSponsoredMessagesEnabled,
    TogglePaidMessageReactionIsAnonymous,
    ToggleSavedMessagesTopicIsPinned,
    ToggleSessionCanAcceptCalls,
    ToggleSessionCanAcceptSecretChats,
    ToggleStoryIsPostedToChatPage,
    ToggleSupergroupCanHaveSponsoredMessages,
    ToggleSupergroupHasAggressiveAntiSpamEnabled,
    ToggleSupergroupHasHiddenMembers,
    ToggleSupergroupIsAllHistoryAvailable,
    ToggleSupergroupIsBroadcastGroup,
    ToggleSupergroupIsForum,
    ToggleSupergroupJoinByRequest,
    ToggleSupergroupJoinToSendMessages,
    ToggleSupergroupSignMessages,
    ToggleSupergroupUsernameIsActive,
    ToggleUsernameIsActive,
    TransferChatOwnership,
    TranslateMessageText,
    TranslateText,
    UnpinAllChatMessages,
    UnpinAllMessageThreadMessages,
    UnpinChatMessage,
    UpgradeBasicGroupChatToSupergroupChat,
    UploadStickerFile,
    ValidateOrderInfo,
    ViewMessages,
    ViewPremiumFeature,
    ViewTrendingStickerSets,
    WriteGeneratedFilePart,
)
from .tdjson import BaseTDJsonClient, TDJsonClient
from .types import (
    AccountTtl,
    AddedReactions,
    AnimatedEmoji,
    Animations,
    ArchiveChatListSettings,
    AttachmentMenuBot,
    AuthenticationCodeInfo,
    AuthorizationState,
    AutoDownloadSettings,
    AutoDownloadSettingsPresets,
    AutosaveSettings,
    AutosaveSettingsScope,
    AvailableReactions,
    Background,
    Backgrounds,
    BackgroundType,
    BankCardInfo,
    BasicGroup,
    BasicGroupFullInfo,
    Birthdate,
    BlockList,
    BotCommand,
    BotCommands,
    BotCommandScope,
    BotMediaPreview,
    BotMediaPreviewInfo,
    BotMediaPreviews,
    BotMenuButton,
    BusinessAwayMessageSettings,
    BusinessChatLink,
    BusinessChatLinkInfo,
    BusinessChatLinks,
    BusinessConnectedBot,
    BusinessConnection,
    BusinessFeature,
    BusinessFeatures,
    BusinessGreetingMessageSettings,
    BusinessLocation,
    BusinessMessage,
    BusinessMessages,
    BusinessOpeningHours,
    CallbackQueryAnswer,
    CallbackQueryPayload,
    CallId,
    CallProblem,
    CallProtocol,
    CanSendMessageToUserResult,
    CanSendStoryResult,
    CanTransferOwnershipResult,
    Chat,
    ChatAction,
    ChatActiveStories,
    ChatAdministratorRights,
    ChatAdministrators,
    ChatAvailableReactions,
    ChatBoostFeatures,
    ChatBoostLevelFeatures,
    ChatBoostLink,
    ChatBoostLinkInfo,
    ChatBoostSlots,
    ChatBoostStatus,
    ChatEventLogFilters,
    ChatEvents,
    ChatFolder,
    ChatFolderIcon,
    ChatFolderInfo,
    ChatFolderInviteLink,
    ChatFolderInviteLinkInfo,
    ChatFolderInviteLinks,
    ChatInviteLink,
    ChatInviteLinkCounts,
    ChatInviteLinkInfo,
    ChatInviteLinkMember,
    ChatInviteLinkMembers,
    ChatInviteLinks,
    ChatJoinRequest,
    ChatJoinRequests,
    ChatList,
    ChatLists,
    ChatLocation,
    ChatMember,
    ChatMembers,
    ChatMembersFilter,
    ChatMemberStatus,
    ChatMessageSenders,
    ChatNotificationSettings,
    ChatPermissions,
    ChatPhotos,
    ChatRevenueStatistics,
    ChatRevenueTransactions,
    Chats,
    ChatsNearby,
    ChatStatistics,
    CheckChatUsernameResult,
    CheckStickerSetNameResult,
    CollectibleItemInfo,
    CollectibleItemType,
    ConnectedWebsites,
    Contact,
    Count,
    Countries,
    CreatedBasicGroupChat,
    CurrentWeather,
    CustomRequestResult,
    DatabaseStatistics,
    DeepLinkInfo,
    DeviceToken,
    DraftMessage,
    EmailAddressAuthentication,
    EmailAddressAuthenticationCodeInfo,
    EmojiCategories,
    EmojiCategoryType,
    EmojiKeywords,
    EmojiReaction,
    Emojis,
    EmojiStatus,
    EmojiStatuses,
    Error,
    FailedToAddMembers,
    File,
    FileDownloadedPrefixSize,
    FilePart,
    FileType,
    FormattedText,
    ForumTopic,
    ForumTopicIcon,
    ForumTopicInfo,
    ForumTopics,
    FoundChatBoosts,
    FoundChatMessages,
    FoundFileDownloads,
    FoundMessages,
    FoundPosition,
    FoundPositions,
    FoundStories,
    FoundUsers,
    FoundWebApp,
    GameHighScores,
    GroupCall,
    GroupCallId,
    GroupCallStreams,
    GroupCallVideoQuality,
    Hashtags,
    HttpUrl,
    ImportedContacts,
    InlineQueryResults,
    InlineQueryResultsButton,
    InputBackground,
    InputBusinessChatLink,
    InputBusinessStartPage,
    InputChatPhoto,
    InputCredentials,
    InputFile,
    InputInlineQueryResult,
    InputInvoice,
    InputMessageContent,
    InputMessageReplyTo,
    InputPassportElement,
    InputPassportElementError,
    InputSticker,
    InputStoryAreas,
    InputStoryContent,
    InputTextQuote,
    InternalLinkType,
    JsonValue,
    LanguagePackInfo,
    LanguagePackString,
    LanguagePackStrings,
    LanguagePackStringValue,
    LinkPreview,
    LinkPreviewOptions,
    LocalizationTargetInfo,
    Location,
    LocationAddress,
    LoginUrlInfo,
    LogStream,
    LogTags,
    LogVerbosityLevel,
    MainWebApp,
    MaskPosition,
    Message,
    MessageAutoDeleteTime,
    MessageCalendar,
    MessageEffect,
    MessageFileType,
    MessageLink,
    MessageLinkInfo,
    MessagePositions,
    MessageProperties,
    MessageReadDate,
    Messages,
    MessageSchedulingState,
    MessageSender,
    MessageSenders,
    MessageSendOptions,
    MessageSource,
    MessageStatistics,
    MessageThreadInfo,
    MessageViewers,
    NetworkStatistics,
    NetworkStatisticsEntry,
    NetworkType,
    NewChatPrivacySettings,
    NotificationSettingsScope,
    NotificationSound,
    NotificationSounds,
    Ok,
    OptionValue,
    OrderInfo,
    PassportAuthorizationForm,
    PassportElement,
    PassportElements,
    PassportElementsWithErrors,
    PassportElementType,
    PasswordState,
    PaymentForm,
    PaymentReceipt,
    PaymentResult,
    PhoneNumberAuthenticationSettings,
    PhoneNumberCodeType,
    PhoneNumberInfo,
    PremiumFeature,
    PremiumFeatures,
    PremiumGiftCodeInfo,
    PremiumGiftCodePaymentOptions,
    PremiumGiveawayInfo,
    PremiumGiveawayParameters,
    PremiumLimit,
    PremiumLimitType,
    PremiumSource,
    PremiumState,
    Proxies,
    Proxy,
    ProxyType,
    PublicChatType,
    PublicForwards,
    PushReceiverId,
    QuickReplyMessage,
    QuickReplyMessages,
    ReactionNotificationSettings,
    ReactionType,
    ReadDatePrivacySettings,
    RecommendedChatFolders,
    RecoveryEmailAddress,
    ReplyMarkup,
    ReportChatSponsoredMessageResult,
    ReportReason,
    ResendCodeReason,
    ResetPasswordResult,
    RtmpUrl,
    SavedMessagesTags,
    ScopeAutosaveSettings,
    ScopeNotificationSettings,
    SearchMessagesFilter,
    Seconds,
    SecretChat,
    SentWebAppMessage,
    Session,
    Sessions,
    ShippingOption,
    SponsoredMessages,
    StarPaymentOptions,
    StarRevenueStatistics,
    StarSubscriptionPricing,
    StarSubscriptions,
    StarTransactionDirection,
    StarTransactions,
    StatisticalGraph,
    Sticker,
    StickerFormat,
    Stickers,
    StickerSet,
    StickerSets,
    StickerType,
    StorageStatistics,
    StorageStatisticsFast,
    StorePaymentPurpose,
    Stories,
    Story,
    StoryFullId,
    StoryInteractions,
    StoryList,
    StoryPrivacySettings,
    StoryStatistics,
    SuggestedAction,
    Supergroup,
    SupergroupFullInfo,
    SupergroupMembersFilter,
    TemporaryPasswordState,
    TestBytes,
    TestInt,
    TestString,
    TestVectorInt,
    TestVectorIntObject,
    TestVectorString,
    TestVectorStringObject,
    Text,
    TextEntities,
    TextParseMode,
    ThemeParameters,
    TimeZones,
    TMeUrls,
    TopChatCategory,
    TrendingStickerSets,
    Update,
    Updates,
    User,
    UserFullInfo,
    UserLink,
    UserPrivacySetting,
    UserPrivacySettingRules,
    Users,
    UserSupportInfo,
    ValidatedOrderInfo,
    WebAppInfo,
    WebPageInstantView,
)

T = TypeVar("T")


class Client:
    def __init__(
        self,
        tdjson_client: BaseTDJsonClient | None = None,
        lib_path: str | None = None,
    ):
        if lib_path is None and tdjson_client is None:
            raise ValueError(
                "`lib_path` and `tdjson_client` is None, you must pass one of it to start"
            )

        self.tdjson_client = tdjson_client or TDJsonClient(lib_path=lib_path)

    async def __call__(self, method: BaseMethod[T], request_timeout: float = 10.0) -> T:
        return await self.tdjson_client.request(method, timeout=request_timeout)

    async def get_authorization_state(
        self,
        request_timeout: float = 10.0,
    ) -> AuthorizationState:
        """
        Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
        :param request_timeout: Request timeout
        """
        return await self(
            GetAuthorizationState(),
            request_timeout=request_timeout,
        )

    async def set_tdlib_parameters(
        self,
        use_test_dc: bool,
        database_directory: str,
        files_directory: str,
        database_encryption_key: bytes,
        use_file_database: bool,
        use_chat_info_database: bool,
        use_message_database: bool,
        use_secret_chats: bool,
        api_id: int,
        api_hash: str,
        system_language_code: str,
        device_model: str,
        system_version: str,
        application_version: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters
        :param use_test_dc: Pass true to use Telegram test environment instead of the production environment
        :param database_directory: The path to the directory for the persistent database; if empty, the current working directory will be used
        :param files_directory: The path to the directory for storing files; if empty, database_directory will be used
        :param database_encryption_key: Encryption key for the database. If the encryption key is invalid, then an error with code 401 will be returned
        :param use_file_database: Pass true to keep information about downloaded and uploaded files between application restarts
        :param use_chat_info_database: Pass true to keep cache of users, basic groups, supergroups, channels and secret chats between restarts. Implies use_file_database
        :param use_message_database: Pass true to keep cache of chats and messages between restarts. Implies use_chat_info_database
        :param use_secret_chats: Pass true to enable support for secret chats
        :param api_id: Application identifier for Telegram API access, which can be obtained at https://my.telegram.org
        :param api_hash: Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org
        :param system_language_code: IETF language tag of the user's operating system language; must be non-empty
        :param device_model: Model of the device the application is being run on; must be non-empty
        :param system_version: Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib
        :param application_version: Application version; must be non-empty
        :param request_timeout: Request timeout
        """
        return await self(
            SetTdlibParameters(
                use_test_dc=use_test_dc,
                database_directory=database_directory,
                files_directory=files_directory,
                database_encryption_key=database_encryption_key,
                use_file_database=use_file_database,
                use_chat_info_database=use_chat_info_database,
                use_message_database=use_message_database,
                use_secret_chats=use_secret_chats,
                api_id=api_id,
                api_hash=api_hash,
                system_language_code=system_language_code,
                device_model=device_model,
                system_version=system_version,
                application_version=application_version,
            ),
            request_timeout=request_timeout,
        )

    async def set_authentication_phone_number(
        self,
        phone_number: str,
        settings: PhoneNumberAuthenticationSettings | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber,
        :param phone_number: The phone number of the user, in international format
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings
        :param request_timeout: Request timeout
        """
        return await self(
            SetAuthenticationPhoneNumber(
                phone_number=phone_number,
                settings=settings,
            ),
            request_timeout=request_timeout,
        )

    async def set_authentication_email_address(
        self,
        email_address: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the email address of the user and sends an authentication code to the email address. Works only when the current authorization state is authorizationStateWaitEmailAddress
        :param email_address: The email address of the user
        :param request_timeout: Request timeout
        """
        return await self(
            SetAuthenticationEmailAddress(
                email_address=email_address,
            ),
            request_timeout=request_timeout,
        )

    async def resend_authentication_code(
        self,
        reason: ResendCodeReason | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Resends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode, the next_code_type of the result is not null
        :param reason: Reason of code resending; pass null if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            ResendAuthenticationCode(
                reason=reason,
            ),
            request_timeout=request_timeout,
        )

    async def check_authentication_email_code(
        self,
        code: EmailAddressAuthentication,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks the authentication of an email address. Works only when the current authorization state is authorizationStateWaitEmailCode
        :param code: Email address authentication to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckAuthenticationEmailCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def check_authentication_code(
        self,
        code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode
        :param code: Authentication code to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckAuthenticationCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def request_qr_code_authentication(
        self,
        other_user_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber,
        :param other_user_ids: List of user identifiers of other users currently using the application
        :param request_timeout: Request timeout
        """
        return await self(
            RequestQrCodeAuthentication(
                other_user_ids=other_user_ids,
            ),
            request_timeout=request_timeout,
        )

    async def register_user(
        self,
        first_name: str,
        last_name: str,
        disable_notification: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration
        :param first_name: The first name of the user; 1-64 characters
        :param last_name: The last name of the user; 0-64 characters
        :param disable_notification: Pass true to disable notification about the current user joining Telegram for other users that added them to contact list
        :param request_timeout: Request timeout
        """
        return await self(
            RegisterUser(
                first_name=first_name,
                last_name=last_name,
                disable_notification=disable_notification,
            ),
            request_timeout=request_timeout,
        )

    async def reset_authentication_email_address(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Resets the login email address. May return an error with a message 'TASK_ALREADY_EXISTS' if reset is still pending.
        :param request_timeout: Request timeout
        """
        return await self(
            ResetAuthenticationEmailAddress(),
            request_timeout=request_timeout,
        )

    async def check_authentication_password(
        self,
        password: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks the 2-step verification password for correctness. Works only when the current authorization state is authorizationStateWaitPassword
        :param password: The 2-step verification password to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckAuthenticationPassword(
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def request_authentication_password_recovery(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Requests to send a 2-step verification password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
        :param request_timeout: Request timeout
        """
        return await self(
            RequestAuthenticationPasswordRecovery(),
            request_timeout=request_timeout,
        )

    async def check_authentication_password_recovery_code(
        self,
        recovery_code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks whether a 2-step verification password recovery code sent to an email address is valid. Works only when the current authorization state is authorizationStateWaitPassword
        :param recovery_code: Recovery code to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckAuthenticationPasswordRecoveryCode(
                recovery_code=recovery_code,
            ),
            request_timeout=request_timeout,
        )

    async def recover_authentication_password(
        self,
        recovery_code: str,
        new_password: str | None = None,
        new_hint: str | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
        :param recovery_code: Recovery code to check
        :param new_password: New 2-step verification password of the user; may be empty to remove the password
        :param new_hint: New password hint; may be empty
        :param request_timeout: Request timeout
        """
        return await self(
            RecoverAuthenticationPassword(
                recovery_code=recovery_code,
                new_password=new_password,
                new_hint=new_hint,
            ),
            request_timeout=request_timeout,
        )

    async def send_authentication_firebase_sms(
        self,
        token: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends Firebase Authentication SMS to the phone number of the user. Works only when the current authorization state is authorizationStateWaitCode and the server returned code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos
        :param token: Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application
        :param request_timeout: Request timeout
        """
        return await self(
            SendAuthenticationFirebaseSms(
                token=token,
            ),
            request_timeout=request_timeout,
        )

    async def report_authentication_code_missing(
        self,
        mobile_network_code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports that authentication code wasn't delivered via SMS; for official mobile applications only. Works only when the current authorization state is authorizationStateWaitCode
        :param mobile_network_code: Current mobile network code
        :param request_timeout: Request timeout
        """
        return await self(
            ReportAuthenticationCodeMissing(
                mobile_network_code=mobile_network_code,
            ),
            request_timeout=request_timeout,
        )

    async def check_authentication_bot_token(
        self,
        token: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in
        :param token: The bot token
        :param request_timeout: Request timeout
        """
        return await self(
            CheckAuthenticationBotToken(
                token=token,
            ),
            request_timeout=request_timeout,
        )

    async def log_out(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Closes the TDLib instance after a proper logout. Requires an available network connection. All local data will be destroyed. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent
        :param request_timeout: Request timeout
        """
        return await self(
            LogOut(),
            request_timeout=request_timeout,
        )

    async def close(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Closes the TDLib instance. All databases will be flushed to disk and properly closed. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent. Can be called before initialization
        :param request_timeout: Request timeout
        """
        return await self(
            Close(),
            request_timeout=request_timeout,
        )

    async def destroy(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Closes the TDLib instance, destroying all local data without a proper logout. The current user session will remain in the list of all active sessions. All local data will be destroyed.
        :param request_timeout: Request timeout
        """
        return await self(
            Destroy(),
            request_timeout=request_timeout,
        )

    async def confirm_qr_code_authentication(
        self,
        link: str,
        request_timeout: float = 10.0,
    ) -> Session:
        """
        Confirms QR code authentication on another device. Returns created session on success
        :param link: A link from a QR code. The link must be scanned by the in-app camera
        :param request_timeout: Request timeout
        """
        return await self(
            ConfirmQrCodeAuthentication(
                link=link,
            ),
            request_timeout=request_timeout,
        )

    async def get_current_state(
        self,
        request_timeout: float = 10.0,
    ) -> Updates:
        """
        Returns all updates needed to restore current TDLib state, i.e. all actual updateAuthorizationState/updateUser/updateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization
        :param request_timeout: Request timeout
        """
        return await self(
            GetCurrentState(),
            request_timeout=request_timeout,
        )

    async def set_database_encryption_key(
        self,
        new_encryption_key: bytes,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain
        :param new_encryption_key: New encryption key
        :param request_timeout: Request timeout
        """
        return await self(
            SetDatabaseEncryptionKey(
                new_encryption_key=new_encryption_key,
            ),
            request_timeout=request_timeout,
        )

    async def get_password_state(
        self,
        request_timeout: float = 10.0,
    ) -> PasswordState:
        """
        Returns the current state of 2-step verification
        :param request_timeout: Request timeout
        """
        return await self(
            GetPasswordState(),
            request_timeout=request_timeout,
        )

    async def set_password(
        self,
        old_password: str,
        set_recovery_email_address: bool,
        new_password: str | None = None,
        new_hint: str | None = None,
        new_recovery_email_address: str | None = None,
        request_timeout: float = 10.0,
    ) -> PasswordState:
        """
        Changes the 2-step verification password for the current user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed
        :param old_password: Previous 2-step verification password of the user
        :param set_recovery_email_address: Pass true to change also the recovery email address
        :param new_password: New 2-step verification password of the user; may be empty to remove the password
        :param new_hint: New password hint; may be empty
        :param new_recovery_email_address: New recovery email address; may be empty
        :param request_timeout: Request timeout
        """
        return await self(
            SetPassword(
                old_password=old_password,
                set_recovery_email_address=set_recovery_email_address,
                new_password=new_password,
                new_hint=new_hint,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_timeout=request_timeout,
        )

    async def set_login_email_address(
        self,
        new_login_email_address: str,
        request_timeout: float = 10.0,
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Changes the login email address of the user. The email address can be changed only if the current user already has login email and passwordState.login_email_address_pattern is non-empty.
        :param new_login_email_address: New login email address
        :param request_timeout: Request timeout
        """
        return await self(
            SetLoginEmailAddress(
                new_login_email_address=new_login_email_address,
            ),
            request_timeout=request_timeout,
        )

    async def resend_login_email_address_code(
        self,
        request_timeout: float = 10.0,
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Resends the login email address verification code
        :param request_timeout: Request timeout
        """
        return await self(
            ResendLoginEmailAddressCode(),
            request_timeout=request_timeout,
        )

    async def check_login_email_address_code(
        self,
        code: EmailAddressAuthentication,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks the login email address authentication
        :param code: Email address authentication to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckLoginEmailAddressCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def get_recovery_email_address(
        self,
        password: str,
        request_timeout: float = 10.0,
    ) -> RecoveryEmailAddress:
        """
        Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user
        :param password: The 2-step verification password for the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecoveryEmailAddress(
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def set_recovery_email_address(
        self,
        password: str,
        new_recovery_email_address: str,
        request_timeout: float = 10.0,
    ) -> PasswordState:
        """
        Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed.
        :param password: The 2-step verification password of the current user
        :param new_recovery_email_address: New recovery email address
        :param request_timeout: Request timeout
        """
        return await self(
            SetRecoveryEmailAddress(
                password=password,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_timeout=request_timeout,
        )

    async def check_recovery_email_address_code(
        self,
        code: str,
        request_timeout: float = 10.0,
    ) -> PasswordState:
        """
        Checks the 2-step verification recovery email address verification code
        :param code: Verification code to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckRecoveryEmailAddressCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def resend_recovery_email_address_code(
        self,
        request_timeout: float = 10.0,
    ) -> PasswordState:
        """
        Resends the 2-step verification recovery email address verification code
        :param request_timeout: Request timeout
        """
        return await self(
            ResendRecoveryEmailAddressCode(),
            request_timeout=request_timeout,
        )

    async def cancel_recovery_email_address_verification(
        self,
        request_timeout: float = 10.0,
    ) -> PasswordState:
        """
        Cancels verification of the 2-step verification recovery email address
        :param request_timeout: Request timeout
        """
        return await self(
            CancelRecoveryEmailAddressVerification(),
            request_timeout=request_timeout,
        )

    async def request_password_recovery(
        self,
        request_timeout: float = 10.0,
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Requests to send a 2-step verification password recovery code to an email address that was previously set up
        :param request_timeout: Request timeout
        """
        return await self(
            RequestPasswordRecovery(),
            request_timeout=request_timeout,
        )

    async def check_password_recovery_code(
        self,
        recovery_code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks whether a 2-step verification password recovery code sent to an email address is valid
        :param recovery_code: Recovery code to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckPasswordRecoveryCode(
                recovery_code=recovery_code,
            ),
            request_timeout=request_timeout,
        )

    async def recover_password(
        self,
        recovery_code: str,
        new_password: str | None = None,
        new_hint: str | None = None,
        request_timeout: float = 10.0,
    ) -> PasswordState:
        """
        Recovers the 2-step verification password using a recovery code sent to an email address that was previously set up
        :param recovery_code: Recovery code to check
        :param new_password: New 2-step verification password of the user; may be empty to remove the password
        :param new_hint: New password hint; may be empty
        :param request_timeout: Request timeout
        """
        return await self(
            RecoverPassword(
                recovery_code=recovery_code,
                new_password=new_password,
                new_hint=new_hint,
            ),
            request_timeout=request_timeout,
        )

    async def reset_password(
        self,
        request_timeout: float = 10.0,
    ) -> ResetPasswordResult:
        """
        Removes 2-step verification password without previous password and access to recovery email address. The password can't be reset immediately and the request needs to be repeated after the specified time
        :param request_timeout: Request timeout
        """
        return await self(
            ResetPassword(),
            request_timeout=request_timeout,
        )

    async def cancel_password_reset(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0
        :param request_timeout: Request timeout
        """
        return await self(
            CancelPasswordReset(),
            request_timeout=request_timeout,
        )

    async def create_temporary_password(
        self,
        password: str,
        valid_for: int,
        request_timeout: float = 10.0,
    ) -> TemporaryPasswordState:
        """
        Creates a new temporary password for processing payments
        :param password: The 2-step verification password of the current user
        :param valid_for: Time during which the temporary password will be valid, in seconds; must be between 60 and 86400
        :param request_timeout: Request timeout
        """
        return await self(
            CreateTemporaryPassword(
                password=password,
                valid_for=valid_for,
            ),
            request_timeout=request_timeout,
        )

    async def get_temporary_password_state(
        self,
        request_timeout: float = 10.0,
    ) -> TemporaryPasswordState:
        """
        Returns information about the current temporary password
        :param request_timeout: Request timeout
        """
        return await self(
            GetTemporaryPasswordState(),
            request_timeout=request_timeout,
        )

    async def get_me(
        self,
        request_timeout: float = 10.0,
    ) -> User:
        """
        Returns the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetMe(),
            request_timeout=request_timeout,
        )

    async def get_user(
        self,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> User:
        """
        Returns information about a user by their identifier. This is an offline request if the current user is not a bot
        :param user_id: User identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetUser(
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_user_full_info(
        self,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> UserFullInfo:
        """
        Returns full information about a user by their identifier
        :param user_id: User identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetUserFullInfo(
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_basic_group(
        self,
        basic_group_id: int,
        request_timeout: float = 10.0,
    ) -> BasicGroup:
        """
        Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot
        :param basic_group_id: Basic group identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetBasicGroup(
                basic_group_id=basic_group_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_basic_group_full_info(
        self,
        basic_group_id: int,
        request_timeout: float = 10.0,
    ) -> BasicGroupFullInfo:
        """
        Returns full information about a basic group by its identifier
        :param basic_group_id: Basic group identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetBasicGroupFullInfo(
                basic_group_id=basic_group_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_supergroup(
        self,
        supergroup_id: int,
        request_timeout: float = 10.0,
    ) -> Supergroup:
        """
        Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot
        :param supergroup_id: Supergroup or channel identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetSupergroup(
                supergroup_id=supergroup_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_supergroup_full_info(
        self,
        supergroup_id: int,
        request_timeout: float = 10.0,
    ) -> SupergroupFullInfo:
        """
        Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute
        :param supergroup_id: Supergroup or channel identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetSupergroupFullInfo(
                supergroup_id=supergroup_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_secret_chat(
        self,
        secret_chat_id: int,
        request_timeout: float = 10.0,
    ) -> SecretChat:
        """
        Returns information about a secret chat by its identifier. This is an offline request
        :param secret_chat_id: Secret chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetSecretChat(
                secret_chat_id=secret_chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Returns information about a chat by its identifier; this is an offline request if the current user is not a bot
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_message(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Returns information about a message
        :param chat_id: Identifier of the chat the message belongs to
        :param message_id: Identifier of the message to get
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_locally(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Returns information about a message, if it is available without sending network request. This is an offline request
        :param chat_id: Identifier of the chat the message belongs to
        :param message_id: Identifier of the message to get
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageLocally(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_replied_message(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Returns information about a non-bundled message that is replied by a given message. Also, returns the pinned message, the game message, the invoice message,
        :param chat_id: Identifier of the chat the message belongs to
        :param message_id: Identifier of the reply message
        :param request_timeout: Request timeout
        """
        return await self(
            GetRepliedMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_pinned_message(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Returns information about a newest pinned message in the chat
        :param chat_id: Identifier of the chat the message belongs to
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatPinnedMessage(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_callback_query_message(
        self,
        chat_id: int,
        message_id: int,
        callback_query_id: int,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Returns information about a message with the callback button that originated a callback query; for bots only
        :param chat_id: Identifier of the chat the message belongs to
        :param message_id: Message identifier
        :param callback_query_id: Identifier of the callback query
        :param request_timeout: Request timeout
        """
        return await self(
            GetCallbackQueryMessage(
                chat_id=chat_id,
                message_id=message_id,
                callback_query_id=callback_query_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_messages(
        self,
        chat_id: int,
        message_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Returns information about messages. If a message is not found, returns null on the corresponding position of the result
        :param chat_id: Identifier of the chat the messages belong to
        :param message_ids: Identifiers of the messages to get
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessages(
                chat_id=chat_id,
                message_ids=message_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_properties(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> MessageProperties:
        """
        Returns properties of a message; this is an offline request
        :param chat_id: Chat identifier
        :param message_id: Identifier of the message
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageProperties(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_thread(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> MessageThreadInfo:
        """
        Returns information about a message thread. Can be used only if messageProperties.can_get_message_thread == true
        :param chat_id: Chat identifier
        :param message_id: Identifier of the message
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageThread(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_read_date(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> MessageReadDate:
        """
        Returns read date of a recent outgoing message in a private chat. The method can be called if messageProperties.can_get_read_date == true
        :param chat_id: Chat identifier
        :param message_id: Identifier of the message
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageReadDate(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_viewers(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> MessageViewers:
        """
        Returns viewers of a recent outgoing message in a basic group or a supergroup chat. For video notes and voice notes only users, opened content of the message, are returned. The method can be called if messageProperties.can_get_viewers == true
        :param chat_id: Chat identifier
        :param message_id: Identifier of the message
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageViewers(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_file(
        self,
        file_id: int,
        request_timeout: float = 10.0,
    ) -> File:
        """
        Returns information about a file; this is an offline request
        :param file_id: Identifier of the file to get
        :param request_timeout: Request timeout
        """
        return await self(
            GetFile(
                file_id=file_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_remote_file(
        self,
        remote_file_id: str,
        file_type: FileType | None = None,
        request_timeout: float = 10.0,
    ) -> File:
        """
        Returns information about a file by its remote identifier; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user.
        :param remote_file_id: Remote identifier of the file to get
        :param file_type: File type; pass null if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            GetRemoteFile(
                remote_file_id=remote_file_id,
                file_type=file_type,
            ),
            request_timeout=request_timeout,
        )

    async def load_chats(
        self,
        limit: int,
        chat_list: ChatList | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded
        :param limit: The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
        :param chat_list: The chat list in which to load chats; pass null to load chats from the main chat list
        :param request_timeout: Request timeout
        """
        return await self(
            LoadChats(
                limit=limit,
                chat_list=chat_list,
            ),
            request_timeout=request_timeout,
        )

    async def get_chats(
        self,
        limit: int,
        chat_list: ChatList | None = None,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats and updates processing instead to maintain chat lists in a consistent state
        :param limit: The maximum number of chats to be returned
        :param chat_list: The chat list in which to return chats; pass null to get chats from the main chat list
        :param request_timeout: Request timeout
        """
        return await self(
            GetChats(
                limit=limit,
                chat_list=chat_list,
            ),
            request_timeout=request_timeout,
        )

    async def search_public_chat(
        self,
        username: str,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Searches a public chat by its username. Currently, only private chats, supergroups and channels can be public. Returns the chat if found; otherwise, an error is returned
        :param username: Username to be resolved
        :param request_timeout: Request timeout
        """
        return await self(
            SearchPublicChat(
                username=username,
            ),
            request_timeout=request_timeout,
        )

    async def search_public_chats(
        self,
        query: str,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Searches public chats by looking for specified query in their username and title. Currently, only private chats, supergroups and channels can be public. Returns a meaningful number of results.
        :param query: Query to search for
        :param request_timeout: Request timeout
        """
        return await self(
            SearchPublicChats(
                query=query,
            ),
            request_timeout=request_timeout,
        )

    async def search_chats(
        self,
        query: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats; this is an offline request. Returns chats in the order seen in the main chat list
        :param query: Query to search for. If the query is empty, returns up to 50 recently found chats
        :param limit: The maximum number of chats to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            SearchChats(
                query=query,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_chats_on_server(
        self,
        query: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the main chat list
        :param query: Query to search for
        :param limit: The maximum number of chats to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            SearchChatsOnServer(
                query=query,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_chats_nearby(
        self,
        location: Location,
        request_timeout: float = 10.0,
    ) -> ChatsNearby:
        """
        Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby.
        :param location: Current user location
        :param request_timeout: Request timeout
        """
        return await self(
            SearchChatsNearby(
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def get_recommended_chats(
        self,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of channel chats recommended to the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecommendedChats(),
            request_timeout=request_timeout,
        )

    async def get_chat_similar_chats(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of chats similar to the given chat
        :param chat_id: Identifier of the target chat; must be an identifier of a channel chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatSimilarChats(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_similar_chat_count(
        self,
        chat_id: int,
        return_local: bool,
        request_timeout: float = 10.0,
    ) -> Count:
        """
        Returns approximate number of chats similar to the given chat
        :param chat_id: Identifier of the target chat; must be an identifier of a channel chat
        :param return_local: Pass true to get the number of chats without sending network requests, or -1 if the number of chats is unknown locally
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatSimilarChatCount(
                chat_id=chat_id,
                return_local=return_local,
            ),
            request_timeout=request_timeout,
        )

    async def open_chat_similar_chat(
        self,
        chat_id: int,
        opened_chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that a chat was opened from the list of similar chats. The method is independent of openChat and closeChat methods
        :param chat_id: Identifier of the original chat, which similar chats were requested
        :param opened_chat_id: Identifier of the opened chat
        :param request_timeout: Request timeout
        """
        return await self(
            OpenChatSimilarChat(
                chat_id=chat_id,
                opened_chat_id=opened_chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_top_chats(
        self,
        category: TopChatCategory,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of frequently used chats
        :param category: Category of chats to be returned
        :param limit: The maximum number of chats to be returned; up to 30
        :param request_timeout: Request timeout
        """
        return await self(
            GetTopChats(
                category=category,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def remove_top_chat(
        self,
        category: TopChatCategory,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled
        :param category: Category of frequently used chats
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveTopChat(
                category=category,
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def search_recently_found_chats(
        self,
        query: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Searches for the specified query in the title and username of up to 50 recently found chats; this is an offline request
        :param query: Query to search for
        :param limit: The maximum number of chats to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            SearchRecentlyFoundChats(
                query=query,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def add_recently_found_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first
        :param chat_id: Identifier of the chat to add
        :param request_timeout: Request timeout
        """
        return await self(
            AddRecentlyFoundChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def remove_recently_found_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a chat from the list of recently found chats
        :param chat_id: Identifier of the chat to be removed
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveRecentlyFoundChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def clear_recently_found_chats(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears the list of recently found chats
        :param request_timeout: Request timeout
        """
        return await self(
            ClearRecentlyFoundChats(),
            request_timeout=request_timeout,
        )

    async def get_recently_opened_chats(
        self,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns recently opened chats; this is an offline request. Returns chats in the order of last opening
        :param limit: The maximum number of chats to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecentlyOpenedChats(
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def check_chat_username(
        self,
        chat_id: int,
        username: str,
        request_timeout: float = 10.0,
    ) -> CheckChatUsernameResult:
        """
        Checks whether a username can be set for a chat
        :param chat_id: Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or 0 if the chat is being created
        :param username: Username to be checked
        :param request_timeout: Request timeout
        """
        return await self(
            CheckChatUsername(
                chat_id=chat_id,
                username=username,
            ),
            request_timeout=request_timeout,
        )

    async def get_created_public_chats(
        self,
        type: PublicChatType,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of public chats of the specified type, owned by the user
        :param type: Type of the public chats to return
        :param request_timeout: Request timeout
        """
        return await self(
            GetCreatedPublicChats(
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def check_created_public_chats_limit(
        self,
        type: PublicChatType,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached. The limit can be increased with Telegram Premium
        :param type: Type of the public chats, for which to check the limit
        :param request_timeout: Request timeout
        """
        return await self(
            CheckCreatedPublicChatsLimit(
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def get_suitable_discussion_chats(
        self,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group.
        :param request_timeout: Request timeout
        """
        return await self(
            GetSuitableDiscussionChats(),
            request_timeout=request_timeout,
        )

    async def get_inactive_supergroup_chats(
        self,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error. Also, the limit can be increased with Telegram Premium
        :param request_timeout: Request timeout
        """
        return await self(
            GetInactiveSupergroupChats(),
            request_timeout=request_timeout,
        )

    async def get_suitable_personal_chats(
        self,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of channel chats, which can be used as a personal chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetSuitablePersonalChats(),
            request_timeout=request_timeout,
        )

    async def load_saved_messages_topics(
        self,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Loads more Saved Messages topics. The loaded topics will be sent through updateSavedMessagesTopic. Topics are sorted by their topic.order in descending order. Returns a 404 error if all topics have been loaded
        :param limit: The maximum number of topics to be loaded. For optimal performance, the number of loaded topics is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
        :param request_timeout: Request timeout
        """
        return await self(
            LoadSavedMessagesTopics(
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_saved_messages_topic_history(
        self,
        saved_messages_topic_id: int,
        from_message_id: int,
        offset: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Returns messages in a Saved Messages topic. The messages are returned in reverse chronological order (i.e., in order of decreasing message_id)
        :param saved_messages_topic_id: Identifier of Saved Messages topic which messages will be fetched
        :param from_message_id: Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message
        :param offset: Specify 0 to get results from exactly the message from_message_id or a negative offset up to 99 to get additionally some newer messages
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset.
        :param request_timeout: Request timeout
        """
        return await self(
            GetSavedMessagesTopicHistory(
                saved_messages_topic_id=saved_messages_topic_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_saved_messages_topic_message_by_date(
        self,
        saved_messages_topic_id: int,
        date: int,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Returns the last message sent in a Saved Messages topic no later than the specified date
        :param saved_messages_topic_id: Identifier of Saved Messages topic which message will be returned
        :param date: Point in time (Unix timestamp) relative to which to search for messages
        :param request_timeout: Request timeout
        """
        return await self(
            GetSavedMessagesTopicMessageByDate(
                saved_messages_topic_id=saved_messages_topic_id,
                date=date,
            ),
            request_timeout=request_timeout,
        )

    async def delete_saved_messages_topic_history(
        self,
        saved_messages_topic_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all messages in a Saved Messages topic
        :param saved_messages_topic_id: Identifier of Saved Messages topic which messages will be deleted
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteSavedMessagesTopicHistory(
                saved_messages_topic_id=saved_messages_topic_id,
            ),
            request_timeout=request_timeout,
        )

    async def delete_saved_messages_topic_messages_by_date(
        self,
        saved_messages_topic_id: int,
        min_date: int,
        max_date: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all messages between the specified dates in a Saved Messages topic. Messages sent in the last 30 seconds will not be deleted
        :param saved_messages_topic_id: Identifier of Saved Messages topic which messages will be deleted
        :param min_date: The minimum date of the messages to delete
        :param max_date: The maximum date of the messages to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteSavedMessagesTopicMessagesByDate(
                saved_messages_topic_id=saved_messages_topic_id,
                min_date=min_date,
                max_date=max_date,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_saved_messages_topic_is_pinned(
        self,
        saved_messages_topic_id: int,
        is_pinned: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the pinned state of a Saved Messages topic. There can be up to getOption('pinned_saved_messages_topic_count_max') pinned topics. The limit can be increased with Telegram Premium
        :param saved_messages_topic_id: Identifier of Saved Messages topic to pin or unpin
        :param is_pinned: Pass true to pin the topic; pass false to unpin it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSavedMessagesTopicIsPinned(
                saved_messages_topic_id=saved_messages_topic_id,
                is_pinned=is_pinned,
            ),
            request_timeout=request_timeout,
        )

    async def set_pinned_saved_messages_topics(
        self,
        saved_messages_topic_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the order of pinned Saved Messages topics
        :param saved_messages_topic_ids: Identifiers of the new pinned Saved Messages topics
        :param request_timeout: Request timeout
        """
        return await self(
            SetPinnedSavedMessagesTopics(
                saved_messages_topic_ids=saved_messages_topic_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_groups_in_common(
        self,
        user_id: int,
        offset_chat_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns a list of common group chats with a given user. Chats are sorted by their type and creation date
        :param user_id: User identifier
        :param offset_chat_id: Chat identifier starting from which to return chats; use 0 for the first request
        :param limit: The maximum number of chats to be returned; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            GetGroupsInCommon(
                user_id=user_id,
                offset_chat_id=offset_chat_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_history(
        self,
        chat_id: int,
        from_message_id: int,
        offset: int,
        limit: int,
        only_local: bool,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Returns messages in a chat. The messages are returned in reverse chronological order (i.e., in order of decreasing message_id).
        :param chat_id: Chat identifier
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :param offset: Specify 0 to get results from exactly the message from_message_id or a negative offset up to 99 to get additionally some newer messages
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset.
        :param only_local: Pass true to get only messages that are available without sending network requests
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatHistory(
                chat_id=chat_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                only_local=only_local,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_thread_history(
        self,
        chat_id: int,
        message_id: int,
        from_message_id: int,
        offset: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Returns messages in a message thread of a message. Can be used only if messageProperties.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup.
        :param chat_id: Chat identifier
        :param message_id: Message identifier, which thread history needs to be returned
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :param offset: Specify 0 to get results from exactly the message from_message_id or a negative offset up to 99 to get additionally some newer messages
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset.
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageThreadHistory(
                chat_id=chat_id,
                message_id=message_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat_history(
        self,
        chat_id: int,
        remove_from_chat_list: bool,
        revoke: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all messages in the chat. Use chat.can_be_deleted_only_for_self and chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat
        :param chat_id: Chat identifier
        :param remove_from_chat_list: Pass true to remove the chat from all chat lists
        :param revoke: Pass true to delete chat history for all users
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChatHistory(
                chat_id=chat_id,
                remove_from_chat_list=remove_from_chat_list,
                revoke=revoke,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes a chat along with all messages in the corresponding chat for all chat members. For group chats this will release the usernames and remove all members.
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def search_chat_messages(
        self,
        chat_id: int,
        query: str,
        from_message_id: int,
        offset: int,
        limit: int,
        message_thread_id: int,
        saved_messages_topic_id: int,
        sender_id: MessageSender | None = None,
        filter: SearchMessagesFilter | None = None,
        request_timeout: float = 10.0,
    ) -> FoundChatMessages:
        """
        Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query
        :param chat_id: Identifier of the chat in which to search messages
        :param query: Query to search for
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :param offset: Specify 0 to get results from exactly the message from_message_id or a negative offset to get the specified message and some newer messages
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset.
        :param message_thread_id: If not 0, only messages in the specified thread will be returned; supergroups only
        :param saved_messages_topic_id: If not 0, only messages in the specified Saved Messages topic will be returned; pass 0 to return all messages, or for chats other than Saved Messages
        :param sender_id: Identifier of the sender of messages to search for; pass null to search for messages from any sender. Not supported in secret chats
        :param filter: Additional filter for messages to search; pass null to search for all messages
        :param request_timeout: Request timeout
        """
        return await self(
            SearchChatMessages(
                chat_id=chat_id,
                query=query,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                message_thread_id=message_thread_id,
                saved_messages_topic_id=saved_messages_topic_id,
                sender_id=sender_id,
                filter=filter,
            ),
            request_timeout=request_timeout,
        )

    async def search_messages(
        self,
        only_in_channels: bool,
        query: str,
        offset: str,
        limit: int,
        min_date: int,
        max_date: int,
        chat_list: ChatList | None = None,
        filter: SearchMessagesFilter | None = None,
        request_timeout: float = 10.0,
    ) -> FoundMessages:
        """
        Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)).
        :param only_in_channels: Pass true to search only for messages in channels
        :param query: Query to search for
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :param min_date: If not 0, the minimum date of the messages to return
        :param max_date: If not 0, the maximum date of the messages to return
        :param chat_list: Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported
        :param filter: Additional filter for messages to search; pass null to search for all messages. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function
        :param request_timeout: Request timeout
        """
        return await self(
            SearchMessages(
                only_in_channels=only_in_channels,
                query=query,
                offset=offset,
                limit=limit,
                min_date=min_date,
                max_date=max_date,
                chat_list=chat_list,
                filter=filter,
            ),
            request_timeout=request_timeout,
        )

    async def search_secret_messages(
        self,
        chat_id: int,
        query: str,
        offset: str,
        limit: int,
        filter: SearchMessagesFilter | None = None,
        request_timeout: float = 10.0,
    ) -> FoundMessages:
        """
        Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib
        :param chat_id: Identifier of the chat in which to search. Specify 0 to search in all secret chats
        :param query: Query to search for. If empty, searchChatMessages must be used instead
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :param filter: Additional filter for messages to search; pass null to search for all messages
        :param request_timeout: Request timeout
        """
        return await self(
            SearchSecretMessages(
                chat_id=chat_id,
                query=query,
                offset=offset,
                limit=limit,
                filter=filter,
            ),
            request_timeout=request_timeout,
        )

    async def search_saved_messages(
        self,
        saved_messages_topic_id: int,
        query: str,
        from_message_id: int,
        offset: int,
        limit: int,
        tag: ReactionType | None = None,
        request_timeout: float = 10.0,
    ) -> FoundChatMessages:
        """
        Searches for messages tagged by the given reaction and with the given words in the Saved Messages chat; for Telegram Premium users only.
        :param saved_messages_topic_id: If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages
        :param query: Query to search for
        :param from_message_id: Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message
        :param offset: Specify 0 to get results from exactly the message from_message_id or a negative offset to get the specified message and some newer messages
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset.
        :param tag: Tag to search for; pass null to return all suitable messages
        :param request_timeout: Request timeout
        """
        return await self(
            SearchSavedMessages(
                saved_messages_topic_id=saved_messages_topic_id,
                query=query,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                tag=tag,
            ),
            request_timeout=request_timeout,
        )

    async def search_call_messages(
        self,
        offset: str,
        limit: int,
        only_missed: bool,
        request_timeout: float = 10.0,
    ) -> FoundMessages:
        """
        Searches for call messages. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :param only_missed: Pass true to search only for messages with missed/declined calls
        :param request_timeout: Request timeout
        """
        return await self(
            SearchCallMessages(
                offset=offset,
                limit=limit,
                only_missed=only_missed,
            ),
            request_timeout=request_timeout,
        )

    async def search_outgoing_document_messages(
        self,
        query: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> FoundMessages:
        """
        Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order
        :param query: Query to search for in document file name and message caption
        :param limit: The maximum number of messages to be returned; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            SearchOutgoingDocumentMessages(
                query=query,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_public_messages_by_tag(
        self,
        tag: str,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> FoundMessages:
        """
        Searches for public channel posts containing the given hashtag or cashtag. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :param tag: Hashtag or cashtag to search for
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            SearchPublicMessagesByTag(
                tag=tag,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_public_stories_by_tag(
        self,
        tag: str,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> FoundStories:
        """
        Searches for public stories containing the given hashtag or cashtag. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :param tag: Hashtag or cashtag to search for
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            SearchPublicStoriesByTag(
                tag=tag,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_public_stories_by_location(
        self,
        address: LocationAddress,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> FoundStories:
        """
        Searches for public stories by the given address location. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :param address: Address of the location
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            SearchPublicStoriesByLocation(
                address=address,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_public_stories_by_venue(
        self,
        venue_provider: str,
        venue_id: str,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> FoundStories:
        """
        Searches for public stories from the given venue. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :param venue_provider: Provider of the venue
        :param venue_id: Identifier of the venue in the provider database
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            SearchPublicStoriesByVenue(
                venue_provider=venue_provider,
                venue_id=venue_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_searched_for_tags(
        self,
        tag_prefix: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Hashtags:
        """
        Returns recently searched for hashtags or cashtags by their prefix
        :param tag_prefix: Prefix of hashtags or cashtags to return
        :param limit: The maximum number of items to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            GetSearchedForTags(
                tag_prefix=tag_prefix,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def remove_searched_for_tag(
        self,
        tag: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a hashtag or a cashtag from the list of recently searched for hashtags or cashtags
        :param tag: Hashtag or cashtag to delete
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveSearchedForTag(
                tag=tag,
            ),
            request_timeout=request_timeout,
        )

    async def clear_searched_for_tags(
        self,
        clear_cashtags: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears the list of recently searched for hashtags or cashtags
        :param clear_cashtags: Pass true to clear the list of recently searched for cashtags; otherwise, the list of recently searched for hashtags will be cleared
        :param request_timeout: Request timeout
        """
        return await self(
            ClearSearchedForTags(
                clear_cashtags=clear_cashtags,
            ),
            request_timeout=request_timeout,
        )

    async def delete_all_call_messages(
        self,
        revoke: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all call messages
        :param revoke: Pass true to delete the messages for all users
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteAllCallMessages(
                revoke=revoke,
            ),
            request_timeout=request_timeout,
        )

    async def search_chat_recent_location_messages(
        self,
        chat_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user
        :param chat_id: Chat identifier
        :param limit: The maximum number of messages to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            SearchChatRecentLocationMessages(
                chat_id=chat_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_message_by_date(
        self,
        chat_id: int,
        date: int,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Returns the last message sent in a chat no later than the specified date
        :param chat_id: Chat identifier
        :param date: Point in time (Unix timestamp) relative to which to search for messages
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatMessageByDate(
                chat_id=chat_id,
                date=date,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_sparse_message_positions(
        self,
        chat_id: int,
        filter: SearchMessagesFilter,
        from_message_id: int,
        limit: int,
        saved_messages_topic_id: int,
        request_timeout: float = 10.0,
    ) -> MessagePositions:
        """
        Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id).
        :param chat_id: Identifier of the chat in which to return information about message positions
        :param filter: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        :param from_message_id: The message identifier from which to return information about message positions
        :param limit: The expected number of message positions to be returned; 50-2000. A smaller number of positions can be returned, if there are not enough appropriate messages
        :param saved_messages_topic_id: If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages, or for chats other than Saved Messages
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatSparseMessagePositions(
                chat_id=chat_id,
                filter=filter,
                from_message_id=from_message_id,
                limit=limit,
                saved_messages_topic_id=saved_messages_topic_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_message_calendar(
        self,
        chat_id: int,
        filter: SearchMessagesFilter,
        from_message_id: int,
        saved_messages_topic_id: int,
        request_timeout: float = 10.0,
    ) -> MessageCalendar:
        """
        Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option 'utc_time_offset'
        :param chat_id: Identifier of the chat in which to return information about messages
        :param filter: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        :param from_message_id: The message identifier from which to return information about messages; use 0 to get results from the last message
        :param saved_messages_topic_id: If not0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages, or for chats other than Saved Messages
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatMessageCalendar(
                chat_id=chat_id,
                filter=filter,
                from_message_id=from_message_id,
                saved_messages_topic_id=saved_messages_topic_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_message_count(
        self,
        chat_id: int,
        filter: SearchMessagesFilter,
        saved_messages_topic_id: int,
        return_local: bool,
        request_timeout: float = 10.0,
    ) -> Count:
        """
        Returns approximate number of messages of the specified type in the chat
        :param chat_id: Identifier of the chat in which to count messages
        :param filter: Filter for message content; searchMessagesFilterEmpty is unsupported in this function
        :param saved_messages_topic_id: If not 0, only messages in the specified Saved Messages topic will be counted; pass 0 to count all messages, or for chats other than Saved Messages
        :param return_local: Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatMessageCount(
                chat_id=chat_id,
                filter=filter,
                saved_messages_topic_id=saved_messages_topic_id,
                return_local=return_local,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_message_position(
        self,
        chat_id: int,
        message_id: int,
        filter: SearchMessagesFilter,
        message_thread_id: int,
        saved_messages_topic_id: int,
        request_timeout: float = 10.0,
    ) -> Count:
        """
        Returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat. Cannot be used in secret chats
        :param chat_id: Identifier of the chat in which to find message position
        :param message_id: Message identifier
        :param filter: Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function
        :param message_thread_id: If not 0, only messages in the specified thread will be considered; supergroups only
        :param saved_messages_topic_id: If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all relevant messages, or for chats other than Saved Messages
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatMessagePosition(
                chat_id=chat_id,
                message_id=message_id,
                filter=filter,
                message_thread_id=message_thread_id,
                saved_messages_topic_id=saved_messages_topic_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_scheduled_messages(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Returns all scheduled messages in a chat. The messages are returned in reverse chronological order (i.e., in order of decreasing message_id)
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatScheduledMessages(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_sponsored_messages(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> SponsoredMessages:
        """
        Returns sponsored messages to be shown in a chat; for channel chats only
        :param chat_id: Identifier of the chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatSponsoredMessages(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def click_chat_sponsored_message(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that the user opened the sponsored chat via the button, the name, the photo, or a mention in the sponsored message
        :param chat_id: Chat identifier of the sponsored message
        :param message_id: Identifier of the sponsored message
        :param request_timeout: Request timeout
        """
        return await self(
            ClickChatSponsoredMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def report_chat_sponsored_message(
        self,
        chat_id: int,
        message_id: int,
        option_id: bytes,
        request_timeout: float = 10.0,
    ) -> ReportChatSponsoredMessageResult:
        """
        Reports a sponsored message to Telegram moderators
        :param chat_id: Chat identifier of the sponsored message
        :param message_id: Identifier of the sponsored message
        :param option_id: Option identifier chosen by the user; leave empty for the initial request
        :param request_timeout: Request timeout
        """
        return await self(
            ReportChatSponsoredMessage(
                chat_id=chat_id,
                message_id=message_id,
                option_id=option_id,
            ),
            request_timeout=request_timeout,
        )

    async def remove_notification(
        self,
        notification_group_id: int,
        notification_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user
        :param notification_group_id: Identifier of notification group to which the notification belongs
        :param notification_id: Identifier of removed notification
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveNotification(
                notification_group_id=notification_group_id,
                notification_id=notification_id,
            ),
            request_timeout=request_timeout,
        )

    async def remove_notification_group(
        self,
        notification_group_id: int,
        max_notification_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user
        :param notification_group_id: Notification group identifier
        :param max_notification_id: The maximum identifier of removed notifications
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveNotificationGroup(
                notification_group_id=notification_group_id,
                max_notification_id=max_notification_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_link(
        self,
        chat_id: int,
        message_id: int,
        media_timestamp: int,
        for_album: bool,
        in_message_thread: bool,
        request_timeout: float = 10.0,
    ) -> MessageLink:
        """
        Returns an HTTPS link to a message in a chat. Available only if messageProperties.can_get_link, or if messageProperties.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param media_timestamp: If not 0, timestamp from which the video/audio/video note/voice note/story playing must start, in seconds. The media can be in the message content or in its link preview
        :param for_album: Pass true to create a link for the whole media album
        :param in_message_thread: Pass true to create a link to the message as a channel post comment, in a message thread, or a forum topic
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageLink(
                chat_id=chat_id,
                message_id=message_id,
                media_timestamp=media_timestamp,
                for_album=for_album,
                in_message_thread=in_message_thread,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_embedding_code(
        self,
        chat_id: int,
        message_id: int,
        for_album: bool,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns an HTML code for embedding the message. Available only if messageProperties.can_get_embedding_code
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param for_album: Pass true to return an HTML code for embedding of the whole media album
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageEmbeddingCode(
                chat_id=chat_id,
                message_id=message_id,
                for_album=for_album,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_link_info(
        self,
        url: str,
        request_timeout: float = 10.0,
    ) -> MessageLinkInfo:
        """
        Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage
        :param url: The message link
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageLinkInfo(
                url=url,
            ),
            request_timeout=request_timeout,
        )

    async def translate_text(
        self,
        text: FormattedText,
        to_language_code: str,
        request_timeout: float = 10.0,
    ) -> FormattedText:
        """
        Translates a text to the given language. If the current user is a Telegram Premium user, then text formatting is preserved
        :param text: Text to translate
        :param to_language_code: Language code of the language to which the message is translated. Must be one of
        :param request_timeout: Request timeout
        """
        return await self(
            TranslateText(
                text=text,
                to_language_code=to_language_code,
            ),
            request_timeout=request_timeout,
        )

    async def translate_message_text(
        self,
        chat_id: int,
        message_id: int,
        to_language_code: str,
        request_timeout: float = 10.0,
    ) -> FormattedText:
        """
        Extracts text or caption of the given message and translates it to the given language. If the current user is a Telegram Premium user, then text formatting is preserved
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param to_language_code: Language code of the language to which the message is translated. Must be one of
        :param request_timeout: Request timeout
        """
        return await self(
            TranslateMessageText(
                chat_id=chat_id,
                message_id=message_id,
                to_language_code=to_language_code,
            ),
            request_timeout=request_timeout,
        )

    async def recognize_speech(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Recognizes speech in a video note or a voice note message
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message. Use messageProperties.can_recognize_speech to check whether the message is suitable
        :param request_timeout: Request timeout
        """
        return await self(
            RecognizeSpeech(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def rate_speech_recognition(
        self,
        chat_id: int,
        message_id: int,
        is_good: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Rates recognized speech in a video note or a voice note message
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param is_good: Pass true if the speech recognition is good
        :param request_timeout: Request timeout
        """
        return await self(
            RateSpeechRecognition(
                chat_id=chat_id,
                message_id=message_id,
                is_good=is_good,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_available_message_senders(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatMessageSenders:
        """
        Returns the list of message sender identifiers, which can be used to send messages in a chat
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatAvailableMessageSenders(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_message_sender(
        self,
        chat_id: int,
        message_sender_id: MessageSender,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Selects a message sender to send messages in a chat
        :param chat_id: Chat identifier
        :param message_sender_id: New message sender for the chat
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatMessageSender(
                chat_id=chat_id,
                message_sender_id=message_sender_id,
            ),
            request_timeout=request_timeout,
        )

    async def send_message(
        self,
        chat_id: int,
        message_thread_id: int,
        input_message_content: InputMessageContent,
        reply_to: InputMessageReplyTo | None = None,
        options: MessageSendOptions | None = None,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Sends a message. Returns the sent message
        :param chat_id: Target chat
        :param message_thread_id: If not 0, the message thread identifier in which the message will be sent
        :param input_message_content: The content of the message to be sent
        :param reply_to: Information about the message or story to be replied; pass null if none
        :param options: Options to be used to send the message; pass null to use default options
        :param reply_markup: Markup for replying to the message; pass null if none; for bots only
        :param request_timeout: Request timeout
        """
        return await self(
            SendMessage(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                input_message_content=input_message_content,
                reply_to=reply_to,
                options=options,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def send_message_album(
        self,
        chat_id: int,
        message_thread_id: int,
        input_message_contents: list[InputMessageContent],
        reply_to: InputMessageReplyTo | None = None,
        options: MessageSendOptions | None = None,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album.
        :param chat_id: Target chat
        :param message_thread_id: If not 0, the message thread identifier in which the messages will be sent
        :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media
        :param reply_to: Information about the message or story to be replied; pass null if none
        :param options: Options to be used to send the messages; pass null to use default options
        :param request_timeout: Request timeout
        """
        return await self(
            SendMessageAlbum(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                input_message_contents=input_message_contents,
                reply_to=reply_to,
                options=options,
            ),
            request_timeout=request_timeout,
        )

    async def send_bot_start_message(
        self,
        bot_user_id: int,
        chat_id: int,
        parameter: str,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Invites a bot to a chat (if it is not yet a member) and sends it the /start command; requires can_invite_users member right. Bots can't be invited to a private chat other than the chat with the bot.
        :param bot_user_id: Identifier of the bot
        :param chat_id: Identifier of the target chat
        :param parameter: A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)
        :param request_timeout: Request timeout
        """
        return await self(
            SendBotStartMessage(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                parameter=parameter,
            ),
            request_timeout=request_timeout,
        )

    async def send_inline_query_result_message(
        self,
        chat_id: int,
        message_thread_id: int,
        query_id: int,
        result_id: str,
        hide_via_bot: bool,
        reply_to: InputMessageReplyTo | None = None,
        options: MessageSendOptions | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message
        :param chat_id: Target chat
        :param message_thread_id: If not 0, the message thread identifier in which the message will be sent
        :param query_id: Identifier of the inline query
        :param result_id: Identifier of the inline query result
        :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption('animation_search_bot_username'), getOption('photo_search_bot_username'), and getOption('venue_search_bot_username')
        :param reply_to: Information about the message or story to be replied; pass null if none
        :param options: Options to be used to send the message; pass null to use default options
        :param request_timeout: Request timeout
        """
        return await self(
            SendInlineQueryResultMessage(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                query_id=query_id,
                result_id=result_id,
                hide_via_bot=hide_via_bot,
                reply_to=reply_to,
                options=options,
            ),
            request_timeout=request_timeout,
        )

    async def forward_messages(
        self,
        chat_id: int,
        message_thread_id: int,
        from_chat_id: int,
        message_ids: list[int],
        send_copy: bool,
        remove_caption: bool,
        options: MessageSendOptions | None = None,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message
        :param chat_id: Identifier of the chat to which to forward messages
        :param message_thread_id: If not 0, the message thread identifier in which the message will be sent; for forum threads only
        :param from_chat_id: Identifier of the chat from which to forward messages
        :param message_ids: Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously. A message can be forwarded only if messageProperties.can_be_forwarded
        :param send_copy: Pass true to copy content of the messages without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local
        :param remove_caption: Pass true to remove media captions of message copies. Ignored if send_copy is false
        :param options: Options to be used to send the messages; pass null to use default options
        :param request_timeout: Request timeout
        """
        return await self(
            ForwardMessages(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                from_chat_id=from_chat_id,
                message_ids=message_ids,
                send_copy=send_copy,
                remove_caption=remove_caption,
                options=options,
            ),
            request_timeout=request_timeout,
        )

    async def send_quick_reply_shortcut_messages(
        self,
        chat_id: int,
        shortcut_id: int,
        sending_id: int,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Sends messages from a quick reply shortcut. Requires Telegram Business subscription
        :param chat_id: Identifier of the chat to which to send messages. The chat must be a private chat with a regular user
        :param shortcut_id: Unique identifier of the quick reply shortcut
        :param sending_id: Non-persistent identifier, which will be returned back in messageSendingStatePending object and can be used to match sent messages and corresponding updateNewMessage updates
        :param request_timeout: Request timeout
        """
        return await self(
            SendQuickReplyShortcutMessages(
                chat_id=chat_id,
                shortcut_id=shortcut_id,
                sending_id=sending_id,
            ),
            request_timeout=request_timeout,
        )

    async def resend_messages(
        self,
        chat_id: int,
        message_ids: list[int],
        quote: InputTextQuote | None = None,
        request_timeout: float = 10.0,
    ) -> Messages:
        """
        Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed.
        :param chat_id: Identifier of the chat to send messages
        :param message_ids: Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order
        :param quote: New manually chosen quote from the message to be replied; pass null if none. Ignored if more than one message is re-sent, or if messageSendingStateFailed.need_another_reply_quote == false
        :param request_timeout: Request timeout
        """
        return await self(
            ResendMessages(
                chat_id=chat_id,
                message_ids=message_ids,
                quote=quote,
            ),
            request_timeout=request_timeout,
        )

    async def add_local_message(
        self,
        chat_id: int,
        sender_id: MessageSender,
        disable_notification: bool,
        input_message_content: InputMessageContent,
        reply_to: InputMessageReplyTo | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message
        :param chat_id: Target chat
        :param sender_id: Identifier of the sender of the message
        :param disable_notification: Pass true to disable notification for the message
        :param input_message_content: The content of the message to be added
        :param reply_to: Information about the message or story to be replied; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            AddLocalMessage(
                chat_id=chat_id,
                sender_id=sender_id,
                disable_notification=disable_notification,
                input_message_content=input_message_content,
                reply_to=reply_to,
            ),
            request_timeout=request_timeout,
        )

    async def delete_messages(
        self,
        chat_id: int,
        message_ids: list[int],
        revoke: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes messages
        :param chat_id: Chat identifier
        :param message_ids: Identifiers of the messages to be deleted. Use messageProperties.can_be_deleted_only_for_self and messageProperties.can_be_deleted_for_all_users to get suitable messages
        :param revoke: Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteMessages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=revoke,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat_messages_by_sender(
        self,
        chat_id: int,
        sender_id: MessageSender,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges
        :param chat_id: Chat identifier
        :param sender_id: Identifier of the sender of messages to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChatMessagesBySender(
                chat_id=chat_id,
                sender_id=sender_id,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat_messages_by_date(
        self,
        chat_id: int,
        min_date: int,
        max_date: int,
        revoke: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted
        :param chat_id: Chat identifier
        :param min_date: The minimum date of the messages to delete
        :param max_date: The maximum date of the messages to delete
        :param revoke: Pass true to delete chat messages for all users; private chats only
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChatMessagesByDate(
                chat_id=chat_id,
                min_date=min_date,
                max_date=max_date,
                revoke=revoke,
            ),
            request_timeout=request_timeout,
        )

    async def edit_message_text(
        self,
        chat_id: int,
        message_id: int,
        input_message_content: InputMessageContent,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
        :param input_message_content: New text content of the message. Must be of type inputMessageText
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :param request_timeout: Request timeout
        """
        return await self(
            EditMessageText(
                chat_id=chat_id,
                message_id=message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_message_live_location(
        self,
        chat_id: int,
        message_id: int,
        live_period: int,
        heading: int,
        proximity_alert_radius: int,
        reply_markup: ReplyMarkup | None = None,
        location: Location | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location.
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
        :param live_period: New time relative to the message send date, for which the location can be updated, in seconds. If 0x7FFFFFFF specified, then the location can be updated forever.
        :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :param location: New location content of the message; pass null to stop sharing the live location
        :param request_timeout: Request timeout
        """
        return await self(
            EditMessageLiveLocation(
                chat_id=chat_id,
                message_id=message_id,
                live_period=live_period,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
                reply_markup=reply_markup,
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def edit_message_media(
        self,
        chat_id: int,
        message_id: int,
        input_message_content: InputMessageContent,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video, including message caption. If only the caption needs to be edited, use editMessageCaption instead.
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :param request_timeout: Request timeout
        """
        return await self(
            EditMessageMedia(
                chat_id=chat_id,
                message_id=message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_message_caption(
        self,
        chat_id: int,
        message_id: int,
        show_caption_above_media: bool,
        reply_markup: ReplyMarkup | None = None,
        caption: FormattedText | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Edits the message content caption. Returns the edited message after the edit is completed on the server side
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
        :param show_caption_above_media: Pass true to show the caption above the media; otherwise, the caption will be shown below the media. Can be true only for animation, photo, and video messages
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :param caption: New message content caption; 0-getOption('message_caption_length_max') characters; pass null to remove caption
        :param request_timeout: Request timeout
        """
        return await self(
            EditMessageCaption(
                chat_id=chat_id,
                message_id=message_id,
                show_caption_above_media=show_caption_above_media,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_timeout=request_timeout,
        )

    async def edit_message_reply_markup(
        self,
        chat_id: int,
        message_id: int,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
        :param reply_markup: The new message reply markup; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            EditMessageReplyMarkup(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_inline_message_text(
        self,
        inline_message_id: str,
        input_message_content: InputMessageContent,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits the text of an inline text or game message sent via a bot; for bots only
        :param inline_message_id: Inline message identifier
        :param input_message_content: New text content of the message. Must be of type inputMessageText
        :param reply_markup: The new message reply markup; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            EditInlineMessageText(
                inline_message_id=inline_message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_inline_message_live_location(
        self,
        inline_message_id: str,
        live_period: int,
        heading: int,
        proximity_alert_radius: int,
        reply_markup: ReplyMarkup | None = None,
        location: Location | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits the content of a live location in an inline message sent via a bot; for bots only
        :param inline_message_id: Inline message identifier
        :param live_period: New time relative to the message send date, for which the location can be updated, in seconds. If 0x7FFFFFFF specified, then the location can be updated forever.
        :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        :param reply_markup: The new message reply markup; pass null if none
        :param location: New location content of the message; pass null to stop sharing the live location
        :param request_timeout: Request timeout
        """
        return await self(
            EditInlineMessageLiveLocation(
                inline_message_id=inline_message_id,
                live_period=live_period,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
                reply_markup=reply_markup,
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def edit_inline_message_media(
        self,
        inline_message_id: str,
        input_message_content: InputMessageContent,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only
        :param inline_message_id: Inline message identifier
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :param request_timeout: Request timeout
        """
        return await self(
            EditInlineMessageMedia(
                inline_message_id=inline_message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_inline_message_caption(
        self,
        inline_message_id: str,
        show_caption_above_media: bool,
        reply_markup: ReplyMarkup | None = None,
        caption: FormattedText | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits the caption of an inline message sent via a bot; for bots only
        :param inline_message_id: Inline message identifier
        :param show_caption_above_media: Pass true to show the caption above the media; otherwise, the caption will be shown below the media. Can be true only for animation, photo, and video messages
        :param reply_markup: The new message reply markup; pass null if none
        :param caption: New message content caption; pass null to remove caption; 0-getOption('message_caption_length_max') characters
        :param request_timeout: Request timeout
        """
        return await self(
            EditInlineMessageCaption(
                inline_message_id=inline_message_id,
                show_caption_above_media=show_caption_above_media,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_timeout=request_timeout,
        )

    async def edit_inline_message_reply_markup(
        self,
        inline_message_id: str,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits the reply markup of an inline message sent via a bot; for bots only
        :param inline_message_id: Inline message identifier
        :param reply_markup: The new message reply markup; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            EditInlineMessageReplyMarkup(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_message_scheduling_state(
        self,
        chat_id: int,
        message_id: int,
        scheduling_state: MessageSchedulingState | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message. Use messageProperties.can_edit_scheduling_state to check whether the message is suitable
        :param scheduling_state: The new message scheduling state; pass null to send the message immediately
        :param request_timeout: Request timeout
        """
        return await self(
            EditMessageSchedulingState(
                chat_id=chat_id,
                message_id=message_id,
                scheduling_state=scheduling_state,
            ),
            request_timeout=request_timeout,
        )

    async def set_message_fact_check(
        self,
        chat_id: int,
        message_id: int,
        text: FormattedText | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the fact-check of a message. Can be only used if messageProperties.can_set_fact_check == true
        :param chat_id: The channel chat the message belongs to
        :param message_id: Identifier of the message
        :param text: New text of the fact-check; 0-getOption('fact_check_length_max') characters; pass null to remove it. Only Bold, Italic, and TextUrl entities with https://t.me/ links are supported
        :param request_timeout: Request timeout
        """
        return await self(
            SetMessageFactCheck(
                chat_id=chat_id,
                message_id=message_id,
                text=text,
            ),
            request_timeout=request_timeout,
        )

    async def send_business_message(
        self,
        business_connection_id: str,
        chat_id: int,
        disable_notification: bool,
        protect_content: bool,
        effect_id: int,
        input_message_content: InputMessageContent,
        reply_to: InputMessageReplyTo | None = None,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessage:
        """
        Sends a message on behalf of a business account; for bots only. Returns the message after it was sent
        :param business_connection_id: Unique identifier of business connection on behalf of which to send the request
        :param chat_id: Target chat
        :param disable_notification: Pass true to disable notification for the message
        :param protect_content: Pass true if the content of the message must be protected from forwarding and saving
        :param effect_id: Identifier of the effect to apply to the message
        :param input_message_content: The content of the message to be sent
        :param reply_to: Information about the message to be replied; pass null if none
        :param reply_markup: Markup for replying to the message; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            SendBusinessMessage(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                disable_notification=disable_notification,
                protect_content=protect_content,
                effect_id=effect_id,
                input_message_content=input_message_content,
                reply_to=reply_to,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def send_business_message_album(
        self,
        business_connection_id: str,
        chat_id: int,
        disable_notification: bool,
        protect_content: bool,
        effect_id: int,
        input_message_contents: list[InputMessageContent],
        reply_to: InputMessageReplyTo | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessages:
        """
        Sends 2-10 messages grouped together into an album on behalf of a business account; for bots only. Currently, only audio, document, photo and video messages can be grouped into an album.
        :param business_connection_id: Unique identifier of business connection on behalf of which to send the request
        :param chat_id: Target chat
        :param disable_notification: Pass true to disable notification for the message
        :param protect_content: Pass true if the content of the message must be protected from forwarding and saving
        :param effect_id: Identifier of the effect to apply to the message
        :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media
        :param reply_to: Information about the message to be replied; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            SendBusinessMessageAlbum(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                disable_notification=disable_notification,
                protect_content=protect_content,
                effect_id=effect_id,
                input_message_contents=input_message_contents,
                reply_to=reply_to,
            ),
            request_timeout=request_timeout,
        )

    async def edit_business_message_text(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        input_message_content: InputMessageContent,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessage:
        """
        Edits the text of a text or game message sent on behalf of a business account; for bots only
        :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message
        :param input_message_content: New text content of the message. Must be of type inputMessageText
        :param reply_markup: The new message reply markup; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            EditBusinessMessageText(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                message_id=message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_business_message_live_location(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        live_period: int,
        heading: int,
        proximity_alert_radius: int,
        reply_markup: ReplyMarkup | None = None,
        location: Location | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessage:
        """
        Edits the content of a live location in a message sent on behalf of a business account; for bots only
        :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message
        :param live_period: New time relative to the message send date, for which the location can be updated, in seconds. If 0x7FFFFFFF specified, then the location can be updated forever.
        :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        :param reply_markup: The new message reply markup; pass null if none
        :param location: New location content of the message; pass null to stop sharing the live location
        :param request_timeout: Request timeout
        """
        return await self(
            EditBusinessMessageLiveLocation(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                message_id=message_id,
                live_period=live_period,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
                reply_markup=reply_markup,
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def edit_business_message_media(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        input_message_content: InputMessageContent,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessage:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video in a message sent on behalf of a business account; for bots only
        :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :param request_timeout: Request timeout
        """
        return await self(
            EditBusinessMessageMedia(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                message_id=message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def edit_business_message_caption(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        show_caption_above_media: bool,
        reply_markup: ReplyMarkup | None = None,
        caption: FormattedText | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessage:
        """
        Edits the caption of a message sent on behalf of a business account; for bots only
        :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message
        :param show_caption_above_media: Pass true to show the caption above the media; otherwise, the caption will be shown below the media. Can be true only for animation, photo, and video messages
        :param reply_markup: The new message reply markup; pass null if none
        :param caption: New message content caption; pass null to remove caption; 0-getOption('message_caption_length_max') characters
        :param request_timeout: Request timeout
        """
        return await self(
            EditBusinessMessageCaption(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                message_id=message_id,
                show_caption_above_media=show_caption_above_media,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_timeout=request_timeout,
        )

    async def edit_business_message_reply_markup(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessage:
        """
        Edits the reply markup of a message sent on behalf of a business account; for bots only
        :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message
        :param reply_markup: The new message reply markup; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            EditBusinessMessageReplyMarkup(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def stop_business_poll(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessMessage:
        """
        Stops a poll sent on behalf of a business account; for bots only
        :param business_connection_id: Unique identifier of business connection on behalf of which the message with the poll was sent
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message containing the poll
        :param reply_markup: The new message reply markup; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            StopBusinessPoll(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def set_business_message_is_pinned(
        self,
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        is_pinned: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Pins or unpins a message sent on behalf of a business account; for bots only
        :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
        :param chat_id: The chat the message belongs to
        :param message_id: Identifier of the message
        :param is_pinned: Pass true to pin the message, pass false to unpin it
        :param request_timeout: Request timeout
        """
        return await self(
            SetBusinessMessageIsPinned(
                business_connection_id=business_connection_id,
                chat_id=chat_id,
                message_id=message_id,
                is_pinned=is_pinned,
            ),
            request_timeout=request_timeout,
        )

    async def check_quick_reply_shortcut_name(
        self,
        name: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks validness of a name for a quick reply shortcut. Can be called synchronously
        :param name: The name of the shortcut; 1-32 characters
        :param request_timeout: Request timeout
        """
        return await self(
            CheckQuickReplyShortcutName(
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def load_quick_reply_shortcuts(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Loads quick reply shortcuts created by the current user. The loaded topics will be sent through updateQuickReplyShortcuts
        :param request_timeout: Request timeout
        """
        return await self(
            LoadQuickReplyShortcuts(),
            request_timeout=request_timeout,
        )

    async def set_quick_reply_shortcut_name(
        self,
        shortcut_id: int,
        name: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes name of a quick reply shortcut
        :param shortcut_id: Unique identifier of the quick reply shortcut
        :param name: New name for the shortcut. Use checkQuickReplyShortcutName to check its validness
        :param request_timeout: Request timeout
        """
        return await self(
            SetQuickReplyShortcutName(
                shortcut_id=shortcut_id,
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def delete_quick_reply_shortcut(
        self,
        shortcut_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes a quick reply shortcut
        :param shortcut_id: Unique identifier of the quick reply shortcut
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteQuickReplyShortcut(
                shortcut_id=shortcut_id,
            ),
            request_timeout=request_timeout,
        )

    async def reorder_quick_reply_shortcuts(
        self,
        shortcut_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the order of quick reply shortcuts
        :param shortcut_ids: The new order of quick reply shortcuts
        :param request_timeout: Request timeout
        """
        return await self(
            ReorderQuickReplyShortcuts(
                shortcut_ids=shortcut_ids,
            ),
            request_timeout=request_timeout,
        )

    async def load_quick_reply_shortcut_messages(
        self,
        shortcut_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Loads quick reply messages that can be sent by a given quick reply shortcut. The loaded messages will be sent through updateQuickReplyShortcutMessages
        :param shortcut_id: Unique identifier of the quick reply shortcut
        :param request_timeout: Request timeout
        """
        return await self(
            LoadQuickReplyShortcutMessages(
                shortcut_id=shortcut_id,
            ),
            request_timeout=request_timeout,
        )

    async def delete_quick_reply_shortcut_messages(
        self,
        shortcut_id: int,
        message_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes specified quick reply messages
        :param shortcut_id: Unique identifier of the quick reply shortcut to which the messages belong
        :param message_ids: Unique identifiers of the messages
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteQuickReplyShortcutMessages(
                shortcut_id=shortcut_id,
                message_ids=message_ids,
            ),
            request_timeout=request_timeout,
        )

    async def add_quick_reply_shortcut_message(
        self,
        shortcut_name: str,
        reply_to_message_id: int,
        input_message_content: InputMessageContent,
        request_timeout: float = 10.0,
    ) -> QuickReplyMessage:
        """
        Adds a message to a quick reply shortcut. If shortcut doesn't exist and there are less than getOption('quick_reply_shortcut_count_max') shortcuts, then a new shortcut is created.
        :param shortcut_name: Name of the target shortcut
        :param reply_to_message_id: Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none
        :param input_message_content: The content of the message to be added; inputMessagePoll, inputMessageForwarded and inputMessageLocation with live_period aren't supported
        :param request_timeout: Request timeout
        """
        return await self(
            AddQuickReplyShortcutMessage(
                shortcut_name=shortcut_name,
                reply_to_message_id=reply_to_message_id,
                input_message_content=input_message_content,
            ),
            request_timeout=request_timeout,
        )

    async def add_quick_reply_shortcut_inline_query_result_message(
        self,
        shortcut_name: str,
        reply_to_message_id: int,
        query_id: int,
        result_id: str,
        hide_via_bot: bool,
        request_timeout: float = 10.0,
    ) -> QuickReplyMessage:
        """
        Adds a message to a quick reply shortcut via inline bot. If shortcut doesn't exist and there are less than getOption('quick_reply_shortcut_count_max') shortcuts, then a new shortcut is created.
        :param shortcut_name: Name of the target shortcut
        :param reply_to_message_id: Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none
        :param query_id: Identifier of the inline query
        :param result_id: Identifier of the inline query result
        :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption('animation_search_bot_username'), getOption('photo_search_bot_username'), and getOption('venue_search_bot_username')
        :param request_timeout: Request timeout
        """
        return await self(
            AddQuickReplyShortcutInlineQueryResultMessage(
                shortcut_name=shortcut_name,
                reply_to_message_id=reply_to_message_id,
                query_id=query_id,
                result_id=result_id,
                hide_via_bot=hide_via_bot,
            ),
            request_timeout=request_timeout,
        )

    async def add_quick_reply_shortcut_message_album(
        self,
        shortcut_name: str,
        reply_to_message_id: int,
        input_message_contents: list[InputMessageContent],
        request_timeout: float = 10.0,
    ) -> QuickReplyMessages:
        """
        Adds 2-10 messages grouped together into an album to a quick reply shortcut. Currently, only audio, document, photo and video messages can be grouped into an album.
        :param shortcut_name: Name of the target shortcut
        :param reply_to_message_id: Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none
        :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media
        :param request_timeout: Request timeout
        """
        return await self(
            AddQuickReplyShortcutMessageAlbum(
                shortcut_name=shortcut_name,
                reply_to_message_id=reply_to_message_id,
                input_message_contents=input_message_contents,
            ),
            request_timeout=request_timeout,
        )

    async def readd_quick_reply_shortcut_messages(
        self,
        shortcut_name: str,
        message_ids: list[int],
        request_timeout: float = 10.0,
    ) -> QuickReplyMessages:
        """
        Readds quick reply messages which failed to add. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed.
        :param shortcut_name: Name of the target shortcut
        :param message_ids: Identifiers of the quick reply messages to readd. Message identifiers must be in a strictly increasing order
        :param request_timeout: Request timeout
        """
        return await self(
            ReaddQuickReplyShortcutMessages(
                shortcut_name=shortcut_name,
                message_ids=message_ids,
            ),
            request_timeout=request_timeout,
        )

    async def edit_quick_reply_message(
        self,
        shortcut_id: int,
        message_id: int,
        input_message_content: InputMessageContent,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Asynchronously edits the text, media or caption of a quick reply message. Use quickReplyMessage.can_be_edited to check whether a message can be edited.
        :param shortcut_id: Unique identifier of the quick reply shortcut with the message
        :param message_id: Identifier of the message
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :param request_timeout: Request timeout
        """
        return await self(
            EditQuickReplyMessage(
                shortcut_id=shortcut_id,
                message_id=message_id,
                input_message_content=input_message_content,
            ),
            request_timeout=request_timeout,
        )

    async def get_forum_topic_default_icons(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns the list of custom emoji, which can be used as forum topic icon by all users
        :param request_timeout: Request timeout
        """
        return await self(
            GetForumTopicDefaultIcons(),
            request_timeout=request_timeout,
        )

    async def create_forum_topic(
        self,
        chat_id: int,
        name: str,
        icon: ForumTopicIcon,
        request_timeout: float = 10.0,
    ) -> ForumTopicInfo:
        """
        Creates a topic in a forum supergroup chat; requires can_manage_topics administrator or can_create_topics member right in the supergroup
        :param chat_id: Identifier of the chat
        :param name: Name of the topic; 1-128 characters
        :param icon: Icon of the topic. Icon color must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F. Telegram Premium users can use any custom emoji as topic icon, other users can use only a custom emoji returned by getForumTopicDefaultIcons
        :param request_timeout: Request timeout
        """
        return await self(
            CreateForumTopic(
                chat_id=chat_id,
                name=name,
                icon=icon,
            ),
            request_timeout=request_timeout,
        )

    async def edit_forum_topic(
        self,
        chat_id: int,
        message_thread_id: int,
        name: str,
        edit_icon_custom_emoji: bool,
        icon_custom_emoji_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits title and icon of a topic in a forum supergroup chat; requires can_manage_topics right in the supergroup unless the user is creator of the topic
        :param chat_id: Identifier of the chat
        :param message_thread_id: Message thread identifier of the forum topic
        :param name: New name of the topic; 0-128 characters. If empty, the previous topic name is kept
        :param edit_icon_custom_emoji: Pass true to edit the icon of the topic. Icon of the General topic can't be edited
        :param icon_custom_emoji_id: Identifier of the new custom emoji for topic icon; pass 0 to remove the custom emoji. Ignored if edit_icon_custom_emoji is false. Telegram Premium users can use any custom emoji, other users can use only a custom emoji returned by getForumTopicDefaultIcons
        :param request_timeout: Request timeout
        """
        return await self(
            EditForumTopic(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                name=name,
                edit_icon_custom_emoji=edit_icon_custom_emoji,
                icon_custom_emoji_id=icon_custom_emoji_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_forum_topic(
        self,
        chat_id: int,
        message_thread_id: int,
        request_timeout: float = 10.0,
    ) -> ForumTopic:
        """
        Returns information about a forum topic
        :param chat_id: Identifier of the chat
        :param message_thread_id: Message thread identifier of the forum topic
        :param request_timeout: Request timeout
        """
        return await self(
            GetForumTopic(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_forum_topic_link(
        self,
        chat_id: int,
        message_thread_id: int,
        request_timeout: float = 10.0,
    ) -> MessageLink:
        """
        Returns an HTTPS link to a topic in a forum chat. This is an offline request
        :param chat_id: Identifier of the chat
        :param message_thread_id: Message thread identifier of the forum topic
        :param request_timeout: Request timeout
        """
        return await self(
            GetForumTopicLink(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_forum_topics(
        self,
        chat_id: int,
        query: str,
        offset_date: int,
        offset_message_id: int,
        offset_message_thread_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> ForumTopics:
        """
        Returns found forum topics in a forum chat. This is a temporary method for getting information about topic list from the server
        :param chat_id: Identifier of the forum chat
        :param query: Query to search for in the forum topic's name
        :param offset_date: The date starting from which the results need to be fetched. Use 0 or any date in the future to get results from the last topic
        :param offset_message_id: The message identifier of the last message in the last found topic, or 0 for the first request
        :param offset_message_thread_id: The message thread identifier of the last found topic, or 0 for the first request
        :param limit: The maximum number of forum topics to be returned; up to 100. For optimal performance, the number of returned forum topics is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            GetForumTopics(
                chat_id=chat_id,
                query=query,
                offset_date=offset_date,
                offset_message_id=offset_message_id,
                offset_message_thread_id=offset_message_thread_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def set_forum_topic_notification_settings(
        self,
        chat_id: int,
        message_thread_id: int,
        notification_settings: ChatNotificationSettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the notification settings of a forum topic
        :param chat_id: Chat identifier
        :param message_thread_id: Message thread identifier of the forum topic
        :param notification_settings: New notification settings for the forum topic. If the topic is muted for more than 366 days, it is considered to be muted forever
        :param request_timeout: Request timeout
        """
        return await self(
            SetForumTopicNotificationSettings(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                notification_settings=notification_settings,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_forum_topic_is_closed(
        self,
        chat_id: int,
        message_thread_id: int,
        is_closed: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether a topic is closed in a forum supergroup chat; requires can_manage_topics right in the supergroup unless the user is creator of the topic
        :param chat_id: Identifier of the chat
        :param message_thread_id: Message thread identifier of the forum topic
        :param is_closed: Pass true to close the topic; pass false to reopen it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleForumTopicIsClosed(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                is_closed=is_closed,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_general_forum_topic_is_hidden(
        self,
        chat_id: int,
        is_hidden: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether a General topic is hidden in a forum supergroup chat; requires can_manage_topics right in the supergroup
        :param chat_id: Identifier of the chat
        :param is_hidden: Pass true to hide and close the General topic; pass false to unhide it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGeneralForumTopicIsHidden(
                chat_id=chat_id,
                is_hidden=is_hidden,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_forum_topic_is_pinned(
        self,
        chat_id: int,
        message_thread_id: int,
        is_pinned: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the pinned state of a forum topic; requires can_manage_topics right in the supergroup. There can be up to getOption('pinned_forum_topic_count_max') pinned forum topics
        :param chat_id: Chat identifier
        :param message_thread_id: Message thread identifier of the forum topic
        :param is_pinned: Pass true to pin the topic; pass false to unpin it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleForumTopicIsPinned(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                is_pinned=is_pinned,
            ),
            request_timeout=request_timeout,
        )

    async def set_pinned_forum_topics(
        self,
        chat_id: int,
        message_thread_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the order of pinned forum topics; requires can_manage_topics right in the supergroup
        :param chat_id: Chat identifier
        :param message_thread_ids: The new list of pinned forum topics
        :param request_timeout: Request timeout
        """
        return await self(
            SetPinnedForumTopics(
                chat_id=chat_id,
                message_thread_ids=message_thread_ids,
            ),
            request_timeout=request_timeout,
        )

    async def delete_forum_topic(
        self,
        chat_id: int,
        message_thread_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all messages in a forum topic; requires can_delete_messages administrator right in the supergroup unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages
        :param chat_id: Identifier of the chat
        :param message_thread_id: Message thread identifier of the forum topic
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteForumTopic(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_emoji_reaction(
        self,
        emoji: str,
        request_timeout: float = 10.0,
    ) -> EmojiReaction:
        """
        Returns information about an emoji reaction. Returns a 404 error if the reaction is not found
        :param emoji: Text representation of the reaction
        :param request_timeout: Request timeout
        """
        return await self(
            GetEmojiReaction(
                emoji=emoji,
            ),
            request_timeout=request_timeout,
        )

    async def get_custom_emoji_reaction_animations(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns TGS stickers with generic animations for custom emoji reactions
        :param request_timeout: Request timeout
        """
        return await self(
            GetCustomEmojiReactionAnimations(),
            request_timeout=request_timeout,
        )

    async def get_message_available_reactions(
        self,
        chat_id: int,
        message_id: int,
        row_size: int,
        request_timeout: float = 10.0,
    ) -> AvailableReactions:
        """
        Returns reactions, which can be added to a message. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param row_size: Number of reaction per row, 5-25
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageAvailableReactions(
                chat_id=chat_id,
                message_id=message_id,
                row_size=row_size,
            ),
            request_timeout=request_timeout,
        )

    async def clear_recent_reactions(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears the list of recently used reactions
        :param request_timeout: Request timeout
        """
        return await self(
            ClearRecentReactions(),
            request_timeout=request_timeout,
        )

    async def add_message_reaction(
        self,
        chat_id: int,
        message_id: int,
        reaction_type: ReactionType,
        is_big: bool,
        update_recent_reactions: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a reaction or a tag to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param reaction_type: Type of the reaction to add. Use addPaidMessageReaction instead to add the paid reaction
        :param is_big: Pass true if the reaction is added with a big animation
        :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions; tags are never added to the list of recent reactions
        :param request_timeout: Request timeout
        """
        return await self(
            AddMessageReaction(
                chat_id=chat_id,
                message_id=message_id,
                reaction_type=reaction_type,
                is_big=is_big,
                update_recent_reactions=update_recent_reactions,
            ),
            request_timeout=request_timeout,
        )

    async def remove_message_reaction(
        self,
        chat_id: int,
        message_id: int,
        reaction_type: ReactionType,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a reaction from a message. A chosen reaction can always be removed
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param reaction_type: Type of the reaction to remove. The paid reaction can't be removed
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveMessageReaction(
                chat_id=chat_id,
                message_id=message_id,
                reaction_type=reaction_type,
            ),
            request_timeout=request_timeout,
        )

    async def add_paid_message_reaction(
        self,
        chat_id: int,
        message_id: int,
        star_count: int,
        is_anonymous: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds the paid message reaction to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param star_count: Number of Telegram Stars to be used for the reaction; 1-getOption('paid_reaction_star_count_max')
        :param is_anonymous: Pass true to make paid reaction of the user on the message anonymous; pass false to make the user's profile visible among top reactors
        :param request_timeout: Request timeout
        """
        return await self(
            AddPaidMessageReaction(
                chat_id=chat_id,
                message_id=message_id,
                star_count=star_count,
                is_anonymous=is_anonymous,
            ),
            request_timeout=request_timeout,
        )

    async def remove_pending_paid_message_reactions(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes all pending paid reactions on a message. Can be called within 5 seconds after the last addPaidMessageReaction call
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param request_timeout: Request timeout
        """
        return await self(
            RemovePendingPaidMessageReactions(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_paid_message_reaction_is_anonymous(
        self,
        chat_id: int,
        message_id: int,
        is_anonymous: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes whether the paid message reaction of the user to a message is anonymous. The message must have paid reaction added by the user
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param is_anonymous: Pass true to make paid reaction of the user on the message anonymous; pass false to make the user's profile visible among top reactors
        :param request_timeout: Request timeout
        """
        return await self(
            TogglePaidMessageReactionIsAnonymous(
                chat_id=chat_id,
                message_id=message_id,
                is_anonymous=is_anonymous,
            ),
            request_timeout=request_timeout,
        )

    async def set_message_reactions(
        self,
        chat_id: int,
        message_id: int,
        reaction_types: list[ReactionType],
        is_big: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets reactions on a message; for bots only
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message
        :param reaction_types: Types of the reaction to set
        :param is_big: Pass true if the reactions are added with a big animation
        :param request_timeout: Request timeout
        """
        return await self(
            SetMessageReactions(
                chat_id=chat_id,
                message_id=message_id,
                reaction_types=reaction_types,
                is_big=is_big,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_added_reactions(
        self,
        chat_id: int,
        message_id: int,
        offset: str,
        limit: int,
        reaction_type: ReactionType | None = None,
        request_timeout: float = 10.0,
    ) -> AddedReactions:
        """
        Returns reactions added for a message, along with their sender
        :param chat_id: Identifier of the chat to which the message belongs
        :param message_id: Identifier of the message. Use message.interaction_info.reactions.can_get_added_reactions to check whether added reactions can be received for the message
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of reactions to be returned; must be positive and can't be greater than 100
        :param reaction_type: Type of the reactions to return; pass null to return all added reactions; reactionTypePaid isn't supported
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageAddedReactions(
                chat_id=chat_id,
                message_id=message_id,
                offset=offset,
                limit=limit,
                reaction_type=reaction_type,
            ),
            request_timeout=request_timeout,
        )

    async def set_default_reaction_type(
        self,
        reaction_type: ReactionType,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes type of default reaction for the current user
        :param reaction_type: New type of the default reaction. The paid reaction can't be set as default
        :param request_timeout: Request timeout
        """
        return await self(
            SetDefaultReactionType(
                reaction_type=reaction_type,
            ),
            request_timeout=request_timeout,
        )

    async def get_saved_messages_tags(
        self,
        saved_messages_topic_id: int,
        request_timeout: float = 10.0,
    ) -> SavedMessagesTags:
        """
        Returns tags used in Saved Messages or a Saved Messages topic
        :param saved_messages_topic_id: Identifier of Saved Messages topic which tags will be returned; pass 0 to get all Saved Messages tags
        :param request_timeout: Request timeout
        """
        return await self(
            GetSavedMessagesTags(
                saved_messages_topic_id=saved_messages_topic_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_saved_messages_tag_label(
        self,
        tag: ReactionType,
        label: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes label of a Saved Messages tag; for Telegram Premium users only
        :param tag: The tag which label will be changed
        :param label: New label for the tag; 0-12 characters
        :param request_timeout: Request timeout
        """
        return await self(
            SetSavedMessagesTagLabel(
                tag=tag,
                label=label,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_effect(
        self,
        effect_id: int,
        request_timeout: float = 10.0,
    ) -> MessageEffect:
        """
        Returns information about a message effect. Returns a 404 error if the effect is not found
        :param effect_id: Unique identifier of the effect
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageEffect(
                effect_id=effect_id,
            ),
            request_timeout=request_timeout,
        )

    async def search_quote(
        self,
        text: FormattedText,
        quote: FormattedText,
        quote_position: int,
        request_timeout: float = 10.0,
    ) -> FoundPosition:
        """
        Searches for a given quote in a text. Returns found quote start position in UTF-16 code units. Returns a 404 error if the quote is not found. Can be called synchronously
        :param text: Text in which to search for the quote
        :param quote: Quote to search for
        :param quote_position: Approximate quote position in UTF-16 code units
        :param request_timeout: Request timeout
        """
        return await self(
            SearchQuote(
                text=text,
                quote=quote,
                quote_position=quote_position,
            ),
            request_timeout=request_timeout,
        )

    async def get_text_entities(
        self,
        text: str,
        request_timeout: float = 10.0,
    ) -> TextEntities:
        """
        Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) found in the text. Can be called synchronously
        :param text: The text in which to look for entities
        :param request_timeout: Request timeout
        """
        return await self(
            GetTextEntities(
                text=text,
            ),
            request_timeout=request_timeout,
        )

    async def parse_text_entities(
        self,
        text: str,
        parse_mode: TextParseMode,
        request_timeout: float = 10.0,
    ) -> FormattedText:
        """
        Parses Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, BlockQuote, ExpandableBlockQuote, Code, Pre, PreCode, TextUrl
        :param text: The text to parse
        :param parse_mode: Text parse mode
        :param request_timeout: Request timeout
        """
        return await self(
            ParseTextEntities(
                text=text,
                parse_mode=parse_mode,
            ),
            request_timeout=request_timeout,
        )

    async def parse_markdown(
        self,
        text: FormattedText,
        request_timeout: float = 10.0,
    ) -> FormattedText:
        """
        Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously
        :param text: The text to parse. For example, '__italic__ ~~strikethrough~~ ||spoiler|| **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**'
        :param request_timeout: Request timeout
        """
        return await self(
            ParseMarkdown(
                text=text,
            ),
            request_timeout=request_timeout,
        )

    async def get_markdown_text(
        self,
        text: FormattedText,
        request_timeout: float = 10.0,
    ) -> FormattedText:
        """
        Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously
        :param text: The text
        :param request_timeout: Request timeout
        """
        return await self(
            GetMarkdownText(
                text=text,
            ),
            request_timeout=request_timeout,
        )

    async def get_country_flag_emoji(
        self,
        country_code: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns an emoji for the given country. Returns an empty string on failure. Can be called synchronously
        :param country_code: A two-letter ISO 3166-1 alpha-2 country code as received from getCountries
        :param request_timeout: Request timeout
        """
        return await self(
            GetCountryFlagEmoji(
                country_code=country_code,
            ),
            request_timeout=request_timeout,
        )

    async def get_file_mime_type(
        self,
        file_name: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously
        :param file_name: The name of the file or path to the file
        :param request_timeout: Request timeout
        """
        return await self(
            GetFileMimeType(
                file_name=file_name,
            ),
            request_timeout=request_timeout,
        )

    async def get_file_extension(
        self,
        mime_type: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously
        :param mime_type: The MIME type of the file
        :param request_timeout: Request timeout
        """
        return await self(
            GetFileExtension(
                mime_type=mime_type,
            ),
            request_timeout=request_timeout,
        )

    async def clean_file_name(
        self,
        file_name: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. Can be called synchronously
        :param file_name: File name or path to the file
        :param request_timeout: Request timeout
        """
        return await self(
            CleanFileName(
                file_name=file_name,
            ),
            request_timeout=request_timeout,
        )

    async def get_language_pack_string(
        self,
        language_pack_database_path: str,
        localization_target: str,
        language_pack_id: str,
        key: str,
        request_timeout: float = 10.0,
    ) -> LanguagePackStringValue:
        """
        Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously
        :param language_pack_database_path: Path to the language pack database in which strings are stored
        :param localization_target: Localization target to which the language pack belongs
        :param language_pack_id: Language pack identifier
        :param key: Language pack key of the string to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            GetLanguagePackString(
                language_pack_database_path=language_pack_database_path,
                localization_target=localization_target,
                language_pack_id=language_pack_id,
                key=key,
            ),
            request_timeout=request_timeout,
        )

    async def get_json_value(
        self,
        json: str,
        request_timeout: float = 10.0,
    ) -> JsonValue:
        """
        Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously
        :param json: The JSON-serialized string
        :param request_timeout: Request timeout
        """
        return await self(
            GetJsonValue(
                json=json,
            ),
            request_timeout=request_timeout,
        )

    async def get_json_string(
        self,
        json_value: JsonValue,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously
        :param json_value: The JsonValue object
        :param request_timeout: Request timeout
        """
        return await self(
            GetJsonString(
                json_value=json_value,
            ),
            request_timeout=request_timeout,
        )

    async def get_theme_parameters_json_string(
        self,
        theme: ThemeParameters,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously
        :param theme: Theme parameters to convert to JSON
        :param request_timeout: Request timeout
        """
        return await self(
            GetThemeParametersJsonString(
                theme=theme,
            ),
            request_timeout=request_timeout,
        )

    async def set_poll_answer(
        self,
        chat_id: int,
        message_id: int,
        option_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the user answer to a poll. A poll in quiz mode can be answered only once
        :param chat_id: Identifier of the chat to which the poll belongs
        :param message_id: Identifier of the message containing the poll
        :param option_ids: 0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
        :param request_timeout: Request timeout
        """
        return await self(
            SetPollAnswer(
                chat_id=chat_id,
                message_id=message_id,
                option_ids=option_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_poll_voters(
        self,
        chat_id: int,
        message_id: int,
        option_id: int,
        offset: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> MessageSenders:
        """
        Returns message senders voted for the specified option in a non-anonymous polls. For optimal performance, the number of returned users is chosen by TDLib
        :param chat_id: Identifier of the chat to which the poll belongs
        :param message_id: Identifier of the message containing the poll
        :param option_id: 0-based identifier of the answer option
        :param offset: Number of voters to skip in the result; must be non-negative
        :param limit: The maximum number of voters to be returned; must be positive and can't be greater than 50. For optimal performance, the number of returned voters is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached
        :param request_timeout: Request timeout
        """
        return await self(
            GetPollVoters(
                chat_id=chat_id,
                message_id=message_id,
                option_id=option_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def stop_poll(
        self,
        chat_id: int,
        message_id: int,
        reply_markup: ReplyMarkup | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Stops a poll
        :param chat_id: Identifier of the chat to which the poll belongs
        :param message_id: Identifier of the message containing the poll. Use messageProperties.can_be_edited to check whether the poll can be stopped
        :param reply_markup: The new message reply markup; pass null if none; for bots only
        :param request_timeout: Request timeout
        """
        return await self(
            StopPoll(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_timeout=request_timeout,
        )

    async def hide_suggested_action(
        self,
        action: SuggestedAction,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Hides a suggested action
        :param action: Suggested action to hide
        :param request_timeout: Request timeout
        """
        return await self(
            HideSuggestedAction(
                action=action,
            ),
            request_timeout=request_timeout,
        )

    async def hide_contact_close_birthdays(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Hides the list of contacts that have close birthdays for 24 hours
        :param request_timeout: Request timeout
        """
        return await self(
            HideContactCloseBirthdays(),
            request_timeout=request_timeout,
        )

    async def get_business_connection(
        self,
        connection_id: str,
        request_timeout: float = 10.0,
    ) -> BusinessConnection:
        """
        Returns information about a business connection by its identifier; for bots only
        :param connection_id: Identifier of the business connection to return
        :param request_timeout: Request timeout
        """
        return await self(
            GetBusinessConnection(
                connection_id=connection_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_login_url_info(
        self,
        chat_id: int,
        message_id: int,
        button_id: int,
        request_timeout: float = 10.0,
    ) -> LoginUrlInfo:
        """
        Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button
        :param chat_id: Chat identifier of the message with the button
        :param message_id: Message identifier of the message with the button. The message must not be scheduled
        :param button_id: Button identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetLoginUrlInfo(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_login_url(
        self,
        chat_id: int,
        message_id: int,
        button_id: int,
        allow_write_access: bool,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl.
        :param chat_id: Chat identifier of the message with the button
        :param message_id: Message identifier of the message with the button
        :param button_id: Button identifier
        :param allow_write_access: Pass true to allow the bot to send messages to the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetLoginUrl(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                allow_write_access=allow_write_access,
            ),
            request_timeout=request_timeout,
        )

    async def share_users_with_bot(
        self,
        chat_id: int,
        message_id: int,
        button_id: int,
        shared_user_ids: list[int],
        only_check: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Shares users after pressing a keyboardButtonTypeRequestUsers button with the bot
        :param chat_id: Identifier of the chat with the bot
        :param message_id: Identifier of the message with the button
        :param button_id: Identifier of the button
        :param shared_user_ids: Identifiers of the shared users
        :param only_check: Pass true to check that the users can be shared by the button instead of actually sharing them
        :param request_timeout: Request timeout
        """
        return await self(
            ShareUsersWithBot(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                shared_user_ids=shared_user_ids,
                only_check=only_check,
            ),
            request_timeout=request_timeout,
        )

    async def share_chat_with_bot(
        self,
        chat_id: int,
        message_id: int,
        button_id: int,
        shared_chat_id: int,
        only_check: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Shares a chat after pressing a keyboardButtonTypeRequestChat button with the bot
        :param chat_id: Identifier of the chat with the bot
        :param message_id: Identifier of the message with the button
        :param button_id: Identifier of the button
        :param shared_chat_id: Identifier of the shared chat
        :param only_check: Pass true to check that the chat can be shared by the button instead of actually sharing it. Doesn't check bot_is_member and bot_administrator_rights restrictions.
        :param request_timeout: Request timeout
        """
        return await self(
            ShareChatWithBot(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                shared_chat_id=shared_chat_id,
                only_check=only_check,
            ),
            request_timeout=request_timeout,
        )

    async def get_inline_query_results(
        self,
        bot_user_id: int,
        chat_id: int,
        query: str,
        offset: str,
        user_location: Location | None = None,
        request_timeout: float = 10.0,
    ) -> InlineQueryResults:
        """
        Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
        :param bot_user_id: Identifier of the target bot
        :param chat_id: Identifier of the chat where the query was sent
        :param query: Text of the query
        :param offset: Offset of the first entry to return; use empty string to get the first chunk of results
        :param user_location: Location of the user; pass null if unknown or the bot doesn't need user's location
        :param request_timeout: Request timeout
        """
        return await self(
            GetInlineQueryResults(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                query=query,
                offset=offset,
                user_location=user_location,
            ),
            request_timeout=request_timeout,
        )

    async def answer_inline_query(
        self,
        inline_query_id: int,
        is_personal: bool,
        results: list[InputInlineQueryResult],
        cache_time: int,
        next_offset: str,
        button: InlineQueryResultsButton | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the result of an inline query; for bots only
        :param inline_query_id: Identifier of the inline query
        :param is_personal: Pass true if results may be cached and returned only for the user that sent the query. By default, results may be returned to any user who sends the same query
        :param results: The results of the query
        :param cache_time: Allowed time to cache the results of the query, in seconds
        :param next_offset: Offset for the next inline query; pass an empty string if there are no more results
        :param button: Button to be shown above inline query results; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            AnswerInlineQuery(
                inline_query_id=inline_query_id,
                is_personal=is_personal,
                results=results,
                cache_time=cache_time,
                next_offset=next_offset,
                button=button,
            ),
            request_timeout=request_timeout,
        )

    async def get_popular_web_app_bots(
        self,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> FoundUsers:
        """
        Returns popular Web App bots
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of bots to be returned; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            GetPopularWebAppBots(
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_web_app(
        self,
        bot_user_id: int,
        web_app_short_name: str,
        request_timeout: float = 10.0,
    ) -> FoundWebApp:
        """
        Returns information about a Web App by its short name. Returns a 404 error if the Web App is not found
        :param bot_user_id: Identifier of the target bot
        :param web_app_short_name: Short name of the Web App
        :param request_timeout: Request timeout
        """
        return await self(
            SearchWebApp(
                bot_user_id=bot_user_id,
                web_app_short_name=web_app_short_name,
            ),
            request_timeout=request_timeout,
        )

    async def get_web_app_link_url(
        self,
        chat_id: int,
        bot_user_id: int,
        web_app_short_name: str,
        start_parameter: str,
        application_name: str,
        allow_write_access: bool,
        theme: ThemeParameters | None = None,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns an HTTPS URL of a Web App to open after a link of the type internalLinkTypeWebApp is clicked
        :param chat_id: Identifier of the chat in which the link was clicked; pass 0 if none
        :param bot_user_id: Identifier of the target bot
        :param web_app_short_name: Short name of the Web App
        :param start_parameter: Start parameter from internalLinkTypeWebApp
        :param application_name: Short name of the current application; 0-64 English letters, digits, and underscores
        :param allow_write_access: Pass true if the current user allowed the bot to send them messages
        :param theme: Preferred Web App theme; pass null to use the default theme
        :param request_timeout: Request timeout
        """
        return await self(
            GetWebAppLinkUrl(
                chat_id=chat_id,
                bot_user_id=bot_user_id,
                web_app_short_name=web_app_short_name,
                start_parameter=start_parameter,
                application_name=application_name,
                allow_write_access=allow_write_access,
                theme=theme,
            ),
            request_timeout=request_timeout,
        )

    async def get_main_web_app(
        self,
        chat_id: int,
        bot_user_id: int,
        start_parameter: str,
        application_name: str,
        theme: ThemeParameters | None = None,
        request_timeout: float = 10.0,
    ) -> MainWebApp:
        """
        Returns information needed to open the main Web App of a bot
        :param chat_id: Identifier of the chat in which the Web App is opened; pass 0 if none
        :param bot_user_id: Identifier of the target bot
        :param start_parameter: Start parameter from internalLinkTypeMainWebApp
        :param application_name: Short name of the current application; 0-64 English letters, digits, and underscores
        :param theme: Preferred Web App theme; pass null to use the default theme
        :param request_timeout: Request timeout
        """
        return await self(
            GetMainWebApp(
                chat_id=chat_id,
                bot_user_id=bot_user_id,
                start_parameter=start_parameter,
                application_name=application_name,
                theme=theme,
            ),
            request_timeout=request_timeout,
        )

    async def get_web_app_url(
        self,
        bot_user_id: int,
        url: str,
        application_name: str,
        theme: ThemeParameters | None = None,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns an HTTPS URL of a Web App to open from the side menu, a keyboardButtonTypeWebApp button, or an inlineQueryResultsButtonTypeWebApp button
        :param bot_user_id: Identifier of the target bot
        :param url: The URL from a keyboardButtonTypeWebApp button, inlineQueryResultsButtonTypeWebApp button, or an empty string when the bot is opened from the side menu
        :param application_name: Short name of the current application; 0-64 English letters, digits, and underscores
        :param theme: Preferred Web App theme; pass null to use the default theme
        :param request_timeout: Request timeout
        """
        return await self(
            GetWebAppUrl(
                bot_user_id=bot_user_id,
                url=url,
                application_name=application_name,
                theme=theme,
            ),
            request_timeout=request_timeout,
        )

    async def send_web_app_data(
        self,
        bot_user_id: int,
        button_text: str,
        data: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends data received from a keyboardButtonTypeWebApp Web App to a bot
        :param bot_user_id: Identifier of the target bot
        :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
        :param data: The data
        :param request_timeout: Request timeout
        """
        return await self(
            SendWebAppData(
                bot_user_id=bot_user_id,
                button_text=button_text,
                data=data,
            ),
            request_timeout=request_timeout,
        )

    async def open_web_app(
        self,
        chat_id: int,
        bot_user_id: int,
        url: str,
        application_name: str,
        message_thread_id: int,
        theme: ThemeParameters | None = None,
        reply_to: InputMessageReplyTo | None = None,
        request_timeout: float = 10.0,
    ) -> WebAppInfo:
        """
        Informs TDLib that a Web App is being opened from the attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button.
        :param chat_id: Identifier of the chat in which the Web App is opened. The Web App can't be opened in secret chats
        :param bot_user_id: Identifier of the bot, providing the Web App
        :param url: The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise
        :param application_name: Short name of the current application; 0-64 English letters, digits, and underscores
        :param message_thread_id: If not 0, the message thread identifier in which the message will be sent
        :param theme: Preferred Web App theme; pass null to use the default theme
        :param reply_to: Information about the message or story to be replied in the message sent by the Web App; pass null if none
        :param request_timeout: Request timeout
        """
        return await self(
            OpenWebApp(
                chat_id=chat_id,
                bot_user_id=bot_user_id,
                url=url,
                application_name=application_name,
                message_thread_id=message_thread_id,
                theme=theme,
                reply_to=reply_to,
            ),
            request_timeout=request_timeout,
        )

    async def close_web_app(
        self,
        web_app_launch_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that a previously opened Web App was closed
        :param web_app_launch_id: Identifier of Web App launch, received from openWebApp
        :param request_timeout: Request timeout
        """
        return await self(
            CloseWebApp(
                web_app_launch_id=web_app_launch_id,
            ),
            request_timeout=request_timeout,
        )

    async def answer_web_app_query(
        self,
        web_app_query_id: str,
        result: InputInlineQueryResult,
        request_timeout: float = 10.0,
    ) -> SentWebAppMessage:
        """
        Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only
        :param web_app_query_id: Identifier of the Web App query
        :param result: The result of the query
        :param request_timeout: Request timeout
        """
        return await self(
            AnswerWebAppQuery(
                web_app_query_id=web_app_query_id,
                result=result,
            ),
            request_timeout=request_timeout,
        )

    async def get_callback_query_answer(
        self,
        chat_id: int,
        message_id: int,
        payload: CallbackQueryPayload,
        request_timeout: float = 10.0,
    ) -> CallbackQueryAnswer:
        """
        Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
        :param chat_id: Identifier of the chat with the message
        :param message_id: Identifier of the message from which the query originated. The message must not be scheduled
        :param payload: Query payload
        :param request_timeout: Request timeout
        """
        return await self(
            GetCallbackQueryAnswer(
                chat_id=chat_id,
                message_id=message_id,
                payload=payload,
            ),
            request_timeout=request_timeout,
        )

    async def answer_callback_query(
        self,
        callback_query_id: int,
        text: str,
        show_alert: bool,
        url: str,
        cache_time: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the result of a callback query; for bots only
        :param callback_query_id: Identifier of the callback query
        :param text: Text of the answer
        :param show_alert: Pass true to show an alert to the user instead of a toast notification
        :param url: URL to be opened
        :param cache_time: Time during which the result of the query can be cached, in seconds
        :param request_timeout: Request timeout
        """
        return await self(
            AnswerCallbackQuery(
                callback_query_id=callback_query_id,
                text=text,
                show_alert=show_alert,
                url=url,
                cache_time=cache_time,
            ),
            request_timeout=request_timeout,
        )

    async def answer_shipping_query(
        self,
        shipping_query_id: int,
        shipping_options: list[ShippingOption],
        error_message: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the result of a shipping query; for bots only
        :param shipping_query_id: Identifier of the shipping query
        :param shipping_options: Available shipping options
        :param error_message: An error message, empty on success
        :param request_timeout: Request timeout
        """
        return await self(
            AnswerShippingQuery(
                shipping_query_id=shipping_query_id,
                shipping_options=shipping_options,
                error_message=error_message,
            ),
            request_timeout=request_timeout,
        )

    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: int,
        error_message: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the result of a pre-checkout query; for bots only
        :param pre_checkout_query_id: Identifier of the pre-checkout query
        :param error_message: An error message, empty on success
        :param request_timeout: Request timeout
        """
        return await self(
            AnswerPreCheckoutQuery(
                pre_checkout_query_id=pre_checkout_query_id,
                error_message=error_message,
            ),
            request_timeout=request_timeout,
        )

    async def set_game_score(
        self,
        chat_id: int,
        message_id: int,
        edit_message: bool,
        user_id: int,
        score: int,
        force: bool,
        request_timeout: float = 10.0,
    ) -> Message:
        """
        Updates the game score of the specified user in the game; for bots only
        :param chat_id: The chat to which the message with the game belongs
        :param message_id: Identifier of the message
        :param edit_message: Pass true to edit the game message to include the current scoreboard
        :param user_id: User identifier
        :param score: The new score
        :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        :param request_timeout: Request timeout
        """
        return await self(
            SetGameScore(
                chat_id=chat_id,
                message_id=message_id,
                edit_message=edit_message,
                user_id=user_id,
                score=score,
                force=force,
            ),
            request_timeout=request_timeout,
        )

    async def set_inline_game_score(
        self,
        inline_message_id: str,
        edit_message: bool,
        user_id: int,
        score: int,
        force: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Updates the game score of the specified user in a game; for bots only
        :param inline_message_id: Inline message identifier
        :param edit_message: Pass true to edit the game message to include the current scoreboard
        :param user_id: User identifier
        :param score: The new score
        :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        :param request_timeout: Request timeout
        """
        return await self(
            SetInlineGameScore(
                inline_message_id=inline_message_id,
                edit_message=edit_message,
                user_id=user_id,
                score=score,
                force=force,
            ),
            request_timeout=request_timeout,
        )

    async def get_game_high_scores(
        self,
        chat_id: int,
        message_id: int,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> GameHighScores:
        """
        Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only
        :param chat_id: The chat that contains the message with the game
        :param message_id: Identifier of the message
        :param user_id: User identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetGameHighScores(
                chat_id=chat_id,
                message_id=message_id,
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_inline_game_high_scores(
        self,
        inline_message_id: str,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> GameHighScores:
        """
        Returns game high scores and some part of the high score table in the range of the specified user; for bots only
        :param inline_message_id: Inline message identifier
        :param user_id: User identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetInlineGameHighScores(
                inline_message_id=inline_message_id,
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat_reply_markup(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a replyMarkupForceReply reply markup has been used. An updateChatReplyMarkup update will be sent if the reply markup is changed
        :param chat_id: Chat identifier
        :param message_id: The message identifier of the used keyboard
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChatReplyMarkup(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def send_chat_action(
        self,
        chat_id: int,
        message_thread_id: int,
        business_connection_id: str,
        action: ChatAction | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends a notification about user activity in a chat
        :param chat_id: Chat identifier
        :param message_thread_id: If not 0, the message thread identifier in which the action was performed
        :param business_connection_id: Unique identifier of business connection on behalf of which to send the request; for bots only
        :param action: The action description; pass null to cancel the currently active action
        :param request_timeout: Request timeout
        """
        return await self(
            SendChatAction(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                business_connection_id=business_connection_id,
                action=action,
            ),
            request_timeout=request_timeout,
        )

    async def open_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats)
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            OpenChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def close_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            CloseChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def view_messages(
        self,
        chat_id: int,
        message_ids: list[int],
        force_read: bool,
        source: MessageSource | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that messages are being viewed by the user. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen (excluding the button).
        :param chat_id: Chat identifier
        :param message_ids: The identifiers of the messages being viewed
        :param force_read: Pass true to mark as read the specified messages even the chat is closed
        :param source: Source of the message view; pass null to guess the source based on chat open state
        :param request_timeout: Request timeout
        """
        return await self(
            ViewMessages(
                chat_id=chat_id,
                message_ids=message_ids,
                force_read=force_read,
                source=source,
            ),
            request_timeout=request_timeout,
        )

    async def open_message_content(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message).
        :param chat_id: Chat identifier of the message
        :param message_id: Identifier of the message with the opened content
        :param request_timeout: Request timeout
        """
        return await self(
            OpenMessageContent(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def click_animated_emoji_message(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Sticker:
        """
        Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played
        :param chat_id: Chat identifier of the message
        :param message_id: Identifier of the clicked message
        :param request_timeout: Request timeout
        """
        return await self(
            ClickAnimatedEmojiMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_internal_link(
        self,
        type: InternalLinkType,
        is_http: bool,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns an HTTPS or a tg: link with the given type. Can be called before authorization
        :param type: Expected type of the link
        :param is_http: Pass true to create an HTTPS link (only available for some link types); pass false to create a tg: link
        :param request_timeout: Request timeout
        """
        return await self(
            GetInternalLink(
                type=type,
                is_http=is_http,
            ),
            request_timeout=request_timeout,
        )

    async def get_internal_link_type(
        self,
        link: str,
        request_timeout: float = 10.0,
    ) -> InternalLinkType:
        """
        Returns information about the type of internal link. Returns a 404 error if the link is not internal. Can be called before authorization
        :param link: The link
        :param request_timeout: Request timeout
        """
        return await self(
            GetInternalLinkType(
                link=link,
            ),
            request_timeout=request_timeout,
        )

    async def get_external_link_info(
        self,
        link: str,
        request_timeout: float = 10.0,
    ) -> LoginUrlInfo:
        """
        Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if link preview is disabled in secret chats
        :param link: The link
        :param request_timeout: Request timeout
        """
        return await self(
            GetExternalLinkInfo(
                link=link,
            ),
            request_timeout=request_timeout,
        )

    async def get_external_link(
        self,
        link: str,
        allow_write_access: bool,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed
        :param link: The HTTP link
        :param allow_write_access: Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
        :param request_timeout: Request timeout
        """
        return await self(
            GetExternalLink(
                link=link,
                allow_write_access=allow_write_access,
            ),
            request_timeout=request_timeout,
        )

    async def read_all_chat_mentions(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Marks all mentions in a chat as read
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            ReadAllChatMentions(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def read_all_message_thread_mentions(
        self,
        chat_id: int,
        message_thread_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Marks all mentions in a forum topic as read
        :param chat_id: Chat identifier
        :param message_thread_id: Message thread identifier in which mentions are marked as read
        :param request_timeout: Request timeout
        """
        return await self(
            ReadAllMessageThreadMentions(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_timeout=request_timeout,
        )

    async def read_all_chat_reactions(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Marks all reactions in a chat or a forum topic as read
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            ReadAllChatReactions(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def read_all_message_thread_reactions(
        self,
        chat_id: int,
        message_thread_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Marks all reactions in a forum topic as read
        :param chat_id: Chat identifier
        :param message_thread_id: Message thread identifier in which reactions are marked as read
        :param request_timeout: Request timeout
        """
        return await self(
            ReadAllMessageThreadReactions(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_timeout=request_timeout,
        )

    async def create_private_chat(
        self,
        user_id: int,
        force: bool,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Returns an existing chat corresponding to a given user
        :param user_id: User identifier
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :param request_timeout: Request timeout
        """
        return await self(
            CreatePrivateChat(
                user_id=user_id,
                force=force,
            ),
            request_timeout=request_timeout,
        )

    async def create_basic_group_chat(
        self,
        basic_group_id: int,
        force: bool,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known basic group
        :param basic_group_id: Basic group identifier
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :param request_timeout: Request timeout
        """
        return await self(
            CreateBasicGroupChat(
                basic_group_id=basic_group_id,
                force=force,
            ),
            request_timeout=request_timeout,
        )

    async def create_supergroup_chat(
        self,
        supergroup_id: int,
        force: bool,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known supergroup or channel
        :param supergroup_id: Supergroup or channel identifier
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :param request_timeout: Request timeout
        """
        return await self(
            CreateSupergroupChat(
                supergroup_id=supergroup_id,
                force=force,
            ),
            request_timeout=request_timeout,
        )

    async def create_secret_chat(
        self,
        secret_chat_id: int,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known secret chat
        :param secret_chat_id: Secret chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            CreateSecretChat(
                secret_chat_id=secret_chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def create_new_basic_group_chat(
        self,
        title: str,
        message_auto_delete_time: int,
        user_ids: list[int] | None = None,
        request_timeout: float = 10.0,
    ) -> CreatedBasicGroupChat:
        """
        Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns information about the newly created chat
        :param title: Title of the new basic group; 1-128 characters
        :param message_auto_delete_time: Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :param user_ids: Identifiers of users to be added to the basic group; may be empty to create a basic group without other members
        :param request_timeout: Request timeout
        """
        return await self(
            CreateNewBasicGroupChat(
                title=title,
                message_auto_delete_time=message_auto_delete_time,
                user_ids=user_ids,
            ),
            request_timeout=request_timeout,
        )

    async def create_new_supergroup_chat(
        self,
        title: str,
        is_forum: bool,
        is_channel: bool,
        description: str,
        message_auto_delete_time: int,
        for_import: bool,
        location: ChatLocation | None = None,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat
        :param title: Title of the new chat; 1-128 characters
        :param is_forum: Pass true to create a forum supergroup chat
        :param is_channel: Pass true to create a channel chat; ignored if a forum is created
        :param description: Chat description; 0-255 characters
        :param message_auto_delete_time: Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :param for_import: Pass true to create a supergroup for importing messages using importMessages
        :param location: Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat
        :param request_timeout: Request timeout
        """
        return await self(
            CreateNewSupergroupChat(
                title=title,
                is_forum=is_forum,
                is_channel=is_channel,
                description=description,
                message_auto_delete_time=message_auto_delete_time,
                for_import=for_import,
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def create_new_secret_chat(
        self,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Creates a new secret chat. Returns the newly created chat
        :param user_id: Identifier of the target user
        :param request_timeout: Request timeout
        """
        return await self(
            CreateNewSecretChat(
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def upgrade_basic_group_chat_to_supergroup_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires owner privileges. Deactivates the original basic group
        :param chat_id: Identifier of the chat to upgrade
        :param request_timeout: Request timeout
        """
        return await self(
            UpgradeBasicGroupChatToSupergroupChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_lists_to_add_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatLists:
        """
        Returns chat lists to which the chat can be added. This is an offline request
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatListsToAddChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def add_chat_to_list(
        self,
        chat_id: int,
        chat_list: ChatList,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed
        :param chat_id: Chat identifier
        :param chat_list: The chat list. Use getChatListsToAddChat to get suitable chat lists
        :param request_timeout: Request timeout
        """
        return await self(
            AddChatToList(
                chat_id=chat_id,
                chat_list=chat_list,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_folder(
        self,
        chat_folder_id: int,
        request_timeout: float = 10.0,
    ) -> ChatFolder:
        """
        Returns information about a chat folder by its identifier
        :param chat_folder_id: Chat folder identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatFolder(
                chat_folder_id=chat_folder_id,
            ),
            request_timeout=request_timeout,
        )

    async def create_chat_folder(
        self,
        folder: ChatFolder,
        request_timeout: float = 10.0,
    ) -> ChatFolderInfo:
        """
        Creates new chat folder. Returns information about the created chat folder. There can be up to getOption('chat_folder_count_max') chat folders, but the limit can be increased with Telegram Premium
        :param folder: The new chat folder
        :param request_timeout: Request timeout
        """
        return await self(
            CreateChatFolder(
                folder=folder,
            ),
            request_timeout=request_timeout,
        )

    async def edit_chat_folder(
        self,
        chat_folder_id: int,
        folder: ChatFolder,
        request_timeout: float = 10.0,
    ) -> ChatFolderInfo:
        """
        Edits existing chat folder. Returns information about the edited chat folder
        :param chat_folder_id: Chat folder identifier
        :param folder: The edited chat folder
        :param request_timeout: Request timeout
        """
        return await self(
            EditChatFolder(
                chat_folder_id=chat_folder_id,
                folder=folder,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat_folder(
        self,
        chat_folder_id: int,
        leave_chat_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes existing chat folder
        :param chat_folder_id: Chat folder identifier
        :param leave_chat_ids: Identifiers of the chats to leave. The chats must be pinned or always included in the folder
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChatFolder(
                chat_folder_id=chat_folder_id,
                leave_chat_ids=leave_chat_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_folder_chats_to_leave(
        self,
        chat_folder_id: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns identifiers of pinned or always included chats from a chat folder, which are suggested to be left when the chat folder is deleted
        :param chat_folder_id: Chat folder identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatFolderChatsToLeave(
                chat_folder_id=chat_folder_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_folder_chat_count(
        self,
        folder: ChatFolder,
        request_timeout: float = 10.0,
    ) -> Count:
        """
        Returns approximate number of chats in a being created chat folder. Main and archive chat lists must be fully preloaded for this function to work correctly
        :param folder: The new chat folder
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatFolderChatCount(
                folder=folder,
            ),
            request_timeout=request_timeout,
        )

    async def reorder_chat_folders(
        self,
        chat_folder_ids: list[int],
        main_chat_list_position: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the order of chat folders
        :param chat_folder_ids: Identifiers of chat folders in the new correct order
        :param main_chat_list_position: Position of the main chat list among chat folders, 0-based. Can be non-zero only for Premium users
        :param request_timeout: Request timeout
        """
        return await self(
            ReorderChatFolders(
                chat_folder_ids=chat_folder_ids,
                main_chat_list_position=main_chat_list_position,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_chat_folder_tags(
        self,
        are_tags_enabled: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether chat folder tags are enabled
        :param are_tags_enabled: Pass true to enable folder tags; pass false to disable them
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleChatFolderTags(
                are_tags_enabled=are_tags_enabled,
            ),
            request_timeout=request_timeout,
        )

    async def get_recommended_chat_folders(
        self,
        request_timeout: float = 10.0,
    ) -> RecommendedChatFolders:
        """
        Returns recommended chat folders for the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecommendedChatFolders(),
            request_timeout=request_timeout,
        )

    async def get_chat_folder_default_icon_name(
        self,
        folder: ChatFolder,
        request_timeout: float = 10.0,
    ) -> ChatFolderIcon:
        """
        Returns default icon name for a folder. Can be called synchronously
        :param folder: Chat folder
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatFolderDefaultIconName(
                folder=folder,
            ),
            request_timeout=request_timeout,
        )

    async def get_chats_for_chat_folder_invite_link(
        self,
        chat_folder_id: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns identifiers of chats from a chat folder, suitable for adding to a chat folder invite link
        :param chat_folder_id: Chat folder identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatsForChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
            ),
            request_timeout=request_timeout,
        )

    async def create_chat_folder_invite_link(
        self,
        chat_folder_id: int,
        name: str,
        chat_ids: list[int],
        request_timeout: float = 10.0,
    ) -> ChatFolderInviteLink:
        """
        Creates a new invite link for a chat folder. A link can be created for a chat folder if it has only pinned and included chats
        :param chat_folder_id: Chat folder identifier
        :param name: Name of the link; 0-32 characters
        :param chat_ids: Identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link creation
        :param request_timeout: Request timeout
        """
        return await self(
            CreateChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
                name=name,
                chat_ids=chat_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_folder_invite_links(
        self,
        chat_folder_id: int,
        request_timeout: float = 10.0,
    ) -> ChatFolderInviteLinks:
        """
        Returns invite links created by the current user for a shareable chat folder
        :param chat_folder_id: Chat folder identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatFolderInviteLinks(
                chat_folder_id=chat_folder_id,
            ),
            request_timeout=request_timeout,
        )

    async def edit_chat_folder_invite_link(
        self,
        chat_folder_id: int,
        invite_link: str,
        name: str,
        chat_ids: list[int],
        request_timeout: float = 10.0,
    ) -> ChatFolderInviteLink:
        """
        Edits an invite link for a chat folder
        :param chat_folder_id: Chat folder identifier
        :param invite_link: Invite link to be edited
        :param name: New name of the link; 0-32 characters
        :param chat_ids: New identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link editing
        :param request_timeout: Request timeout
        """
        return await self(
            EditChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
                invite_link=invite_link,
                name=name,
                chat_ids=chat_ids,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat_folder_invite_link(
        self,
        chat_folder_id: int,
        invite_link: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes an invite link for a chat folder
        :param chat_folder_id: Chat folder identifier
        :param invite_link: Invite link to be deleted
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
                invite_link=invite_link,
            ),
            request_timeout=request_timeout,
        )

    async def check_chat_folder_invite_link(
        self,
        invite_link: str,
        request_timeout: float = 10.0,
    ) -> ChatFolderInviteLinkInfo:
        """
        Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder
        :param invite_link: Invite link to be checked
        :param request_timeout: Request timeout
        """
        return await self(
            CheckChatFolderInviteLink(
                invite_link=invite_link,
            ),
            request_timeout=request_timeout,
        )

    async def add_chat_folder_by_invite_link(
        self,
        invite_link: str,
        chat_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a chat folder by an invite link
        :param invite_link: Invite link for the chat folder
        :param chat_ids: Identifiers of the chats added to the chat folder. The chats are automatically joined if they aren't joined yet
        :param request_timeout: Request timeout
        """
        return await self(
            AddChatFolderByInviteLink(
                invite_link=invite_link,
                chat_ids=chat_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_folder_new_chats(
        self,
        chat_folder_id: int,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns new chats added to a shareable chat folder by its owner. The method must be called at most once in getOption('chat_folder_new_chats_update_period') for the given chat folder
        :param chat_folder_id: Chat folder identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatFolderNewChats(
                chat_folder_id=chat_folder_id,
            ),
            request_timeout=request_timeout,
        )

    async def process_chat_folder_new_chats(
        self,
        chat_folder_id: int,
        added_chat_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Process new chats added to a shareable chat folder by its owner
        :param chat_folder_id: Chat folder identifier
        :param added_chat_ids: Identifiers of the new chats, which are added to the chat folder. The chats are automatically joined if they aren't joined yet
        :param request_timeout: Request timeout
        """
        return await self(
            ProcessChatFolderNewChats(
                chat_folder_id=chat_folder_id,
                added_chat_ids=added_chat_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_archive_chat_list_settings(
        self,
        request_timeout: float = 10.0,
    ) -> ArchiveChatListSettings:
        """
        Returns settings for automatic moving of chats to and from the Archive chat lists
        :param request_timeout: Request timeout
        """
        return await self(
            GetArchiveChatListSettings(),
            request_timeout=request_timeout,
        )

    async def set_archive_chat_list_settings(
        self,
        settings: ArchiveChatListSettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes settings for automatic moving of chats to and from the Archive chat lists
        :param settings: New settings
        :param request_timeout: Request timeout
        """
        return await self(
            SetArchiveChatListSettings(
                settings=settings,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_title(
        self,
        chat_id: int,
        title: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info member right
        :param chat_id: Chat identifier
        :param title: New title of the chat; 1-128 characters
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatTitle(
                chat_id=chat_id,
                title=title,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_photo(
        self,
        chat_id: int,
        photo: InputChatPhoto | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info member right
        :param chat_id: Chat identifier
        :param photo: New chat photo; pass null to delete the chat photo
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatPhoto(
                chat_id=chat_id,
                photo=photo,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_accent_color(
        self,
        chat_id: int,
        accent_color_id: int,
        background_custom_emoji_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes accent color and background custom emoji of a channel chat. Requires can_change_info administrator right
        :param chat_id: Chat identifier
        :param accent_color_id: Identifier of the accent color to use. The chat must have at least accentColor.min_channel_chat_boost_level boost level to pass the corresponding color
        :param background_custom_emoji_id: Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none. Use chatBoostLevelFeatures.can_set_background_custom_emoji to check whether a custom emoji can be set
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatAccentColor(
                chat_id=chat_id,
                accent_color_id=accent_color_id,
                background_custom_emoji_id=background_custom_emoji_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_profile_accent_color(
        self,
        chat_id: int,
        profile_accent_color_id: int,
        profile_background_custom_emoji_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes accent color and background custom emoji for profile of a supergroup or channel chat. Requires can_change_info administrator right
        :param chat_id: Chat identifier
        :param profile_accent_color_id: Identifier of the accent color to use for profile; pass -1 if none. The chat must have at least profileAccentColor.min_supergroup_chat_boost_level for supergroups
        :param profile_background_custom_emoji_id: Identifier of a custom emoji to be shown on the chat's profile photo background; 0 if none. Use chatBoostLevelFeatures.can_set_profile_background_custom_emoji to check whether a custom emoji can be set
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatProfileAccentColor(
                chat_id=chat_id,
                profile_accent_color_id=profile_accent_color_id,
                profile_background_custom_emoji_id=profile_background_custom_emoji_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_message_auto_delete_time(
        self,
        chat_id: int,
        message_auto_delete_time: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the message auto-delete or self-destruct (for secret chats) time in a chat. Requires change_info administrator right in basic groups, supergroups and channels
        :param chat_id: Chat identifier
        :param message_auto_delete_time: New time value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatMessageAutoDeleteTime(
                chat_id=chat_id,
                message_auto_delete_time=message_auto_delete_time,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_emoji_status(
        self,
        chat_id: int,
        emoji_status: EmojiStatus | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the emoji status of a chat. Use chatBoostLevelFeatures.can_set_emoji_status to check whether an emoji status can be set. Requires can_change_info administrator right
        :param chat_id: Chat identifier
        :param emoji_status: New emoji status; pass null to remove emoji status
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatEmojiStatus(
                chat_id=chat_id,
                emoji_status=emoji_status,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_permissions(
        self,
        chat_id: int,
        permissions: ChatPermissions,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right
        :param chat_id: Chat identifier
        :param permissions: New non-administrator members permissions in the chat
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatPermissions(
                chat_id=chat_id,
                permissions=permissions,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_background(
        self,
        chat_id: int,
        dark_theme_dimming: int,
        only_for_self: bool,
        background: InputBackground | None = None,
        type: BackgroundType | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the background in a specific chat. Supported only in private and secret chats with non-deleted users, and in chats with sufficient boost level and can_change_info administrator right
        :param chat_id: Chat identifier
        :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100. Applied only to Wallpaper and Fill types of background
        :param only_for_self: Pass true to set background only for self; pass false to set background for all chat users. Always false for backgrounds set in boosted chats. Background can be set for both users only by Telegram Premium users and if set background isn't of the type inputBackgroundPrevious
        :param background: The input background to use; pass null to create a new filled or chat theme background
        :param type: Background type; pass null to use default background type for the chosen background; backgroundTypeChatTheme isn't supported for private and secret chats.
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatBackground(
                chat_id=chat_id,
                dark_theme_dimming=dark_theme_dimming,
                only_for_self=only_for_self,
                background=background,
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def delete_chat_background(
        self,
        chat_id: int,
        restore_previous: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes background in a specific chat
        :param chat_id: Chat identifier
        :param restore_previous: Pass true to restore previously set background. Can be used only in private and secret chats with non-deleted users if userFullInfo.set_chat_background == true.
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteChatBackground(
                chat_id=chat_id,
                restore_previous=restore_previous,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_theme(
        self,
        chat_id: int,
        theme_name: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the chat theme. Supported only in private and secret chats
        :param chat_id: Chat identifier
        :param theme_name: Name of the new chat theme; pass an empty string to return the default theme
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatTheme(
                chat_id=chat_id,
                theme_name=theme_name,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_draft_message(
        self,
        chat_id: int,
        message_thread_id: int,
        draft_message: DraftMessage | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the draft message in a chat
        :param chat_id: Chat identifier
        :param message_thread_id: If not 0, the message thread identifier in which the draft was changed
        :param draft_message: New draft message; pass null to remove the draft. All files in draft message content must be of the type inputFileLocal. Media thumbnails and captions are ignored
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatDraftMessage(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                draft_message=draft_message,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_notification_settings(
        self,
        chat_id: int,
        notification_settings: ChatNotificationSettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed
        :param chat_id: Chat identifier
        :param notification_settings: New notification settings for the chat. If the chat is muted for more than 366 days, it is considered to be muted forever
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatNotificationSettings(
                chat_id=chat_id,
                notification_settings=notification_settings,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_chat_has_protected_content(
        self,
        chat_id: int,
        has_protected_content: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges
        :param chat_id: Chat identifier
        :param has_protected_content: New value of has_protected_content
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleChatHasProtectedContent(
                chat_id=chat_id,
                has_protected_content=has_protected_content,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_chat_view_as_topics(
        self,
        chat_id: int,
        view_as_topics: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the view_as_topics setting of a forum chat or Saved Messages
        :param chat_id: Chat identifier
        :param view_as_topics: New value of view_as_topics
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleChatViewAsTopics(
                chat_id=chat_id,
                view_as_topics=view_as_topics,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_translatable(
        self,
        chat_id: int,
        is_translatable: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the translatable state of a chat
        :param chat_id: Chat identifier
        :param is_translatable: New value of is_translatable
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleChatIsTranslatable(
                chat_id=chat_id,
                is_translatable=is_translatable,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_marked_as_unread(
        self,
        chat_id: int,
        is_marked_as_unread: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the marked as unread state of a chat
        :param chat_id: Chat identifier
        :param is_marked_as_unread: New value of is_marked_as_unread
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleChatIsMarkedAsUnread(
                chat_id=chat_id,
                is_marked_as_unread=is_marked_as_unread,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_chat_default_disable_notification(
        self,
        chat_id: int,
        default_disable_notification: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the value of the default disable_notification parameter, used when a message is sent to a chat
        :param chat_id: Chat identifier
        :param default_disable_notification: New value of default_disable_notification
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleChatDefaultDisableNotification(
                chat_id=chat_id,
                default_disable_notification=default_disable_notification,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_available_reactions(
        self,
        chat_id: int,
        available_reactions: ChatAvailableReactions,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info member right
        :param chat_id: Identifier of the chat
        :param available_reactions: Reactions available in the chat. All explicitly specified emoji reactions must be active. In channel chats up to the chat's boost level custom emoji reactions can be explicitly specified
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatAvailableReactions(
                chat_id=chat_id,
                available_reactions=available_reactions,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_client_data(
        self,
        chat_id: int,
        client_data: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes application-specific data associated with a chat
        :param chat_id: Chat identifier
        :param client_data: New value of client_data
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatClientData(
                chat_id=chat_id,
                client_data=client_data,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_description(
        self,
        chat_id: int,
        description: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info member right
        :param chat_id: Identifier of the chat
        :param description: New chat description; 0-255 characters
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatDescription(
                chat_id=chat_id,
                description=description,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_discussion_group(
        self,
        chat_id: int,
        discussion_chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the discussion group of a channel chat; requires can_change_info administrator right in the channel if it is specified
        :param chat_id: Identifier of the channel chat. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages member right in the supergroup)
        :param discussion_chat_id: Identifier of a new channel's discussion group. Use 0 to remove the discussion group. Use the method getSuitableDiscussionChats to find all suitable groups.
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatDiscussionGroup(
                chat_id=chat_id,
                discussion_chat_id=discussion_chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_location(
        self,
        chat_id: int,
        location: ChatLocation,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use
        :param chat_id: Chat identifier
        :param location: New location for the chat; must be valid and not null
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatLocation(
                chat_id=chat_id,
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_slow_mode_delay(
        self,
        chat_id: int,
        slow_mode_delay: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members right
        :param chat_id: Chat identifier
        :param slow_mode_delay: New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatSlowModeDelay(
                chat_id=chat_id,
                slow_mode_delay=slow_mode_delay,
            ),
            request_timeout=request_timeout,
        )

    async def pin_chat_message(
        self,
        chat_id: int,
        message_id: int,
        disable_notification: bool,
        only_for_self: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Pins a message in a chat. A message can be pinned only if messageProperties.can_be_pinned
        :param chat_id: Identifier of the chat
        :param message_id: Identifier of the new pinned message
        :param disable_notification: Pass true to disable notification about the pinned message. Notifications are always disabled in channels and private chats
        :param only_for_self: Pass true to pin the message only for self; private chats only
        :param request_timeout: Request timeout
        """
        return await self(
            PinChatMessage(
                chat_id=chat_id,
                message_id=message_id,
                disable_notification=disable_notification,
                only_for_self=only_for_self,
            ),
            request_timeout=request_timeout,
        )

    async def unpin_chat_message(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a pinned message from a chat; requires can_pin_messages member right if the chat is a basic group or supergroup, or can_edit_messages administrator right if the chat is a channel
        :param chat_id: Identifier of the chat
        :param message_id: Identifier of the removed pinned message
        :param request_timeout: Request timeout
        """
        return await self(
            UnpinChatMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def unpin_all_chat_messages(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes all pinned messages from a chat; requires can_pin_messages member right if the chat is a basic group or supergroup, or can_edit_messages administrator right if the chat is a channel
        :param chat_id: Identifier of the chat
        :param request_timeout: Request timeout
        """
        return await self(
            UnpinAllChatMessages(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def unpin_all_message_thread_messages(
        self,
        chat_id: int,
        message_thread_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes all pinned messages from a forum topic; requires can_pin_messages member right in the supergroup
        :param chat_id: Identifier of the chat
        :param message_thread_id: Message thread identifier in which messages will be unpinned
        :param request_timeout: Request timeout
        """
        return await self(
            UnpinAllMessageThreadMessages(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_timeout=request_timeout,
        )

    async def join_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method. May return an error with a message 'INVITE_REQUEST_SENT' if only a join request was created
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            JoinChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def leave_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes the current user from chat members. Private and secret chats can't be left using this method
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            LeaveChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def add_chat_member(
        self,
        chat_id: int,
        user_id: int,
        forward_limit: int,
        request_timeout: float = 10.0,
    ) -> FailedToAddMembers:
        """
        Adds a new member to a chat; requires can_invite_users member right. Members can't be added to private or secret chats. Returns information about members that weren't added
        :param chat_id: Chat identifier
        :param user_id: Identifier of the user
        :param forward_limit: The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels, or if the added user is a bot
        :param request_timeout: Request timeout
        """
        return await self(
            AddChatMember(
                chat_id=chat_id,
                user_id=user_id,
                forward_limit=forward_limit,
            ),
            request_timeout=request_timeout,
        )

    async def add_chat_members(
        self,
        chat_id: int,
        user_ids: list[int],
        request_timeout: float = 10.0,
    ) -> FailedToAddMembers:
        """
        Adds multiple new members to a chat; requires can_invite_users member right. Currently, this method is only available for supergroups and channels.
        :param chat_id: Chat identifier
        :param user_ids: Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels
        :param request_timeout: Request timeout
        """
        return await self(
            AddChatMembers(
                chat_id=chat_id,
                user_ids=user_ids,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_member_status(
        self,
        chat_id: int,
        member_id: MessageSender,
        status: ChatMemberStatus,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the status of a chat member; requires can_invite_users member right to add a chat member, can_promote_members administrator right to change administrator rights of the member,
        :param chat_id: Chat identifier
        :param member_id: Member identifier. Chats can be only banned and unbanned in supergroups and channels
        :param status: The new status of the member in the chat
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatMemberStatus(
                chat_id=chat_id,
                member_id=member_id,
                status=status,
            ),
            request_timeout=request_timeout,
        )

    async def ban_chat_member(
        self,
        chat_id: int,
        member_id: MessageSender,
        banned_until_date: int,
        revoke_messages: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Bans a member in a chat; requires can_restrict_members administrator right. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first
        :param chat_id: Chat identifier
        :param member_id: Member identifier
        :param banned_until_date: Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups and if a chat is banned
        :param revoke_messages: Pass true to delete all messages in the chat for the user that is being removed. Always true for supergroups and channels
        :param request_timeout: Request timeout
        """
        return await self(
            BanChatMember(
                chat_id=chat_id,
                member_id=member_id,
                banned_until_date=banned_until_date,
                revoke_messages=revoke_messages,
            ),
            request_timeout=request_timeout,
        )

    async def can_transfer_ownership(
        self,
        request_timeout: float = 10.0,
    ) -> CanTransferOwnershipResult:
        """
        Checks whether the current session can be used to transfer a chat ownership to another user
        :param request_timeout: Request timeout
        """
        return await self(
            CanTransferOwnership(),
            request_timeout=request_timeout,
        )

    async def transfer_chat_ownership(
        self,
        chat_id: int,
        user_id: int,
        password: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the owner of a chat; requires owner privileges in the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats
        :param chat_id: Chat identifier
        :param user_id: Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user
        :param password: The 2-step verification password of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            TransferChatOwnership(
                chat_id=chat_id,
                user_id=user_id,
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_member(
        self,
        chat_id: int,
        member_id: MessageSender,
        request_timeout: float = 10.0,
    ) -> ChatMember:
        """
        Returns information about a single member of a chat
        :param chat_id: Chat identifier
        :param member_id: Member identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatMember(
                chat_id=chat_id,
                member_id=member_id,
            ),
            request_timeout=request_timeout,
        )

    async def search_chat_members(
        self,
        chat_id: int,
        query: str,
        limit: int,
        filter: ChatMembersFilter | None = None,
        request_timeout: float = 10.0,
    ) -> ChatMembers:
        """
        Searches for a specified query in the first name, last name and usernames of the members of a specified chat. Requires administrator rights if the chat is a channel
        :param chat_id: Chat identifier
        :param query: Query to search for
        :param limit: The maximum number of users to be returned; up to 200
        :param filter: The type of users to search for; pass null to search among all chat members
        :param request_timeout: Request timeout
        """
        return await self(
            SearchChatMembers(
                chat_id=chat_id,
                query=query,
                limit=limit,
                filter=filter,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_administrators(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatAdministrators:
        """
        Returns a list of administrators of the chat with their custom titles
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatAdministrators(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def clear_all_draft_messages(
        self,
        exclude_secret_chats: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears message drafts in all chats
        :param exclude_secret_chats: Pass true to keep local message drafts in secret chats
        :param request_timeout: Request timeout
        """
        return await self(
            ClearAllDraftMessages(
                exclude_secret_chats=exclude_secret_chats,
            ),
            request_timeout=request_timeout,
        )

    async def get_saved_notification_sound(
        self,
        notification_sound_id: int,
        request_timeout: float = 10.0,
    ) -> NotificationSounds:
        """
        Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier
        :param notification_sound_id: Identifier of the notification sound
        :param request_timeout: Request timeout
        """
        return await self(
            GetSavedNotificationSound(
                notification_sound_id=notification_sound_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_saved_notification_sounds(
        self,
        request_timeout: float = 10.0,
    ) -> NotificationSounds:
        """
        Returns the list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used
        :param request_timeout: Request timeout
        """
        return await self(
            GetSavedNotificationSounds(),
            request_timeout=request_timeout,
        )

    async def add_saved_notification_sound(
        self,
        sound: InputFile,
        request_timeout: float = 10.0,
    ) -> NotificationSound:
        """
        Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed
        :param sound: Notification sound file to add
        :param request_timeout: Request timeout
        """
        return await self(
            AddSavedNotificationSound(
                sound=sound,
            ),
            request_timeout=request_timeout,
        )

    async def remove_saved_notification_sound(
        self,
        notification_sound_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a notification sound from the list of saved notification sounds
        :param notification_sound_id: Identifier of the notification sound
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveSavedNotificationSound(
                notification_sound_id=notification_sound_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_notification_settings_exceptions(
        self,
        compare_sound: bool,
        scope: NotificationSettingsScope | None = None,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns the list of chats with non-default notification settings for new messages
        :param compare_sound: Pass true to include in the response chats with only non-default sound
        :param scope: If specified, only chats from the scope will be returned; pass null to return chats from all scopes
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatNotificationSettingsExceptions(
                compare_sound=compare_sound,
                scope=scope,
            ),
            request_timeout=request_timeout,
        )

    async def get_scope_notification_settings(
        self,
        scope: NotificationSettingsScope,
        request_timeout: float = 10.0,
    ) -> ScopeNotificationSettings:
        """
        Returns the notification settings for chats of a given type
        :param scope: Types of chats for which to return the notification settings information
        :param request_timeout: Request timeout
        """
        return await self(
            GetScopeNotificationSettings(
                scope=scope,
            ),
            request_timeout=request_timeout,
        )

    async def set_scope_notification_settings(
        self,
        scope: NotificationSettingsScope,
        notification_settings: ScopeNotificationSettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes notification settings for chats of a given type
        :param scope: Types of chats for which to change the notification settings
        :param notification_settings: The new notification settings for the given scope
        :param request_timeout: Request timeout
        """
        return await self(
            SetScopeNotificationSettings(
                scope=scope,
                notification_settings=notification_settings,
            ),
            request_timeout=request_timeout,
        )

    async def set_reaction_notification_settings(
        self,
        notification_settings: ReactionNotificationSettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes notification settings for reactions
        :param notification_settings: The new notification settings for reactions
        :param request_timeout: Request timeout
        """
        return await self(
            SetReactionNotificationSettings(
                notification_settings=notification_settings,
            ),
            request_timeout=request_timeout,
        )

    async def reset_all_notification_settings(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Resets all chat and scope notification settings to their default values. By default, all chats are unmuted and message previews are shown
        :param request_timeout: Request timeout
        """
        return await self(
            ResetAllNotificationSettings(),
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_pinned(
        self,
        chat_list: ChatList,
        chat_id: int,
        is_pinned: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the pinned state of a chat. There can be up to getOption('pinned_chat_count_max')/getOption('pinned_archived_chat_count_max') pinned non-secret chats and the same number of secret chats in the main/archive chat list. The limit can be increased with Telegram Premium
        :param chat_list: Chat list in which to change the pinned state of the chat
        :param chat_id: Chat identifier
        :param is_pinned: Pass true to pin the chat; pass false to unpin it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleChatIsPinned(
                chat_list=chat_list,
                chat_id=chat_id,
                is_pinned=is_pinned,
            ),
            request_timeout=request_timeout,
        )

    async def set_pinned_chats(
        self,
        chat_list: ChatList,
        chat_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the order of pinned chats
        :param chat_list: Chat list in which to change the order of pinned chats
        :param chat_ids: The new list of pinned chats
        :param request_timeout: Request timeout
        """
        return await self(
            SetPinnedChats(
                chat_list=chat_list,
                chat_ids=chat_ids,
            ),
            request_timeout=request_timeout,
        )

    async def read_chat_list(
        self,
        chat_list: ChatList,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Traverse all chats in a chat list and marks all messages in the chats as read
        :param chat_list: Chat list in which to mark all chats as read
        :param request_timeout: Request timeout
        """
        return await self(
            ReadChatList(
                chat_list=chat_list,
            ),
            request_timeout=request_timeout,
        )

    async def get_current_weather(
        self,
        location: Location,
        request_timeout: float = 10.0,
    ) -> CurrentWeather:
        """
        Returns the current weather in the given location
        :param location: The location
        :param request_timeout: Request timeout
        """
        return await self(
            GetCurrentWeather(
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def get_story(
        self,
        story_sender_chat_id: int,
        story_id: int,
        only_local: bool,
        request_timeout: float = 10.0,
    ) -> Story:
        """
        Returns a story
        :param story_sender_chat_id: Identifier of the chat that posted the story
        :param story_id: Story identifier
        :param only_local: Pass true to get only locally available information without sending network requests
        :param request_timeout: Request timeout
        """
        return await self(
            GetStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                only_local=only_local,
            ),
            request_timeout=request_timeout,
        )

    async def get_chats_to_send_stories(
        self,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns supergroup and channel chats in which the current user has the right to post stories. The chats must be rechecked with canSendStory before actually trying to post a story there
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatsToSendStories(),
            request_timeout=request_timeout,
        )

    async def can_send_story(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> CanSendStoryResult:
        """
        Checks whether the current user can send a story on behalf of a chat; requires can_post_stories right for supergroup and channel chats
        :param chat_id: Chat identifier. Pass Saved Messages chat identifier when posting a story on behalf of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            CanSendStory(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def send_story(
        self,
        chat_id: int,
        content: InputStoryContent,
        privacy_settings: StoryPrivacySettings,
        active_period: int,
        is_posted_to_chat_page: bool,
        protect_content: bool,
        areas: InputStoryAreas | None = None,
        caption: FormattedText | None = None,
        from_story_full_id: StoryFullId | None = None,
        request_timeout: float = 10.0,
    ) -> Story:
        """
        Sends a new story to a chat; requires can_post_stories right for supergroup and channel chats. Returns a temporary story
        :param chat_id: Identifier of the chat that will post the story. Pass Saved Messages chat identifier when posting a story on behalf of the current user
        :param content: Content of the story
        :param privacy_settings: The privacy settings for the story; ignored for stories sent to supergroup and channel chats
        :param active_period: Period after which the story is moved to archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400 for Telegram Premium users, and 86400 otherwise
        :param is_posted_to_chat_page: Pass true to keep the story accessible after expiration
        :param protect_content: Pass true if the content of the story must be protected from forwarding and screenshotting
        :param areas: Clickable rectangle areas to be shown on the story media; pass null if none
        :param caption: Story caption; pass null to use an empty caption; 0-getOption('story_caption_length_max') characters; can have entities only if getOption('can_use_text_entities_in_story_caption')
        :param from_story_full_id: Full identifier of the original story, which content was used to create the story; pass null if the story isn't repost of another story
        :param request_timeout: Request timeout
        """
        return await self(
            SendStory(
                chat_id=chat_id,
                content=content,
                privacy_settings=privacy_settings,
                active_period=active_period,
                is_posted_to_chat_page=is_posted_to_chat_page,
                protect_content=protect_content,
                areas=areas,
                caption=caption,
                from_story_full_id=from_story_full_id,
            ),
            request_timeout=request_timeout,
        )

    async def edit_story(
        self,
        story_sender_chat_id: int,
        story_id: int,
        content: InputStoryContent | None = None,
        areas: InputStoryAreas | None = None,
        caption: FormattedText | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes content and caption of a story. Can be called only if story.can_be_edited == true
        :param story_sender_chat_id: Identifier of the chat that posted the story
        :param story_id: Identifier of the story to edit
        :param content: New content of the story; pass null to keep the current content
        :param areas: New clickable rectangle areas to be shown on the story media; pass null to keep the current areas. Areas can't be edited if story content isn't changed
        :param caption: New story caption; pass null to keep the current caption
        :param request_timeout: Request timeout
        """
        return await self(
            EditStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                content=content,
                areas=areas,
                caption=caption,
            ),
            request_timeout=request_timeout,
        )

    async def edit_story_cover(
        self,
        story_sender_chat_id: int,
        story_id: int,
        cover_frame_timestamp: float,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes cover of a video story. Can be called only if story.can_be_edited == true and the story isn't being edited now
        :param story_sender_chat_id: Identifier of the chat that posted the story
        :param story_id: Identifier of the story to edit
        :param cover_frame_timestamp: New timestamp of the frame, which will be used as video thumbnail
        :param request_timeout: Request timeout
        """
        return await self(
            EditStoryCover(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                cover_frame_timestamp=cover_frame_timestamp,
            ),
            request_timeout=request_timeout,
        )

    async def set_story_privacy_settings(
        self,
        story_id: int,
        privacy_settings: StoryPrivacySettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes privacy settings of a story. The method can be called only for stories posted on behalf of the current user and if story.can_be_edited == true
        :param story_id: Identifier of the story
        :param privacy_settings: The new privacy settigs for the story
        :param request_timeout: Request timeout
        """
        return await self(
            SetStoryPrivacySettings(
                story_id=story_id,
                privacy_settings=privacy_settings,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_story_is_posted_to_chat_page(
        self,
        story_sender_chat_id: int,
        story_id: int,
        is_posted_to_chat_page: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether a story is accessible after expiration. Can be called only if story.can_toggle_is_posted_to_chat_page == true
        :param story_sender_chat_id: Identifier of the chat that posted the story
        :param story_id: Identifier of the story
        :param is_posted_to_chat_page: Pass true to make the story accessible after expiration; pass false to make it private
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleStoryIsPostedToChatPage(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                is_posted_to_chat_page=is_posted_to_chat_page,
            ),
            request_timeout=request_timeout,
        )

    async def delete_story(
        self,
        story_sender_chat_id: int,
        story_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes a previously sent story. Can be called only if story.can_be_deleted == true
        :param story_sender_chat_id: Identifier of the chat that posted the story
        :param story_id: Identifier of the story to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_story_notification_settings_exceptions(
        self,
        request_timeout: float = 10.0,
    ) -> Chats:
        """
        Returns the list of chats with non-default notification settings for stories
        :param request_timeout: Request timeout
        """
        return await self(
            GetStoryNotificationSettingsExceptions(),
            request_timeout=request_timeout,
        )

    async def load_active_stories(
        self,
        story_list: StoryList,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Loads more active stories from a story list. The loaded stories will be sent through updates. Active stories are sorted by
        :param story_list: The story list in which to load active stories
        :param request_timeout: Request timeout
        """
        return await self(
            LoadActiveStories(
                story_list=story_list,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_active_stories_list(
        self,
        chat_id: int,
        story_list: StoryList,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes story list in which stories from the chat are shown
        :param chat_id: Identifier of the chat that posted stories
        :param story_list: New list for active stories posted by the chat
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatActiveStoriesList(
                chat_id=chat_id,
                story_list=story_list,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_active_stories(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatActiveStories:
        """
        Returns the list of active stories posted by the given chat
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatActiveStories(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_posted_to_chat_page_stories(
        self,
        chat_id: int,
        from_story_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Stories:
        """
        Returns the list of stories that posted by the given chat to its chat page. If from_story_id == 0, then pinned stories are returned first.
        :param chat_id: Chat identifier
        :param from_story_id: Identifier of the story starting from which stories must be returned; use 0 to get results from pinned and the newest story
        :param limit: The maximum number of stories to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatPostedToChatPageStories(
                chat_id=chat_id,
                from_story_id=from_story_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_archived_stories(
        self,
        chat_id: int,
        from_story_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Stories:
        """
        Returns the list of all stories posted by the given chat; requires can_edit_stories right in the chat.
        :param chat_id: Chat identifier
        :param from_story_id: Identifier of the story starting from which stories must be returned; use 0 to get results from the last story
        :param limit: The maximum number of stories to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatArchivedStories(
                chat_id=chat_id,
                from_story_id=from_story_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def set_chat_pinned_stories(
        self,
        chat_id: int,
        story_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the list of pinned stories on a chat page; requires can_edit_stories right in the chat
        :param chat_id: Identifier of the chat that posted the stories
        :param story_ids: New list of pinned stories. All stories must be posted to the chat page first. There can be up to getOption('pinned_story_count_max') pinned stories on a chat page
        :param request_timeout: Request timeout
        """
        return await self(
            SetChatPinnedStories(
                chat_id=chat_id,
                story_ids=story_ids,
            ),
            request_timeout=request_timeout,
        )

    async def open_story(
        self,
        story_sender_chat_id: int,
        story_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that a story is opened and is being viewed by the user
        :param story_sender_chat_id: The identifier of the sender of the opened story
        :param story_id: The identifier of the story
        :param request_timeout: Request timeout
        """
        return await self(
            OpenStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
            ),
            request_timeout=request_timeout,
        )

    async def close_story(
        self,
        story_sender_chat_id: int,
        story_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that a story is closed by the user
        :param story_sender_chat_id: The identifier of the sender of the story to close
        :param story_id: The identifier of the story
        :param request_timeout: Request timeout
        """
        return await self(
            CloseStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_story_available_reactions(
        self,
        row_size: int,
        request_timeout: float = 10.0,
    ) -> AvailableReactions:
        """
        Returns reactions, which can be chosen for a story
        :param row_size: Number of reaction per row, 5-25
        :param request_timeout: Request timeout
        """
        return await self(
            GetStoryAvailableReactions(
                row_size=row_size,
            ),
            request_timeout=request_timeout,
        )

    async def set_story_reaction(
        self,
        story_sender_chat_id: int,
        story_id: int,
        update_recent_reactions: bool,
        reaction_type: ReactionType | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes chosen reaction on a story that has already been sent
        :param story_sender_chat_id: The identifier of the sender of the story
        :param story_id: The identifier of the story
        :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions
        :param reaction_type: Type of the reaction to set; pass null to remove the reaction. Custom emoji reactions can be used only by Telegram Premium users. Paid reactions can't be set
        :param request_timeout: Request timeout
        """
        return await self(
            SetStoryReaction(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                update_recent_reactions=update_recent_reactions,
                reaction_type=reaction_type,
            ),
            request_timeout=request_timeout,
        )

    async def get_story_interactions(
        self,
        story_id: int,
        only_contacts: bool,
        prefer_forwards: bool,
        prefer_with_reaction: bool,
        offset: str,
        limit: int,
        query: str | None = None,
        request_timeout: float = 10.0,
    ) -> StoryInteractions:
        """
        Returns interactions with a story. The method can be called only for stories posted on behalf of the current user
        :param story_id: Story identifier
        :param only_contacts: Pass true to get only interactions by contacts; pass false to get all relevant interactions
        :param prefer_forwards: Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date
        :param prefer_with_reaction: Pass true to get interactions with reaction first; pass false to get interactions sorted just by interaction date. Ignored if prefer_forwards == true
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of story interactions to return
        :param query: Query to search for in names, usernames and titles; may be empty to get all relevant interactions
        :param request_timeout: Request timeout
        """
        return await self(
            GetStoryInteractions(
                story_id=story_id,
                only_contacts=only_contacts,
                prefer_forwards=prefer_forwards,
                prefer_with_reaction=prefer_with_reaction,
                offset=offset,
                limit=limit,
                query=query,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_story_interactions(
        self,
        story_sender_chat_id: int,
        story_id: int,
        prefer_forwards: bool,
        offset: str,
        limit: int,
        reaction_type: ReactionType | None = None,
        request_timeout: float = 10.0,
    ) -> StoryInteractions:
        """
        Returns interactions with a story posted in a chat. Can be used only if story is posted on behalf of a chat and the user is an administrator in the chat
        :param story_sender_chat_id: The identifier of the sender of the story
        :param story_id: Story identifier
        :param prefer_forwards: Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of story interactions to return
        :param reaction_type: Pass the default heart reaction or a suggested reaction type to receive only interactions with the specified reaction type; pass null to receive all interactions; reactionTypePaid isn't supported
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatStoryInteractions(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                prefer_forwards=prefer_forwards,
                offset=offset,
                limit=limit,
                reaction_type=reaction_type,
            ),
            request_timeout=request_timeout,
        )

    async def report_story(
        self,
        story_sender_chat_id: int,
        story_id: int,
        reason: ReportReason,
        text: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports a story to the Telegram moderators
        :param story_sender_chat_id: The identifier of the sender of the story to report
        :param story_id: The identifier of the story to report
        :param reason: The reason for reporting the story
        :param text: Additional report details; 0-1024 characters
        :param request_timeout: Request timeout
        """
        return await self(
            ReportStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                reason=reason,
                text=text,
            ),
            request_timeout=request_timeout,
        )

    async def activate_story_stealth_mode(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Activates stealth mode for stories, which hides all views of stories from the current user in the last 'story_stealth_mode_past_period' seconds
        :param request_timeout: Request timeout
        """
        return await self(
            ActivateStoryStealthMode(),
            request_timeout=request_timeout,
        )

    async def get_story_public_forwards(
        self,
        story_sender_chat_id: int,
        story_id: int,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> PublicForwards:
        """
        Returns forwards of a story as a message to public chats and reposts by public channels. Can be used only if the story is posted on behalf of the current user or story.can_get_statistics == true.
        :param story_sender_chat_id: The identifier of the sender of the story
        :param story_id: The identifier of the story
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of messages and stories to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            GetStoryPublicForwards(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_boost_level_features(
        self,
        is_channel: bool,
        level: int,
        request_timeout: float = 10.0,
    ) -> ChatBoostLevelFeatures:
        """
        Returns the list of features available on the specific chat boost level; this is an offline request
        :param is_channel: Pass true to get the list of features for channels; pass false to get the list of features for supergroups
        :param level: Chat boost level
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatBoostLevelFeatures(
                is_channel=is_channel,
                level=level,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_boost_features(
        self,
        is_channel: bool,
        request_timeout: float = 10.0,
    ) -> ChatBoostFeatures:
        """
        Returns the list of features available for different chat boost levels; this is an offline request
        :param is_channel: Pass true to get the list of features for channels; pass false to get the list of features for supergroups
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatBoostFeatures(
                is_channel=is_channel,
            ),
            request_timeout=request_timeout,
        )

    async def get_available_chat_boost_slots(
        self,
        request_timeout: float = 10.0,
    ) -> ChatBoostSlots:
        """
        Returns the list of available chat boost slots for the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetAvailableChatBoostSlots(),
            request_timeout=request_timeout,
        )

    async def get_chat_boost_status(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatBoostStatus:
        """
        Returns the current boost status for a supergroup or a channel chat
        :param chat_id: Identifier of the chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatBoostStatus(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def boost_chat(
        self,
        chat_id: int,
        slot_ids: list[int],
        request_timeout: float = 10.0,
    ) -> ChatBoostSlots:
        """
        Boosts a chat and returns the list of available chat boost slots for the current user after the boost
        :param chat_id: Identifier of the chat
        :param slot_ids: Identifiers of boost slots of the current user from which to apply boosts to the chat
        :param request_timeout: Request timeout
        """
        return await self(
            BoostChat(
                chat_id=chat_id,
                slot_ids=slot_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_boost_link(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatBoostLink:
        """
        Returns an HTTPS link to boost the specified supergroup or channel chat
        :param chat_id: Identifier of the chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatBoostLink(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_boost_link_info(
        self,
        url: str,
        request_timeout: float = 10.0,
    ) -> ChatBoostLinkInfo:
        """
        Returns information about a link to boost a chat. Can be called for any internal link of the type internalLinkTypeChatBoost
        :param url: The link to boost a chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatBoostLinkInfo(
                url=url,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_boosts(
        self,
        chat_id: int,
        only_gift_codes: bool,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> FoundChatBoosts:
        """
        Returns the list of boosts applied to a chat; requires administrator rights in the chat
        :param chat_id: Identifier of the chat
        :param only_gift_codes: Pass true to receive only boosts received from gift codes and giveaways created by the chat
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of boosts to be returned; up to 100. For optimal performance, the number of returned boosts can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatBoosts(
                chat_id=chat_id,
                only_gift_codes=only_gift_codes,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_user_chat_boosts(
        self,
        chat_id: int,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> FoundChatBoosts:
        """
        Returns the list of boosts applied to a chat by a given user; requires administrator rights in the chat; for bots only
        :param chat_id: Identifier of the chat
        :param user_id: Identifier of the user
        :param request_timeout: Request timeout
        """
        return await self(
            GetUserChatBoosts(
                chat_id=chat_id,
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_attachment_menu_bot(
        self,
        bot_user_id: int,
        request_timeout: float = 10.0,
    ) -> AttachmentMenuBot:
        """
        Returns information about a bot that can be added to attachment or side menu
        :param bot_user_id: Bot's user identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetAttachmentMenuBot(
                bot_user_id=bot_user_id,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_bot_is_added_to_attachment_menu(
        self,
        bot_user_id: int,
        is_added: bool,
        allow_write_access: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds or removes a bot to attachment and side menu. Bot can be added to the menu, only if userTypeBot.can_be_added_to_attachment_menu == true
        :param bot_user_id: Bot's user identifier
        :param is_added: Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu
        :param allow_write_access: Pass true if the current user allowed the bot to send them messages. Ignored if is_added is false
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleBotIsAddedToAttachmentMenu(
                bot_user_id=bot_user_id,
                is_added=is_added,
                allow_write_access=allow_write_access,
            ),
            request_timeout=request_timeout,
        )

    async def get_themed_emoji_statuses(
        self,
        request_timeout: float = 10.0,
    ) -> EmojiStatuses:
        """
        Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list for self status
        :param request_timeout: Request timeout
        """
        return await self(
            GetThemedEmojiStatuses(),
            request_timeout=request_timeout,
        )

    async def get_recent_emoji_statuses(
        self,
        request_timeout: float = 10.0,
    ) -> EmojiStatuses:
        """
        Returns recent emoji statuses for self status
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecentEmojiStatuses(),
            request_timeout=request_timeout,
        )

    async def get_default_emoji_statuses(
        self,
        request_timeout: float = 10.0,
    ) -> EmojiStatuses:
        """
        Returns default emoji statuses for self status
        :param request_timeout: Request timeout
        """
        return await self(
            GetDefaultEmojiStatuses(),
            request_timeout=request_timeout,
        )

    async def clear_recent_emoji_statuses(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears the list of recently used emoji statuses for self status
        :param request_timeout: Request timeout
        """
        return await self(
            ClearRecentEmojiStatuses(),
            request_timeout=request_timeout,
        )

    async def get_themed_chat_emoji_statuses(
        self,
        request_timeout: float = 10.0,
    ) -> EmojiStatuses:
        """
        Returns up to 8 emoji statuses, which must be shown in the emoji status list for chats
        :param request_timeout: Request timeout
        """
        return await self(
            GetThemedChatEmojiStatuses(),
            request_timeout=request_timeout,
        )

    async def get_default_chat_emoji_statuses(
        self,
        request_timeout: float = 10.0,
    ) -> EmojiStatuses:
        """
        Returns default emoji statuses for chats
        :param request_timeout: Request timeout
        """
        return await self(
            GetDefaultChatEmojiStatuses(),
            request_timeout=request_timeout,
        )

    async def get_disallowed_chat_emoji_statuses(
        self,
        request_timeout: float = 10.0,
    ) -> EmojiStatuses:
        """
        Returns the list of emoji statuses, which can't be used as chat emoji status, even they are from a sticker set with is_allowed_as_chat_emoji_status == true
        :param request_timeout: Request timeout
        """
        return await self(
            GetDisallowedChatEmojiStatuses(),
            request_timeout=request_timeout,
        )

    async def download_file(
        self,
        file_id: int,
        priority: int,
        offset: int,
        limit: int,
        synchronous: bool,
        request_timeout: float = 10.0,
    ) -> File:
        """
        Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates
        :param file_id: Identifier of the file to download
        :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
        :param offset: The starting position from which the file needs to be downloaded
        :param limit: Number of bytes which need to be downloaded starting from the 'offset' position before the download will automatically be canceled; use 0 to download without a limit
        :param synchronous: Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started
        :param request_timeout: Request timeout
        """
        return await self(
            DownloadFile(
                file_id=file_id,
                priority=priority,
                offset=offset,
                limit=limit,
                synchronous=synchronous,
            ),
            request_timeout=request_timeout,
        )

    async def get_file_downloaded_prefix_size(
        self,
        file_id: int,
        offset: int,
        request_timeout: float = 10.0,
    ) -> FileDownloadedPrefixSize:
        """
        Returns file downloaded prefix size from a given offset, in bytes
        :param file_id: Identifier of the file
        :param offset: Offset from which downloaded prefix size needs to be calculated
        :param request_timeout: Request timeout
        """
        return await self(
            GetFileDownloadedPrefixSize(
                file_id=file_id,
                offset=offset,
            ),
            request_timeout=request_timeout,
        )

    async def cancel_download_file(
        self,
        file_id: int,
        only_if_pending: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Stops the downloading of a file. If a file has already been downloaded, does nothing
        :param file_id: Identifier of a file to stop downloading
        :param only_if_pending: Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server
        :param request_timeout: Request timeout
        """
        return await self(
            CancelDownloadFile(
                file_id=file_id,
                only_if_pending=only_if_pending,
            ),
            request_timeout=request_timeout,
        )

    async def get_suggested_file_name(
        self,
        file_id: int,
        directory: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns suggested name for saving a file in a given directory
        :param file_id: Identifier of the file
        :param directory: Directory in which the file is supposed to be saved
        :param request_timeout: Request timeout
        """
        return await self(
            GetSuggestedFileName(
                file_id=file_id,
                directory=directory,
            ),
            request_timeout=request_timeout,
        )

    async def preliminary_upload_file(
        self,
        file: InputFile,
        priority: int,
        file_type: FileType | None = None,
        request_timeout: float = 10.0,
    ) -> File:
        """
        Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes.
        :param file: File to upload
        :param priority: Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first
        :param file_type: File type; pass null if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            PreliminaryUploadFile(
                file=file,
                priority=priority,
                file_type=file_type,
            ),
            request_timeout=request_timeout,
        )

    async def cancel_preliminary_upload_file(
        self,
        file_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile. For other files the behavior is undefined
        :param file_id: Identifier of the file to stop uploading
        :param request_timeout: Request timeout
        """
        return await self(
            CancelPreliminaryUploadFile(
                file_id=file_id,
            ),
            request_timeout=request_timeout,
        )

    async def write_generated_file_part(
        self,
        generation_id: int,
        offset: int,
        data: bytes,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file
        :param generation_id: The identifier of the generation process
        :param offset: The offset from which to write the data to the file
        :param data: The data to write
        :param request_timeout: Request timeout
        """
        return await self(
            WriteGeneratedFilePart(
                generation_id=generation_id,
                offset=offset,
                data=data,
            ),
            request_timeout=request_timeout,
        )

    async def set_file_generation_progress(
        self,
        generation_id: int,
        expected_size: int,
        local_prefix_size: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib on a file generation progress
        :param generation_id: The identifier of the generation process
        :param expected_size: Expected size of the generated file, in bytes; 0 if unknown
        :param local_prefix_size: The number of bytes already generated
        :param request_timeout: Request timeout
        """
        return await self(
            SetFileGenerationProgress(
                generation_id=generation_id,
                expected_size=expected_size,
                local_prefix_size=local_prefix_size,
            ),
            request_timeout=request_timeout,
        )

    async def finish_file_generation(
        self,
        generation_id: int,
        error: Error | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Finishes the file generation
        :param generation_id: The identifier of the generation process
        :param error: If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded
        :param request_timeout: Request timeout
        """
        return await self(
            FinishFileGeneration(
                generation_id=generation_id,
                error=error,
            ),
            request_timeout=request_timeout,
        )

    async def read_file_part(
        self,
        file_id: int,
        offset: int,
        count: int,
        request_timeout: float = 10.0,
    ) -> FilePart:
        """
        Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file
        :param file_id: Identifier of the file. The file must be located in the TDLib file cache
        :param offset: The offset from which to read the file
        :param count: Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position
        :param request_timeout: Request timeout
        """
        return await self(
            ReadFilePart(
                file_id=file_id,
                offset=offset,
                count=count,
            ),
            request_timeout=request_timeout,
        )

    async def delete_file(
        self,
        file_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes a file from the TDLib file cache
        :param file_id: Identifier of the file to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteFile(
                file_id=file_id,
            ),
            request_timeout=request_timeout,
        )

    async def add_file_to_downloads(
        self,
        file_id: int,
        chat_id: int,
        message_id: int,
        priority: int,
        request_timeout: float = 10.0,
    ) -> File:
        """
        Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates.
        :param file_id: Identifier of the file to download
        :param chat_id: Chat identifier of the message with the file
        :param message_id: Message identifier
        :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
        :param request_timeout: Request timeout
        """
        return await self(
            AddFileToDownloads(
                file_id=file_id,
                chat_id=chat_id,
                message_id=message_id,
                priority=priority,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_download_is_paused(
        self,
        file_id: int,
        is_paused: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes pause state of a file in the file download list
        :param file_id: Identifier of the downloaded file
        :param is_paused: Pass true if the download is paused
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleDownloadIsPaused(
                file_id=file_id,
                is_paused=is_paused,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_all_downloads_are_paused(
        self,
        are_paused: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes pause state of all files in the file download list
        :param are_paused: Pass true to pause all downloads; pass false to unpause them
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleAllDownloadsArePaused(
                are_paused=are_paused,
            ),
            request_timeout=request_timeout,
        )

    async def remove_file_from_downloads(
        self,
        file_id: int,
        delete_from_cache: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a file from the file download list
        :param file_id: Identifier of the downloaded file
        :param delete_from_cache: Pass true to delete the file from the TDLib file cache
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveFileFromDownloads(
                file_id=file_id,
                delete_from_cache=delete_from_cache,
            ),
            request_timeout=request_timeout,
        )

    async def remove_all_files_from_downloads(
        self,
        only_active: bool,
        only_completed: bool,
        delete_from_cache: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes all files from the file download list
        :param only_active: Pass true to remove only active downloads, including paused
        :param only_completed: Pass true to remove only completed downloads
        :param delete_from_cache: Pass true to delete the file from the TDLib file cache
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveAllFilesFromDownloads(
                only_active=only_active,
                only_completed=only_completed,
                delete_from_cache=delete_from_cache,
            ),
            request_timeout=request_timeout,
        )

    async def search_file_downloads(
        self,
        only_active: bool,
        only_completed: bool,
        offset: str,
        limit: int,
        query: str | None = None,
        request_timeout: float = 10.0,
    ) -> FoundFileDownloads:
        """
        Searches for files in the file download list or recently downloaded files from the list
        :param only_active: Pass true to search only for active downloads, including paused
        :param only_completed: Pass true to search only for completed downloads
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of files to be returned
        :param query: Query to search for; may be empty to return all downloaded files
        :param request_timeout: Request timeout
        """
        return await self(
            SearchFileDownloads(
                only_active=only_active,
                only_completed=only_completed,
                offset=offset,
                limit=limit,
                query=query,
            ),
            request_timeout=request_timeout,
        )

    async def set_application_verification_token(
        self,
        verification_id: int,
        token: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Application verification has been completed. Can be called before authorization
        :param verification_id: Unique identifier for the verification process as received from updateApplicationVerificationRequired
        :param token: Play Integrity API token for the Android application, or secret from push notification for the iOS application;
        :param request_timeout: Request timeout
        """
        return await self(
            SetApplicationVerificationToken(
                verification_id=verification_id,
                token=token,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_file_type(
        self,
        message_file_head: str,
        request_timeout: float = 10.0,
    ) -> MessageFileType:
        """
        Returns information about a file with messages exported from another application
        :param message_file_head: Beginning of the message file; up to 100 first lines
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageFileType(
                message_file_head=message_file_head,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_import_confirmation_text(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns a confirmation text to be shown to the user before starting message import
        :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info member right
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageImportConfirmationText(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def import_messages(
        self,
        chat_id: int,
        message_file: InputFile,
        attached_files: list[InputFile],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Imports messages exported from another app
        :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info member right
        :param message_file: File with messages to import. Only inputFileLocal and inputFileGenerated are supported. The file must not be previously uploaded
        :param attached_files: Files used in the imported messages. Only inputFileLocal and inputFileGenerated are supported. The files must not be previously uploaded
        :param request_timeout: Request timeout
        """
        return await self(
            ImportMessages(
                chat_id=chat_id,
                message_file=message_file,
                attached_files=attached_files,
            ),
            request_timeout=request_timeout,
        )

    async def replace_primary_chat_invite_link(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatInviteLink:
        """
        Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            ReplacePrimaryChatInviteLink(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def create_chat_invite_link(
        self,
        chat_id: int,
        name: str,
        expiration_date: int,
        member_limit: int,
        creates_join_request: bool,
        request_timeout: float = 10.0,
    ) -> ChatInviteLink:
        """
        Creates a new invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat
        :param chat_id: Chat identifier
        :param name: Invite link name; 0-32 characters
        :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
        :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
        :param creates_join_request: Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0
        :param request_timeout: Request timeout
        """
        return await self(
            CreateChatInviteLink(
                chat_id=chat_id,
                name=name,
                expiration_date=expiration_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
            request_timeout=request_timeout,
        )

    async def create_chat_subscription_invite_link(
        self,
        chat_id: int,
        name: str,
        subscription_pricing: StarSubscriptionPricing,
        request_timeout: float = 10.0,
    ) -> ChatInviteLink:
        """
        Creates a new subscription invite link for a channel chat. Requires can_invite_users right in the chat
        :param chat_id: Chat identifier
        :param name: Invite link name; 0-32 characters
        :param subscription_pricing: Information about subscription plan that will be applied to the users joining the chat via the link.
        :param request_timeout: Request timeout
        """
        return await self(
            CreateChatSubscriptionInviteLink(
                chat_id=chat_id,
                name=name,
                subscription_pricing=subscription_pricing,
            ),
            request_timeout=request_timeout,
        )

    async def edit_chat_invite_link(
        self,
        chat_id: int,
        invite_link: str,
        name: str,
        expiration_date: int,
        member_limit: int,
        creates_join_request: bool,
        request_timeout: float = 10.0,
    ) -> ChatInviteLink:
        """
        Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels.
        :param chat_id: Chat identifier
        :param invite_link: Invite link to be edited
        :param name: Invite link name; 0-32 characters
        :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
        :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
        :param creates_join_request: Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0
        :param request_timeout: Request timeout
        """
        return await self(
            EditChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
                name=name,
                expiration_date=expiration_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
            request_timeout=request_timeout,
        )

    async def edit_chat_subscription_invite_link(
        self,
        chat_id: int,
        invite_link: str,
        name: str,
        request_timeout: float = 10.0,
    ) -> ChatInviteLink:
        """
        Edits a subscription invite link for a channel chat. Requires can_invite_users right in the chat for own links and owner privileges for other links
        :param chat_id: Chat identifier
        :param invite_link: Invite link to be edited
        :param name: Invite link name; 0-32 characters
        :param request_timeout: Request timeout
        """
        return await self(
            EditChatSubscriptionInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link(
        self,
        chat_id: int,
        invite_link: str,
        request_timeout: float = 10.0,
    ) -> ChatInviteLink:
        """
        Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
        :param chat_id: Chat identifier
        :param invite_link: Invite link to get
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link_counts(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> ChatInviteLinkCounts:
        """
        Returns the list of chat administrators with number of their invite links. Requires owner privileges in the chat
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatInviteLinkCounts(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_invite_links(
        self,
        chat_id: int,
        creator_user_id: int,
        is_revoked: bool,
        offset_date: int,
        offset_invite_link: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> ChatInviteLinks:
        """
        Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
        :param chat_id: Chat identifier
        :param creator_user_id: User identifier of a chat administrator. Must be an identifier of the current user for non-owner
        :param is_revoked: Pass true if revoked links needs to be returned instead of active or expired
        :param offset_date: Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
        :param offset_invite_link: Invite link starting after which to return invite links; use empty string to get results from the beginning
        :param limit: The maximum number of invite links to return; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatInviteLinks(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
                is_revoked=is_revoked,
                offset_date=offset_date,
                offset_invite_link=offset_invite_link,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link_members(
        self,
        chat_id: int,
        invite_link: str,
        only_with_expired_subscription: bool,
        limit: int,
        offset_member: ChatInviteLinkMember | None = None,
        request_timeout: float = 10.0,
    ) -> ChatInviteLinkMembers:
        """
        Returns chat members joined a chat via an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :param chat_id: Chat identifier
        :param invite_link: Invite link for which to return chat members
        :param only_with_expired_subscription: Pass true if the link is a subscription link and only members with expired subscription must be returned
        :param limit: The maximum number of chat members to return; up to 100
        :param offset_member: A chat member from which to return next chat members; pass null to get results from the beginning
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatInviteLinkMembers(
                chat_id=chat_id,
                invite_link=invite_link,
                only_with_expired_subscription=only_with_expired_subscription,
                limit=limit,
                offset_member=offset_member,
            ),
            request_timeout=request_timeout,
        )

    async def revoke_chat_invite_link(
        self,
        chat_id: int,
        invite_link: str,
        request_timeout: float = 10.0,
    ) -> ChatInviteLinks:
        """
        Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links.
        :param chat_id: Chat identifier
        :param invite_link: Invite link to be revoked
        :param request_timeout: Request timeout
        """
        return await self(
            RevokeChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_timeout=request_timeout,
        )

    async def delete_revoked_chat_invite_link(
        self,
        chat_id: int,
        invite_link: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :param chat_id: Chat identifier
        :param invite_link: Invite link to revoke
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteRevokedChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_timeout=request_timeout,
        )

    async def delete_all_revoked_chat_invite_links(
        self,
        chat_id: int,
        creator_user_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :param chat_id: Chat identifier
        :param creator_user_id: User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteAllRevokedChatInviteLinks(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
            ),
            request_timeout=request_timeout,
        )

    async def check_chat_invite_link(
        self,
        invite_link: str,
        request_timeout: float = 10.0,
    ) -> ChatInviteLinkInfo:
        """
        Checks the validity of an invite link for a chat and returns information about the corresponding chat
        :param invite_link: Invite link to be checked
        :param request_timeout: Request timeout
        """
        return await self(
            CheckChatInviteLink(
                invite_link=invite_link,
            ),
            request_timeout=request_timeout,
        )

    async def join_chat_by_invite_link(
        self,
        invite_link: str,
        request_timeout: float = 10.0,
    ) -> Chat:
        """
        Uses an invite link to add the current user to the chat if possible. May return an error with a message 'INVITE_REQUEST_SENT' if only a join request was created
        :param invite_link: Invite link to use
        :param request_timeout: Request timeout
        """
        return await self(
            JoinChatByInviteLink(
                invite_link=invite_link,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_join_requests(
        self,
        chat_id: int,
        invite_link: str,
        query: str,
        limit: int,
        offset_request: ChatJoinRequest | None = None,
        request_timeout: float = 10.0,
    ) -> ChatJoinRequests:
        """
        Returns pending join requests in a chat
        :param chat_id: Chat identifier
        :param invite_link: Invite link for which to return join requests. If empty, all join requests will be returned. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :param query: A query to search for in the first names, last names and usernames of the users to return
        :param limit: The maximum number of requests to join the chat to return
        :param offset_request: A chat join request from which to return next requests; pass null to get results from the beginning
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatJoinRequests(
                chat_id=chat_id,
                invite_link=invite_link,
                query=query,
                limit=limit,
                offset_request=offset_request,
            ),
            request_timeout=request_timeout,
        )

    async def process_chat_join_request(
        self,
        chat_id: int,
        user_id: int,
        approve: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Handles a pending join request in a chat
        :param chat_id: Chat identifier
        :param user_id: Identifier of the user that sent the request
        :param approve: Pass true to approve the request; pass false to decline it
        :param request_timeout: Request timeout
        """
        return await self(
            ProcessChatJoinRequest(
                chat_id=chat_id,
                user_id=user_id,
                approve=approve,
            ),
            request_timeout=request_timeout,
        )

    async def process_chat_join_requests(
        self,
        chat_id: int,
        invite_link: str,
        approve: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Handles all pending join requests for a given link in a chat
        :param chat_id: Chat identifier
        :param invite_link: Invite link for which to process join requests. If empty, all join requests will be processed. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :param approve: Pass true to approve all requests; pass false to decline them
        :param request_timeout: Request timeout
        """
        return await self(
            ProcessChatJoinRequests(
                chat_id=chat_id,
                invite_link=invite_link,
                approve=approve,
            ),
            request_timeout=request_timeout,
        )

    async def create_call(
        self,
        user_id: int,
        protocol: CallProtocol,
        is_video: bool,
        request_timeout: float = 10.0,
    ) -> CallId:
        """
        Creates a new call
        :param user_id: Identifier of the user to be called
        :param protocol: The call protocols supported by the application
        :param is_video: Pass true to create a video call
        :param request_timeout: Request timeout
        """
        return await self(
            CreateCall(
                user_id=user_id,
                protocol=protocol,
                is_video=is_video,
            ),
            request_timeout=request_timeout,
        )

    async def accept_call(
        self,
        call_id: int,
        protocol: CallProtocol,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Accepts an incoming call
        :param call_id: Call identifier
        :param protocol: The call protocols supported by the application
        :param request_timeout: Request timeout
        """
        return await self(
            AcceptCall(
                call_id=call_id,
                protocol=protocol,
            ),
            request_timeout=request_timeout,
        )

    async def send_call_signaling_data(
        self,
        call_id: int,
        data: bytes,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends call signaling data
        :param call_id: Call identifier
        :param data: The data
        :param request_timeout: Request timeout
        """
        return await self(
            SendCallSignalingData(
                call_id=call_id,
                data=data,
            ),
            request_timeout=request_timeout,
        )

    async def discard_call(
        self,
        call_id: int,
        is_disconnected: bool,
        duration: int,
        is_video: bool,
        connection_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Discards a call
        :param call_id: Call identifier
        :param is_disconnected: Pass true if the user was disconnected
        :param duration: The call duration, in seconds
        :param is_video: Pass true if the call was a video call
        :param connection_id: Identifier of the connection used during the call
        :param request_timeout: Request timeout
        """
        return await self(
            DiscardCall(
                call_id=call_id,
                is_disconnected=is_disconnected,
                duration=duration,
                is_video=is_video,
                connection_id=connection_id,
            ),
            request_timeout=request_timeout,
        )

    async def send_call_rating(
        self,
        call_id: int,
        rating: int,
        comment: str,
        problems: list[CallProblem],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends a call rating
        :param call_id: Call identifier
        :param rating: Call rating; 1-5
        :param comment: An optional user comment if the rating is less than 5
        :param problems: List of the exact types of problems with the call, specified by the user
        :param request_timeout: Request timeout
        """
        return await self(
            SendCallRating(
                call_id=call_id,
                rating=rating,
                comment=comment,
                problems=problems,
            ),
            request_timeout=request_timeout,
        )

    async def send_call_debug_information(
        self,
        call_id: int,
        debug_information: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends debug information for a call to Telegram servers
        :param call_id: Call identifier
        :param debug_information: Debug information in application-specific format
        :param request_timeout: Request timeout
        """
        return await self(
            SendCallDebugInformation(
                call_id=call_id,
                debug_information=debug_information,
            ),
            request_timeout=request_timeout,
        )

    async def send_call_log(
        self,
        call_id: int,
        log_file: InputFile,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends log file for a call to Telegram servers
        :param call_id: Call identifier
        :param log_file: Call log file. Only inputFileLocal and inputFileGenerated are supported
        :param request_timeout: Request timeout
        """
        return await self(
            SendCallLog(
                call_id=call_id,
                log_file=log_file,
            ),
            request_timeout=request_timeout,
        )

    async def get_video_chat_available_participants(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> MessageSenders:
        """
        Returns the list of participant identifiers, on whose behalf a video chat in the chat can be joined
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetVideoChatAvailableParticipants(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_video_chat_default_participant(
        self,
        chat_id: int,
        default_participant_id: MessageSender,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes default participant identifier, on whose behalf a video chat in the chat will be joined
        :param chat_id: Chat identifier
        :param default_participant_id: Default group call participant identifier to join the video chats
        :param request_timeout: Request timeout
        """
        return await self(
            SetVideoChatDefaultParticipant(
                chat_id=chat_id,
                default_participant_id=default_participant_id,
            ),
            request_timeout=request_timeout,
        )

    async def create_video_chat(
        self,
        chat_id: int,
        title: str,
        start_date: int,
        is_rtmp_stream: bool,
        request_timeout: float = 10.0,
    ) -> GroupCallId:
        """
        Creates a video chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_video_chats administrator right
        :param chat_id: Identifier of a chat in which the video chat will be created
        :param title: Group call title; if empty, chat title will be used
        :param start_date: Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 to start the video chat immediately. The date must be at least 10 seconds and at most 8 days in the future
        :param is_rtmp_stream: Pass true to create an RTMP stream instead of an ordinary video chat; requires owner privileges
        :param request_timeout: Request timeout
        """
        return await self(
            CreateVideoChat(
                chat_id=chat_id,
                title=title,
                start_date=start_date,
                is_rtmp_stream=is_rtmp_stream,
            ),
            request_timeout=request_timeout,
        )

    async def get_video_chat_rtmp_url(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> RtmpUrl:
        """
        Returns RTMP URL for streaming to the chat; requires owner privileges
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetVideoChatRtmpUrl(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def replace_video_chat_rtmp_url(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> RtmpUrl:
        """
        Replaces the current RTMP URL for streaming to the chat; requires owner privileges
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            ReplaceVideoChatRtmpUrl(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_group_call(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> GroupCall:
        """
        Returns information about a group call
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetGroupCall(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def start_scheduled_group_call(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Starts a scheduled group call
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            StartScheduledGroupCall(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_group_call_enabled_start_notification(
        self,
        group_call_id: int,
        enabled_start_notification: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether the current user will receive a notification when the group call starts; scheduled group calls only
        :param group_call_id: Group call identifier
        :param enabled_start_notification: New value of the enabled_start_notification setting
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGroupCallEnabledStartNotification(
                group_call_id=group_call_id,
                enabled_start_notification=enabled_start_notification,
            ),
            request_timeout=request_timeout,
        )

    async def join_group_call(
        self,
        group_call_id: int,
        audio_source_id: int,
        payload: str,
        is_muted: bool,
        is_my_video_enabled: bool,
        participant_id: MessageSender | None = None,
        invite_hash: str | None = None,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Joins an active group call. Returns join response payload for tgcalls
        :param group_call_id: Group call identifier
        :param audio_source_id: Caller audio channel synchronization source identifier; received from tgcalls
        :param payload: Group call join payload; received from tgcalls
        :param is_muted: Pass true to join the call with muted microphone
        :param is_my_video_enabled: Pass true if the user's video is enabled
        :param participant_id: Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only
        :param invite_hash: If non-empty, invite hash to be used to join the group call without being muted by administrators
        :param request_timeout: Request timeout
        """
        return await self(
            JoinGroupCall(
                group_call_id=group_call_id,
                audio_source_id=audio_source_id,
                payload=payload,
                is_muted=is_muted,
                is_my_video_enabled=is_my_video_enabled,
                participant_id=participant_id,
                invite_hash=invite_hash,
            ),
            request_timeout=request_timeout,
        )

    async def start_group_call_screen_sharing(
        self,
        group_call_id: int,
        audio_source_id: int,
        payload: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Starts screen sharing in a joined group call. Returns join response payload for tgcalls
        :param group_call_id: Group call identifier
        :param audio_source_id: Screen sharing audio channel synchronization source identifier; received from tgcalls
        :param payload: Group call join payload; received from tgcalls
        :param request_timeout: Request timeout
        """
        return await self(
            StartGroupCallScreenSharing(
                group_call_id=group_call_id,
                audio_source_id=audio_source_id,
                payload=payload,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_group_call_screen_sharing_is_paused(
        self,
        group_call_id: int,
        is_paused: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Pauses or unpauses screen sharing in a joined group call
        :param group_call_id: Group call identifier
        :param is_paused: Pass true to pause screen sharing; pass false to unpause it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGroupCallScreenSharingIsPaused(
                group_call_id=group_call_id,
                is_paused=is_paused,
            ),
            request_timeout=request_timeout,
        )

    async def end_group_call_screen_sharing(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Ends screen sharing in a joined group call
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            EndGroupCallScreenSharing(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_group_call_title(
        self,
        group_call_id: int,
        title: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets group call title. Requires groupCall.can_be_managed group call flag
        :param group_call_id: Group call identifier
        :param title: New group call title; 1-64 characters
        :param request_timeout: Request timeout
        """
        return await self(
            SetGroupCallTitle(
                group_call_id=group_call_id,
                title=title,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_group_call_mute_new_participants(
        self,
        group_call_id: int,
        mute_new_participants: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_toggle_mute_new_participants group call flag
        :param group_call_id: Group call identifier
        :param mute_new_participants: New value of the mute_new_participants setting
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGroupCallMuteNewParticipants(
                group_call_id=group_call_id,
                mute_new_participants=mute_new_participants,
            ),
            request_timeout=request_timeout,
        )

    async def invite_group_call_participants(
        self,
        group_call_id: int,
        user_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Invites users to an active group call. Sends a service message of type messageInviteVideoChatParticipants for video chats
        :param group_call_id: Group call identifier
        :param user_ids: User identifiers. At most 10 users can be invited simultaneously
        :param request_timeout: Request timeout
        """
        return await self(
            InviteGroupCallParticipants(
                group_call_id=group_call_id,
                user_ids=user_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_group_call_invite_link(
        self,
        group_call_id: int,
        can_self_unmute: bool,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns invite link to a video chat in a public chat
        :param group_call_id: Group call identifier
        :param can_self_unmute: Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag
        :param request_timeout: Request timeout
        """
        return await self(
            GetGroupCallInviteLink(
                group_call_id=group_call_id,
                can_self_unmute=can_self_unmute,
            ),
            request_timeout=request_timeout,
        )

    async def revoke_group_call_invite_link(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            RevokeGroupCallInviteLink(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def start_group_call_recording(
        self,
        group_call_id: int,
        title: str,
        record_video: bool,
        use_portrait_orientation: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Starts recording of an active group call. Requires groupCall.can_be_managed group call flag
        :param group_call_id: Group call identifier
        :param title: Group call recording title; 0-64 characters
        :param record_video: Pass true to record a video file instead of an audio file
        :param use_portrait_orientation: Pass true to use portrait orientation for video instead of landscape one
        :param request_timeout: Request timeout
        """
        return await self(
            StartGroupCallRecording(
                group_call_id=group_call_id,
                title=title,
                record_video=record_video,
                use_portrait_orientation=use_portrait_orientation,
            ),
            request_timeout=request_timeout,
        )

    async def end_group_call_recording(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Ends recording of an active group call. Requires groupCall.can_be_managed group call flag
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            EndGroupCallRecording(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_group_call_is_my_video_paused(
        self,
        group_call_id: int,
        is_my_video_paused: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether current user's video is paused
        :param group_call_id: Group call identifier
        :param is_my_video_paused: Pass true if the current user's video is paused
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGroupCallIsMyVideoPaused(
                group_call_id=group_call_id,
                is_my_video_paused=is_my_video_paused,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_group_call_is_my_video_enabled(
        self,
        group_call_id: int,
        is_my_video_enabled: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether current user's video is enabled
        :param group_call_id: Group call identifier
        :param is_my_video_enabled: Pass true if the current user's video is enabled
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGroupCallIsMyVideoEnabled(
                group_call_id=group_call_id,
                is_my_video_enabled=is_my_video_enabled,
            ),
            request_timeout=request_timeout,
        )

    async def set_group_call_participant_is_speaking(
        self,
        group_call_id: int,
        audio_source: int,
        is_speaking: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that speaking state of a participant of an active group has changed
        :param group_call_id: Group call identifier
        :param audio_source: Group call participant's synchronization audio source identifier, or 0 for the current user
        :param is_speaking: Pass true if the user is speaking
        :param request_timeout: Request timeout
        """
        return await self(
            SetGroupCallParticipantIsSpeaking(
                group_call_id=group_call_id,
                audio_source=audio_source,
                is_speaking=is_speaking,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_group_call_participant_is_muted(
        self,
        group_call_id: int,
        participant_id: MessageSender,
        is_muted: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves
        :param group_call_id: Group call identifier
        :param participant_id: Participant identifier
        :param is_muted: Pass true to mute the user; pass false to unmute them
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGroupCallParticipantIsMuted(
                group_call_id=group_call_id,
                participant_id=participant_id,
                is_muted=is_muted,
            ),
            request_timeout=request_timeout,
        )

    async def set_group_call_participant_volume_level(
        self,
        group_call_id: int,
        participant_id: MessageSender,
        volume_level: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level
        :param group_call_id: Group call identifier
        :param participant_id: Participant identifier
        :param volume_level: New participant's volume level; 1-20000 in hundreds of percents
        :param request_timeout: Request timeout
        """
        return await self(
            SetGroupCallParticipantVolumeLevel(
                group_call_id=group_call_id,
                participant_id=participant_id,
                volume_level=volume_level,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_group_call_participant_is_hand_raised(
        self,
        group_call_id: int,
        participant_id: MessageSender,
        is_hand_raised: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether a group call participant hand is rased
        :param group_call_id: Group call identifier
        :param participant_id: Participant identifier
        :param is_hand_raised: Pass true if the user's hand needs to be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleGroupCallParticipantIsHandRaised(
                group_call_id=group_call_id,
                participant_id=participant_id,
                is_hand_raised=is_hand_raised,
            ),
            request_timeout=request_timeout,
        )

    async def load_group_call_participants(
        self,
        group_call_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants have already been loaded
        :param group_call_id: Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined
        :param limit: The maximum number of participants to load; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            LoadGroupCallParticipants(
                group_call_id=group_call_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def leave_group_call(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Leaves a group call
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            LeaveGroupCall(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def end_group_call(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Ends a group call. Requires groupCall.can_be_managed
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            EndGroupCall(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_group_call_streams(
        self,
        group_call_id: int,
        request_timeout: float = 10.0,
    ) -> GroupCallStreams:
        """
        Returns information about available group call streams
        :param group_call_id: Group call identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetGroupCallStreams(
                group_call_id=group_call_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_group_call_stream_segment(
        self,
        group_call_id: int,
        time_offset: int,
        scale: int,
        channel_id: int,
        video_quality: GroupCallVideoQuality | None = None,
        request_timeout: float = 10.0,
    ) -> FilePart:
        """
        Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video
        :param group_call_id: Group call identifier
        :param time_offset: Point in time when the stream segment begins; Unix timestamp in milliseconds
        :param scale: Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
        :param channel_id: Identifier of an audio/video channel to get as received from tgcalls
        :param video_quality: Video quality as received from tgcalls; pass null to get the worst available quality
        :param request_timeout: Request timeout
        """
        return await self(
            GetGroupCallStreamSegment(
                group_call_id=group_call_id,
                time_offset=time_offset,
                scale=scale,
                channel_id=channel_id,
                video_quality=video_quality,
            ),
            request_timeout=request_timeout,
        )

    async def set_message_sender_block_list(
        self,
        sender_id: MessageSender,
        block_list: BlockList | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the block list of a message sender. Currently, only users and supergroup chats can be blocked
        :param sender_id: Identifier of a message sender to block/unblock
        :param block_list: New block list for the message sender; pass null to unblock the message sender
        :param request_timeout: Request timeout
        """
        return await self(
            SetMessageSenderBlockList(
                sender_id=sender_id,
                block_list=block_list,
            ),
            request_timeout=request_timeout,
        )

    async def block_message_sender_from_replies(
        self,
        message_id: int,
        delete_message: bool,
        delete_all_messages: bool,
        report_spam: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Blocks an original sender of a message in the Replies chat
        :param message_id: The identifier of an incoming message in the Replies chat
        :param delete_message: Pass true to delete the message
        :param delete_all_messages: Pass true to delete all messages from the same sender
        :param report_spam: Pass true to report the sender to the Telegram moderators
        :param request_timeout: Request timeout
        """
        return await self(
            BlockMessageSenderFromReplies(
                message_id=message_id,
                delete_message=delete_message,
                delete_all_messages=delete_all_messages,
                report_spam=report_spam,
            ),
            request_timeout=request_timeout,
        )

    async def get_blocked_message_senders(
        self,
        block_list: BlockList,
        offset: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> MessageSenders:
        """
        Returns users and chats that were blocked by the current user
        :param block_list: Block list from which to return users
        :param offset: Number of users and chats to skip in the result; must be non-negative
        :param limit: The maximum number of users and chats to return; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            GetBlockedMessageSenders(
                block_list=block_list,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def add_contact(
        self,
        contact: Contact,
        share_phone_number: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a user to the contact list or edits an existing contact by their user identifier
        :param contact: The contact to add or edit; phone number may be empty and needs to be specified only if known, vCard is ignored
        :param share_phone_number: Pass true to share the current user's phone number with the new contact. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed.
        :param request_timeout: Request timeout
        """
        return await self(
            AddContact(
                contact=contact,
                share_phone_number=share_phone_number,
            ),
            request_timeout=request_timeout,
        )

    async def import_contacts(
        self,
        contacts: list[Contact],
        request_timeout: float = 10.0,
    ) -> ImportedContacts:
        """
        Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored
        :param contacts: The list of contacts to import or edit; contacts' vCard are ignored and are not imported
        :param request_timeout: Request timeout
        """
        return await self(
            ImportContacts(
                contacts=contacts,
            ),
            request_timeout=request_timeout,
        )

    async def get_contacts(
        self,
        request_timeout: float = 10.0,
    ) -> Users:
        """
        Returns all contacts of the user
        :param request_timeout: Request timeout
        """
        return await self(
            GetContacts(),
            request_timeout=request_timeout,
        )

    async def search_contacts(
        self,
        limit: int,
        query: str | None = None,
        request_timeout: float = 10.0,
    ) -> Users:
        """
        Searches for the specified query in the first names, last names and usernames of the known user contacts
        :param limit: The maximum number of users to be returned
        :param query: Query to search for; may be empty to return all contacts
        :param request_timeout: Request timeout
        """
        return await self(
            SearchContacts(
                limit=limit,
                query=query,
            ),
            request_timeout=request_timeout,
        )

    async def remove_contacts(
        self,
        user_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes users from the contact list
        :param user_ids: Identifiers of users to be deleted
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveContacts(
                user_ids=user_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_imported_contact_count(
        self,
        request_timeout: float = 10.0,
    ) -> Count:
        """
        Returns the total number of imported contacts
        :param request_timeout: Request timeout
        """
        return await self(
            GetImportedContactCount(),
            request_timeout=request_timeout,
        )

    async def change_imported_contacts(
        self,
        contacts: list[Contact],
        request_timeout: float = 10.0,
    ) -> ImportedContacts:
        """
        Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts.
        :param contacts: The new list of contacts, contact's vCard are ignored and are not imported
        :param request_timeout: Request timeout
        """
        return await self(
            ChangeImportedContacts(
                contacts=contacts,
            ),
            request_timeout=request_timeout,
        )

    async def clear_imported_contacts(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears all imported contacts, contact list remains unchanged
        :param request_timeout: Request timeout
        """
        return await self(
            ClearImportedContacts(),
            request_timeout=request_timeout,
        )

    async def set_close_friends(
        self,
        user_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the list of close friends of the current user
        :param user_ids: User identifiers of close friends; the users must be contacts of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            SetCloseFriends(
                user_ids=user_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_close_friends(
        self,
        request_timeout: float = 10.0,
    ) -> Users:
        """
        Returns all close friends of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetCloseFriends(),
            request_timeout=request_timeout,
        )

    async def set_user_personal_profile_photo(
        self,
        user_id: int,
        photo: InputChatPhoto | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes a personal profile photo of a contact user
        :param user_id: User identifier
        :param photo: Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function
        :param request_timeout: Request timeout
        """
        return await self(
            SetUserPersonalProfilePhoto(
                user_id=user_id,
                photo=photo,
            ),
            request_timeout=request_timeout,
        )

    async def suggest_user_profile_photo(
        self,
        user_id: int,
        photo: InputChatPhoto,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Suggests a profile photo to another regular user with common messages
        :param user_id: User identifier
        :param photo: Profile photo to suggest; inputChatPhotoPrevious isn't supported in this function
        :param request_timeout: Request timeout
        """
        return await self(
            SuggestUserProfilePhoto(
                user_id=user_id,
                photo=photo,
            ),
            request_timeout=request_timeout,
        )

    async def search_user_by_phone_number(
        self,
        phone_number: str,
        only_local: bool,
        request_timeout: float = 10.0,
    ) -> User:
        """
        Searches a user by their phone number. Returns a 404 error if the user can't be found
        :param phone_number: Phone number to search for
        :param only_local: Pass true to get only locally available information without sending network requests
        :param request_timeout: Request timeout
        """
        return await self(
            SearchUserByPhoneNumber(
                phone_number=phone_number,
                only_local=only_local,
            ),
            request_timeout=request_timeout,
        )

    async def share_phone_number(
        self,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber
        :param user_id: Identifier of the user with whom to share the phone number. The user must be a mutual contact
        :param request_timeout: Request timeout
        """
        return await self(
            SharePhoneNumber(
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> ChatPhotos:
        """
        Returns the profile photos of a user. Personal and public photo aren't returned
        :param user_id: User identifier
        :param offset: The number of photos to skip; must be non-negative
        :param limit: The maximum number of photos to be returned; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            GetUserProfilePhotos(
                user_id=user_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_stickers(
        self,
        sticker_type: StickerType,
        query: str,
        limit: int,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns stickers from the installed sticker sets that correspond to any of the given emoji or can be found by sticker-specific keywords. If the query is non-empty, then favorite, recently used or trending stickers may also be returned
        :param sticker_type: Type of the stickers to return
        :param query: Search query; a space-separated list of emojis or a keyword prefix. If empty, returns all known installed stickers
        :param limit: The maximum number of stickers to be returned
        :param chat_id: Chat identifier for which to return stickers. Available custom emoji stickers may be different for different chats
        :param request_timeout: Request timeout
        """
        return await self(
            GetStickers(
                sticker_type=sticker_type,
                query=query,
                limit=limit,
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_all_sticker_emojis(
        self,
        sticker_type: StickerType,
        query: str,
        chat_id: int,
        return_only_main_emoji: bool,
        request_timeout: float = 10.0,
    ) -> Emojis:
        """
        Returns unique emoji that correspond to stickers to be found by the getStickers(sticker_type, query, 1000000, chat_id)
        :param sticker_type: Type of the stickers to search for
        :param query: Search query
        :param chat_id: Chat identifier for which to find stickers
        :param return_only_main_emoji: Pass true if only main emoji for each found sticker must be included in the result
        :param request_timeout: Request timeout
        """
        return await self(
            GetAllStickerEmojis(
                sticker_type=sticker_type,
                query=query,
                chat_id=chat_id,
                return_only_main_emoji=return_only_main_emoji,
            ),
            request_timeout=request_timeout,
        )

    async def search_stickers(
        self,
        sticker_type: StickerType,
        emojis: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Searches for stickers from public sticker sets that correspond to any of the given emoji
        :param sticker_type: Type of the stickers to return
        :param emojis: Space-separated list of emojis to search for; must be non-empty
        :param limit: The maximum number of stickers to be returned; 0-100
        :param request_timeout: Request timeout
        """
        return await self(
            SearchStickers(
                sticker_type=sticker_type,
                emojis=emojis,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_greeting_stickers(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns greeting stickers from regular sticker sets that can be used for the start page of other users
        :param request_timeout: Request timeout
        """
        return await self(
            GetGreetingStickers(),
            request_timeout=request_timeout,
        )

    async def get_premium_stickers(
        self,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns premium stickers from regular sticker sets
        :param limit: The maximum number of stickers to be returned; 0-100
        :param request_timeout: Request timeout
        """
        return await self(
            GetPremiumStickers(
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_installed_sticker_sets(
        self,
        sticker_type: StickerType,
        request_timeout: float = 10.0,
    ) -> StickerSets:
        """
        Returns a list of installed sticker sets
        :param sticker_type: Type of the sticker sets to return
        :param request_timeout: Request timeout
        """
        return await self(
            GetInstalledStickerSets(
                sticker_type=sticker_type,
            ),
            request_timeout=request_timeout,
        )

    async def get_archived_sticker_sets(
        self,
        sticker_type: StickerType,
        offset_sticker_set_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> StickerSets:
        """
        Returns a list of archived sticker sets
        :param sticker_type: Type of the sticker sets to return
        :param offset_sticker_set_id: Identifier of the sticker set from which to return the result; use 0 to get results from the beginning
        :param limit: The maximum number of sticker sets to return; up to 100
        :param request_timeout: Request timeout
        """
        return await self(
            GetArchivedStickerSets(
                sticker_type=sticker_type,
                offset_sticker_set_id=offset_sticker_set_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_trending_sticker_sets(
        self,
        sticker_type: StickerType,
        offset: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> TrendingStickerSets:
        """
        Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib
        :param sticker_type: Type of the sticker sets to return
        :param offset: The offset from which to return the sticker sets; must be non-negative
        :param limit: The maximum number of sticker sets to be returned; up to 100. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached
        :param request_timeout: Request timeout
        """
        return await self(
            GetTrendingStickerSets(
                sticker_type=sticker_type,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_attached_sticker_sets(
        self,
        file_id: int,
        request_timeout: float = 10.0,
    ) -> StickerSets:
        """
        Returns a list of sticker sets attached to a file, including regular, mask, and emoji sticker sets. Currently, only animations, photos, and videos can have attached sticker sets
        :param file_id: File identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetAttachedStickerSets(
                file_id=file_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_sticker_set(
        self,
        set_id: int,
        request_timeout: float = 10.0,
    ) -> StickerSet:
        """
        Returns information about a sticker set by its identifier
        :param set_id: Identifier of the sticker set
        :param request_timeout: Request timeout
        """
        return await self(
            GetStickerSet(
                set_id=set_id,
            ),
            request_timeout=request_timeout,
        )

    async def search_sticker_set(
        self,
        name: str,
        request_timeout: float = 10.0,
    ) -> StickerSet:
        """
        Searches for a sticker set by its name
        :param name: Name of the sticker set
        :param request_timeout: Request timeout
        """
        return await self(
            SearchStickerSet(
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def search_installed_sticker_sets(
        self,
        sticker_type: StickerType,
        query: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> StickerSets:
        """
        Searches for installed sticker sets by looking for specified query in their title and name
        :param sticker_type: Type of the sticker sets to search for
        :param query: Query to search for
        :param limit: The maximum number of sticker sets to return
        :param request_timeout: Request timeout
        """
        return await self(
            SearchInstalledStickerSets(
                sticker_type=sticker_type,
                query=query,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def search_sticker_sets(
        self,
        sticker_type: StickerType,
        query: str,
        request_timeout: float = 10.0,
    ) -> StickerSets:
        """
        Searches for sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results
        :param sticker_type: Type of the sticker sets to return
        :param query: Query to search for
        :param request_timeout: Request timeout
        """
        return await self(
            SearchStickerSets(
                sticker_type=sticker_type,
                query=query,
            ),
            request_timeout=request_timeout,
        )

    async def change_sticker_set(
        self,
        set_id: int,
        is_installed: bool,
        is_archived: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Installs/uninstalls or activates/archives a sticker set
        :param set_id: Identifier of the sticker set
        :param is_installed: The new value of is_installed
        :param is_archived: The new value of is_archived. A sticker set can't be installed and archived simultaneously
        :param request_timeout: Request timeout
        """
        return await self(
            ChangeStickerSet(
                set_id=set_id,
                is_installed=is_installed,
                is_archived=is_archived,
            ),
            request_timeout=request_timeout,
        )

    async def view_trending_sticker_sets(
        self,
        sticker_set_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs the server that some trending sticker sets have been viewed by the user
        :param sticker_set_ids: Identifiers of viewed trending sticker sets
        :param request_timeout: Request timeout
        """
        return await self(
            ViewTrendingStickerSets(
                sticker_set_ids=sticker_set_ids,
            ),
            request_timeout=request_timeout,
        )

    async def reorder_installed_sticker_sets(
        self,
        sticker_type: StickerType,
        sticker_set_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the order of installed sticker sets
        :param sticker_type: Type of the sticker sets to reorder
        :param sticker_set_ids: Identifiers of installed sticker sets in the new correct order
        :param request_timeout: Request timeout
        """
        return await self(
            ReorderInstalledStickerSets(
                sticker_type=sticker_type,
                sticker_set_ids=sticker_set_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_recent_stickers(
        self,
        is_attached: bool,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns a list of recently used stickers
        :param is_attached: Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecentStickers(
                is_attached=is_attached,
            ),
            request_timeout=request_timeout,
        )

    async def add_recent_sticker(
        self,
        is_attached: bool,
        sticker: InputFile,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first.
        :param is_attached: Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers
        :param sticker: Sticker file to add
        :param request_timeout: Request timeout
        """
        return await self(
            AddRecentSticker(
                is_attached=is_attached,
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def remove_recent_sticker(
        self,
        is_attached: bool,
        sticker: InputFile,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a sticker from the list of recently used stickers
        :param is_attached: Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
        :param sticker: Sticker file to delete
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveRecentSticker(
                is_attached=is_attached,
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def clear_recent_stickers(
        self,
        is_attached: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears the list of recently used stickers
        :param is_attached: Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers
        :param request_timeout: Request timeout
        """
        return await self(
            ClearRecentStickers(
                is_attached=is_attached,
            ),
            request_timeout=request_timeout,
        )

    async def get_favorite_stickers(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns favorite stickers
        :param request_timeout: Request timeout
        """
        return await self(
            GetFavoriteStickers(),
            request_timeout=request_timeout,
        )

    async def add_favorite_sticker(
        self,
        sticker: InputFile,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first.
        :param sticker: Sticker file to add
        :param request_timeout: Request timeout
        """
        return await self(
            AddFavoriteSticker(
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def remove_favorite_sticker(
        self,
        sticker: InputFile,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a sticker from the list of favorite stickers
        :param sticker: Sticker file to delete from the list
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveFavoriteSticker(
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def get_sticker_emojis(
        self,
        sticker: InputFile,
        request_timeout: float = 10.0,
    ) -> Emojis:
        """
        Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
        :param sticker: Sticker file identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetStickerEmojis(
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def search_emojis(
        self,
        text: str,
        input_language_codes: list[str] | None = None,
        request_timeout: float = 10.0,
    ) -> EmojiKeywords:
        """
        Searches for emojis by keywords. Supported only if the file database is enabled. Order of results is unspecified
        :param text: Text to search for
        :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            SearchEmojis(
                text=text,
                input_language_codes=input_language_codes,
            ),
            request_timeout=request_timeout,
        )

    async def get_keyword_emojis(
        self,
        text: str,
        input_language_codes: list[str] | None = None,
        request_timeout: float = 10.0,
    ) -> Emojis:
        """
        Return emojis matching the keyword. Supported only if the file database is enabled. Order of results is unspecified
        :param text: Text to search for
        :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            GetKeywordEmojis(
                text=text,
                input_language_codes=input_language_codes,
            ),
            request_timeout=request_timeout,
        )

    async def get_emoji_categories(
        self,
        type: EmojiCategoryType | None = None,
        request_timeout: float = 10.0,
    ) -> EmojiCategories:
        """
        Returns available emoji categories
        :param type: Type of emoji categories to return; pass null to get default emoji categories
        :param request_timeout: Request timeout
        """
        return await self(
            GetEmojiCategories(
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def get_animated_emoji(
        self,
        emoji: str,
        request_timeout: float = 10.0,
    ) -> AnimatedEmoji:
        """
        Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji
        :param emoji: The emoji
        :param request_timeout: Request timeout
        """
        return await self(
            GetAnimatedEmoji(
                emoji=emoji,
            ),
            request_timeout=request_timeout,
        )

    async def get_emoji_suggestions_url(
        self,
        language_code: str,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation
        :param language_code: Language code for which the emoji replacements will be suggested
        :param request_timeout: Request timeout
        """
        return await self(
            GetEmojiSuggestionsUrl(
                language_code=language_code,
            ),
            request_timeout=request_timeout,
        )

    async def get_custom_emoji_stickers(
        self,
        custom_emoji_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns the list of custom emoji stickers by their identifiers. Stickers are returned in arbitrary order. Only found stickers are returned
        :param custom_emoji_ids: Identifiers of custom emoji stickers. At most 200 custom emoji stickers can be received simultaneously
        :param request_timeout: Request timeout
        """
        return await self(
            GetCustomEmojiStickers(
                custom_emoji_ids=custom_emoji_ids,
            ),
            request_timeout=request_timeout,
        )

    async def get_default_chat_photo_custom_emoji_stickers(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns default list of custom emoji stickers for placing on a chat photo
        :param request_timeout: Request timeout
        """
        return await self(
            GetDefaultChatPhotoCustomEmojiStickers(),
            request_timeout=request_timeout,
        )

    async def get_default_profile_photo_custom_emoji_stickers(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns default list of custom emoji stickers for placing on a profile photo
        :param request_timeout: Request timeout
        """
        return await self(
            GetDefaultProfilePhotoCustomEmojiStickers(),
            request_timeout=request_timeout,
        )

    async def get_default_background_custom_emoji_stickers(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns default list of custom emoji stickers for reply background
        :param request_timeout: Request timeout
        """
        return await self(
            GetDefaultBackgroundCustomEmojiStickers(),
            request_timeout=request_timeout,
        )

    async def get_saved_animations(
        self,
        request_timeout: float = 10.0,
    ) -> Animations:
        """
        Returns saved animations
        :param request_timeout: Request timeout
        """
        return await self(
            GetSavedAnimations(),
            request_timeout=request_timeout,
        )

    async def add_saved_animation(
        self,
        animation: InputFile,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first.
        :param animation: The animation file to be added. Only animations known to the server (i.e., successfully sent via a message) can be added to the list
        :param request_timeout: Request timeout
        """
        return await self(
            AddSavedAnimation(
                animation=animation,
            ),
            request_timeout=request_timeout,
        )

    async def remove_saved_animation(
        self,
        animation: InputFile,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes an animation from the list of saved animations
        :param animation: Animation file to be removed
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveSavedAnimation(
                animation=animation,
            ),
            request_timeout=request_timeout,
        )

    async def get_recent_inline_bots(
        self,
        request_timeout: float = 10.0,
    ) -> Users:
        """
        Returns up to 20 recently used inline bots in the order of their last usage
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecentInlineBots(),
            request_timeout=request_timeout,
        )

    async def search_hashtags(
        self,
        prefix: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> Hashtags:
        """
        Searches for recently used hashtags by their prefix
        :param prefix: Hashtag prefix to search for
        :param limit: The maximum number of hashtags to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            SearchHashtags(
                prefix=prefix,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def remove_recent_hashtag(
        self,
        hashtag: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a hashtag from the list of recently used hashtags
        :param hashtag: Hashtag to delete
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveRecentHashtag(
                hashtag=hashtag,
            ),
            request_timeout=request_timeout,
        )

    async def get_link_preview(
        self,
        text: FormattedText,
        link_preview_options: LinkPreviewOptions | None = None,
        request_timeout: float = 10.0,
    ) -> LinkPreview:
        """
        Returns a link preview by the text of a message. Do not call this function too often. Returns a 404 error if the text has no link preview
        :param text: Message text with formatting
        :param link_preview_options: Options to be used for generation of the link preview; pass null to use default link preview options
        :param request_timeout: Request timeout
        """
        return await self(
            GetLinkPreview(
                text=text,
                link_preview_options=link_preview_options,
            ),
            request_timeout=request_timeout,
        )

    async def get_web_page_instant_view(
        self,
        url: str,
        force_full: bool,
        request_timeout: float = 10.0,
    ) -> WebPageInstantView:
        """
        Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page
        :param url: The web page URL
        :param force_full: Pass true to get full instant view for the web page
        :param request_timeout: Request timeout
        """
        return await self(
            GetWebPageInstantView(
                url=url,
                force_full=force_full,
            ),
            request_timeout=request_timeout,
        )

    async def set_profile_photo(
        self,
        photo: InputChatPhoto,
        is_public: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes a profile photo for the current user
        :param photo: Profile photo to set
        :param is_public: Pass true to set a public photo, which will be visible even the main photo is hidden by privacy settings
        :param request_timeout: Request timeout
        """
        return await self(
            SetProfilePhoto(
                photo=photo,
                is_public=is_public,
            ),
            request_timeout=request_timeout,
        )

    async def delete_profile_photo(
        self,
        profile_photo_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes a profile photo
        :param profile_photo_id: Identifier of the profile photo to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteProfilePhoto(
                profile_photo_id=profile_photo_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_accent_color(
        self,
        accent_color_id: int,
        background_custom_emoji_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes accent color and background custom emoji for the current user; for Telegram Premium users only
        :param accent_color_id: Identifier of the accent color to use
        :param background_custom_emoji_id: Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none
        :param request_timeout: Request timeout
        """
        return await self(
            SetAccentColor(
                accent_color_id=accent_color_id,
                background_custom_emoji_id=background_custom_emoji_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_profile_accent_color(
        self,
        profile_accent_color_id: int,
        profile_background_custom_emoji_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes accent color and background custom emoji for profile of the current user; for Telegram Premium users only
        :param profile_accent_color_id: Identifier of the accent color to use for profile; pass -1 if none
        :param profile_background_custom_emoji_id: Identifier of a custom emoji to be shown on the user's profile photo background; 0 if none
        :param request_timeout: Request timeout
        """
        return await self(
            SetProfileAccentColor(
                profile_accent_color_id=profile_accent_color_id,
                profile_background_custom_emoji_id=profile_background_custom_emoji_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_name(
        self,
        first_name: str,
        last_name: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the first and last name of the current user
        :param first_name: The new value of the first name for the current user; 1-64 characters
        :param last_name: The new value of the optional last name for the current user; 0-64 characters
        :param request_timeout: Request timeout
        """
        return await self(
            SetName(
                first_name=first_name,
                last_name=last_name,
            ),
            request_timeout=request_timeout,
        )

    async def set_bio(
        self,
        bio: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the bio of the current user
        :param bio: The new value of the user bio; 0-getOption('bio_length_max') characters without line feeds
        :param request_timeout: Request timeout
        """
        return await self(
            SetBio(
                bio=bio,
            ),
            request_timeout=request_timeout,
        )

    async def set_username(
        self,
        username: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the editable username of the current user
        :param username: The new value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username
        :param request_timeout: Request timeout
        """
        return await self(
            SetUsername(
                username=username,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_username_is_active(
        self,
        username: str,
        is_active: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes active state for a username of the current user. The editable username can't be disabled. May return an error with a message 'USERNAMES_ACTIVE_TOO_MUCH' if the maximum number of active usernames has been reached
        :param username: The username to change
        :param is_active: Pass true to activate the username; pass false to disable it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleUsernameIsActive(
                username=username,
                is_active=is_active,
            ),
            request_timeout=request_timeout,
        )

    async def reorder_active_usernames(
        self,
        usernames: list[str],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes order of active usernames of the current user
        :param usernames: The new order of active usernames. All currently active usernames must be specified
        :param request_timeout: Request timeout
        """
        return await self(
            ReorderActiveUsernames(
                usernames=usernames,
            ),
            request_timeout=request_timeout,
        )

    async def set_birthdate(
        self,
        birthdate: Birthdate | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the birthdate of the current user
        :param birthdate: The new value of the current user's birthdate; pass null to remove the birthdate
        :param request_timeout: Request timeout
        """
        return await self(
            SetBirthdate(
                birthdate=birthdate,
            ),
            request_timeout=request_timeout,
        )

    async def set_personal_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the personal chat of the current user
        :param chat_id: Identifier of the new personal chat; pass 0 to remove the chat. Use getSuitablePersonalChats to get suitable chats
        :param request_timeout: Request timeout
        """
        return await self(
            SetPersonalChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_emoji_status(
        self,
        emoji_status: EmojiStatus | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the emoji status of the current user; for Telegram Premium users only
        :param emoji_status: New emoji status; pass null to switch to the default badge
        :param request_timeout: Request timeout
        """
        return await self(
            SetEmojiStatus(
                emoji_status=emoji_status,
            ),
            request_timeout=request_timeout,
        )

    async def set_location(
        self,
        location: Location,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the location of the current user. Needs to be called if getOption('is_location_visible') is true and location changes for more than 1 kilometer. Must not be called if the user has a business location
        :param location: The new location of the user
        :param request_timeout: Request timeout
        """
        return await self(
            SetLocation(
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_has_sponsored_messages_enabled(
        self,
        has_sponsored_messages_enabled: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether the current user has sponsored messages enabled. The setting has no effect for users without Telegram Premium for which sponsored messages are always enabled
        :param has_sponsored_messages_enabled: Pass true to enable sponsored messages for the current user; false to disable them
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleHasSponsoredMessagesEnabled(
                has_sponsored_messages_enabled=has_sponsored_messages_enabled,
            ),
            request_timeout=request_timeout,
        )

    async def set_business_location(
        self,
        location: BusinessLocation | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the business location of the current user. Requires Telegram Business subscription
        :param location: The new location of the business; pass null to remove the location
        :param request_timeout: Request timeout
        """
        return await self(
            SetBusinessLocation(
                location=location,
            ),
            request_timeout=request_timeout,
        )

    async def set_business_opening_hours(
        self,
        opening_hours: BusinessOpeningHours | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the business opening hours of the current user. Requires Telegram Business subscription
        :param opening_hours: The new opening hours of the business; pass null to remove the opening hours; up to 28 time intervals can be specified
        :param request_timeout: Request timeout
        """
        return await self(
            SetBusinessOpeningHours(
                opening_hours=opening_hours,
            ),
            request_timeout=request_timeout,
        )

    async def set_business_greeting_message_settings(
        self,
        greeting_message_settings: BusinessGreetingMessageSettings | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the business greeting message settings of the current user. Requires Telegram Business subscription
        :param greeting_message_settings: The new settings for the greeting message of the business; pass null to disable the greeting message
        :param request_timeout: Request timeout
        """
        return await self(
            SetBusinessGreetingMessageSettings(
                greeting_message_settings=greeting_message_settings,
            ),
            request_timeout=request_timeout,
        )

    async def set_business_away_message_settings(
        self,
        away_message_settings: BusinessAwayMessageSettings | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the business away message settings of the current user. Requires Telegram Business subscription
        :param away_message_settings: The new settings for the away message of the business; pass null to disable the away message
        :param request_timeout: Request timeout
        """
        return await self(
            SetBusinessAwayMessageSettings(
                away_message_settings=away_message_settings,
            ),
            request_timeout=request_timeout,
        )

    async def set_business_start_page(
        self,
        start_page: InputBusinessStartPage | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the business start page of the current user. Requires Telegram Business subscription
        :param start_page: The new start page of the business; pass null to remove custom start page
        :param request_timeout: Request timeout
        """
        return await self(
            SetBusinessStartPage(
                start_page=start_page,
            ),
            request_timeout=request_timeout,
        )

    async def send_phone_number_code(
        self,
        phone_number: str,
        type: PhoneNumberCodeType,
        settings: PhoneNumberAuthenticationSettings | None = None,
        request_timeout: float = 10.0,
    ) -> AuthenticationCodeInfo:
        """
        Sends a code to the specified phone number. Aborts previous phone number verification if there was one. On success, returns information about the sent code
        :param phone_number: The phone number, in international format
        :param type: Type of the request for which the code is sent
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings
        :param request_timeout: Request timeout
        """
        return await self(
            SendPhoneNumberCode(
                phone_number=phone_number,
                type=type,
                settings=settings,
            ),
            request_timeout=request_timeout,
        )

    async def send_phone_number_firebase_sms(
        self,
        token: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends Firebase Authentication SMS to the specified phone number. Works only when received a code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos
        :param token: Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application
        :param request_timeout: Request timeout
        """
        return await self(
            SendPhoneNumberFirebaseSms(
                token=token,
            ),
            request_timeout=request_timeout,
        )

    async def report_phone_number_code_missing(
        self,
        mobile_network_code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports that authentication code wasn't delivered via SMS to the specified phone number; for official mobile applications only
        :param mobile_network_code: Current mobile network code
        :param request_timeout: Request timeout
        """
        return await self(
            ReportPhoneNumberCodeMissing(
                mobile_network_code=mobile_network_code,
            ),
            request_timeout=request_timeout,
        )

    async def resend_phone_number_code(
        self,
        reason: ResendCodeReason | None = None,
        request_timeout: float = 10.0,
    ) -> AuthenticationCodeInfo:
        """
        Resends the authentication code sent to a phone number. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed
        :param reason: Reason of code resending; pass null if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            ResendPhoneNumberCode(
                reason=reason,
            ),
            request_timeout=request_timeout,
        )

    async def check_phone_number_code(
        self,
        code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Check the authentication code and completes the request for which the code was sent if appropriate
        :param code: Authentication code to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckPhoneNumberCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def get_business_connected_bot(
        self,
        request_timeout: float = 10.0,
    ) -> BusinessConnectedBot:
        """
        Returns the business bot that is connected to the current user account. Returns a 404 error if there is no connected bot
        :param request_timeout: Request timeout
        """
        return await self(
            GetBusinessConnectedBot(),
            request_timeout=request_timeout,
        )

    async def set_business_connected_bot(
        self,
        bot: BusinessConnectedBot,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds or changes business bot that is connected to the current user account
        :param bot: Connection settings for the bot
        :param request_timeout: Request timeout
        """
        return await self(
            SetBusinessConnectedBot(
                bot=bot,
            ),
            request_timeout=request_timeout,
        )

    async def delete_business_connected_bot(
        self,
        bot_user_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes the business bot that is connected to the current user account
        :param bot_user_id: Unique user identifier for the bot
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteBusinessConnectedBot(
                bot_user_id=bot_user_id,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_business_connected_bot_chat_is_paused(
        self,
        chat_id: int,
        is_paused: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Pauses or resumes the connected business bot in a specific chat
        :param chat_id: Chat identifier
        :param is_paused: Pass true to pause the connected bot in the chat; pass false to resume the bot
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleBusinessConnectedBotChatIsPaused(
                chat_id=chat_id,
                is_paused=is_paused,
            ),
            request_timeout=request_timeout,
        )

    async def remove_business_connected_bot_from_chat(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes the connected business bot from a specific chat by adding the chat to businessRecipients.excluded_chat_ids
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveBusinessConnectedBotFromChat(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_business_chat_links(
        self,
        request_timeout: float = 10.0,
    ) -> BusinessChatLinks:
        """
        Returns business chat links created for the current account
        :param request_timeout: Request timeout
        """
        return await self(
            GetBusinessChatLinks(),
            request_timeout=request_timeout,
        )

    async def create_business_chat_link(
        self,
        link_info: InputBusinessChatLink,
        request_timeout: float = 10.0,
    ) -> BusinessChatLink:
        """
        Creates a business chat link for the current account. Requires Telegram Business subscription. There can be up to getOption('business_chat_link_count_max') links created. Returns the created link
        :param link_info: Information about the link to create
        :param request_timeout: Request timeout
        """
        return await self(
            CreateBusinessChatLink(
                link_info=link_info,
            ),
            request_timeout=request_timeout,
        )

    async def edit_business_chat_link(
        self,
        link: str,
        link_info: InputBusinessChatLink,
        request_timeout: float = 10.0,
    ) -> BusinessChatLink:
        """
        Edits a business chat link of the current account. Requires Telegram Business subscription. Returns the edited link
        :param link: The link to edit
        :param link_info: New description of the link
        :param request_timeout: Request timeout
        """
        return await self(
            EditBusinessChatLink(
                link=link,
                link_info=link_info,
            ),
            request_timeout=request_timeout,
        )

    async def delete_business_chat_link(
        self,
        link: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes a business chat link of the current account
        :param link: The link to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteBusinessChatLink(
                link=link,
            ),
            request_timeout=request_timeout,
        )

    async def get_business_chat_link_info(
        self,
        link_name: str,
        request_timeout: float = 10.0,
    ) -> BusinessChatLinkInfo:
        """
        Returns information about a business chat link
        :param link_name: Name of the link
        :param request_timeout: Request timeout
        """
        return await self(
            GetBusinessChatLinkInfo(
                link_name=link_name,
            ),
            request_timeout=request_timeout,
        )

    async def get_user_link(
        self,
        request_timeout: float = 10.0,
    ) -> UserLink:
        """
        Returns an HTTPS link, which can be used to get information about the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetUserLink(),
            request_timeout=request_timeout,
        )

    async def search_user_by_token(
        self,
        token: str,
        request_timeout: float = 10.0,
    ) -> User:
        """
        Searches a user by a token from the user's link
        :param token: Token to search for
        :param request_timeout: Request timeout
        """
        return await self(
            SearchUserByToken(
                token=token,
            ),
            request_timeout=request_timeout,
        )

    async def set_commands(
        self,
        language_code: str,
        commands: list[BotCommand],
        scope: BotCommandScope | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the list of commands supported by the bot for the given user scope and language; for bots only
        :param language_code: A two-letter ISO 639-1 language code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
        :param commands: List of the bot's commands
        :param scope: The scope to which the commands are relevant; pass null to change commands in the default bot command scope
        :param request_timeout: Request timeout
        """
        return await self(
            SetCommands(
                language_code=language_code,
                commands=commands,
                scope=scope,
            ),
            request_timeout=request_timeout,
        )

    async def delete_commands(
        self,
        language_code: str,
        scope: BotCommandScope | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes commands supported by the bot for the given user scope and language; for bots only
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :param scope: The scope to which the commands are relevant; pass null to delete commands in the default bot command scope
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteCommands(
                language_code=language_code,
                scope=scope,
            ),
            request_timeout=request_timeout,
        )

    async def get_commands(
        self,
        language_code: str,
        scope: BotCommandScope | None = None,
        request_timeout: float = 10.0,
    ) -> BotCommands:
        """
        Returns the list of commands supported by the bot for the given user scope and language; for bots only
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :param scope: The scope to which the commands are relevant; pass null to get commands in the default bot command scope
        :param request_timeout: Request timeout
        """
        return await self(
            GetCommands(
                language_code=language_code,
                scope=scope,
            ),
            request_timeout=request_timeout,
        )

    async def set_menu_button(
        self,
        user_id: int,
        menu_button: BotMenuButton,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets menu button for the given user or for all users; for bots only
        :param user_id: Identifier of the user or 0 to set menu button for all users
        :param menu_button: New menu button
        :param request_timeout: Request timeout
        """
        return await self(
            SetMenuButton(
                user_id=user_id,
                menu_button=menu_button,
            ),
            request_timeout=request_timeout,
        )

    async def get_menu_button(
        self,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> BotMenuButton:
        """
        Returns menu button set by the bot for the given user; for bots only
        :param user_id: Identifier of the user or 0 to get the default menu button
        :param request_timeout: Request timeout
        """
        return await self(
            GetMenuButton(
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_default_group_administrator_rights(
        self,
        default_group_administrator_rights: ChatAdministratorRights | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only
        :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; pass null to remove default rights
        :param request_timeout: Request timeout
        """
        return await self(
            SetDefaultGroupAdministratorRights(
                default_group_administrator_rights=default_group_administrator_rights,
            ),
            request_timeout=request_timeout,
        )

    async def set_default_channel_administrator_rights(
        self,
        default_channel_administrator_rights: ChatAdministratorRights | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets default administrator rights for adding the bot to channel chats; for bots only
        :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; pass null to remove default rights
        :param request_timeout: Request timeout
        """
        return await self(
            SetDefaultChannelAdministratorRights(
                default_channel_administrator_rights=default_channel_administrator_rights,
            ),
            request_timeout=request_timeout,
        )

    async def can_bot_send_messages(
        self,
        bot_user_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks whether the specified bot can send messages to the user. Returns a 404 error if can't and the access can be granted by call to allowBotToSendMessages
        :param bot_user_id: Identifier of the target bot
        :param request_timeout: Request timeout
        """
        return await self(
            CanBotSendMessages(
                bot_user_id=bot_user_id,
            ),
            request_timeout=request_timeout,
        )

    async def allow_bot_to_send_messages(
        self,
        bot_user_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Allows the specified bot to send messages to the user
        :param bot_user_id: Identifier of the target bot
        :param request_timeout: Request timeout
        """
        return await self(
            AllowBotToSendMessages(
                bot_user_id=bot_user_id,
            ),
            request_timeout=request_timeout,
        )

    async def send_web_app_custom_request(
        self,
        bot_user_id: int,
        method: str,
        parameters: str,
        request_timeout: float = 10.0,
    ) -> CustomRequestResult:
        """
        Sends a custom request from a Web App
        :param bot_user_id: Identifier of the bot
        :param method: The method name
        :param parameters: JSON-serialized method parameters
        :param request_timeout: Request timeout
        """
        return await self(
            SendWebAppCustomRequest(
                bot_user_id=bot_user_id,
                method=method,
                parameters=parameters,
            ),
            request_timeout=request_timeout,
        )

    async def get_bot_media_previews(
        self,
        bot_user_id: int,
        request_timeout: float = 10.0,
    ) -> BotMediaPreviews:
        """
        Returns the list of media previews of a bot
        :param bot_user_id: Identifier of the target bot. The bot must have the main Web App
        :param request_timeout: Request timeout
        """
        return await self(
            GetBotMediaPreviews(
                bot_user_id=bot_user_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_bot_media_preview_info(
        self,
        bot_user_id: int,
        language_code: str,
        request_timeout: float = 10.0,
    ) -> BotMediaPreviewInfo:
        """
        Returns the list of media previews for the given language and the list of languages for which the bot has dedicated previews
        :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
        :param language_code: A two-letter ISO 639-1 language code for which to get previews. If empty, then default previews are returned
        :param request_timeout: Request timeout
        """
        return await self(
            GetBotMediaPreviewInfo(
                bot_user_id=bot_user_id,
                language_code=language_code,
            ),
            request_timeout=request_timeout,
        )

    async def add_bot_media_preview(
        self,
        bot_user_id: int,
        language_code: str,
        content: InputStoryContent,
        request_timeout: float = 10.0,
    ) -> BotMediaPreview:
        """
        Adds a new media preview to the beginning of the list of media previews of a bot. Returns the added preview after addition is completed server-side. The total number of previews must not exceed getOption('bot_media_preview_count_max') for the given language
        :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
        :param language_code: A two-letter ISO 639-1 language code for which preview is added. If empty, then the preview will be shown to all users for whose languages there are no dedicated previews.
        :param content: Content of the added preview
        :param request_timeout: Request timeout
        """
        return await self(
            AddBotMediaPreview(
                bot_user_id=bot_user_id,
                language_code=language_code,
                content=content,
            ),
            request_timeout=request_timeout,
        )

    async def edit_bot_media_preview(
        self,
        bot_user_id: int,
        language_code: str,
        file_id: int,
        content: InputStoryContent,
        request_timeout: float = 10.0,
    ) -> BotMediaPreview:
        """
        Replaces media preview in the list of media previews of a bot. Returns the new preview after edit is completed server-side
        :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
        :param language_code: Language code of the media preview to edit
        :param file_id: File identifier of the media to replace
        :param content: Content of the new preview
        :param request_timeout: Request timeout
        """
        return await self(
            EditBotMediaPreview(
                bot_user_id=bot_user_id,
                language_code=language_code,
                file_id=file_id,
                content=content,
            ),
            request_timeout=request_timeout,
        )

    async def reorder_bot_media_previews(
        self,
        bot_user_id: int,
        language_code: str,
        file_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes order of media previews in the list of media previews of a bot
        :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
        :param language_code: Language code of the media previews to reorder
        :param file_ids: File identifiers of the media in the new order
        :param request_timeout: Request timeout
        """
        return await self(
            ReorderBotMediaPreviews(
                bot_user_id=bot_user_id,
                language_code=language_code,
                file_ids=file_ids,
            ),
            request_timeout=request_timeout,
        )

    async def delete_bot_media_previews(
        self,
        bot_user_id: int,
        language_code: str,
        file_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Delete media previews from the list of media previews of a bot
        :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
        :param language_code: Language code of the media previews to delete
        :param file_ids: File identifiers of the media to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteBotMediaPreviews(
                bot_user_id=bot_user_id,
                language_code=language_code,
                file_ids=file_ids,
            ),
            request_timeout=request_timeout,
        )

    async def set_bot_name(
        self,
        bot_user_id: int,
        language_code: str,
        name: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the name of a bot. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param language_code: A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose languages there is no dedicated name
        :param name: New bot's name on the specified language; 0-64 characters; must be non-empty if language code is empty
        :param request_timeout: Request timeout
        """
        return await self(
            SetBotName(
                bot_user_id=bot_user_id,
                language_code=language_code,
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def get_bot_name(
        self,
        bot_user_id: int,
        language_code: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns the name of a bot in the given language. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :param request_timeout: Request timeout
        """
        return await self(
            GetBotName(
                bot_user_id=bot_user_id,
                language_code=language_code,
            ),
            request_timeout=request_timeout,
        )

    async def set_bot_profile_photo(
        self,
        bot_user_id: int,
        photo: InputChatPhoto | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes a profile photo for a bot
        :param bot_user_id: Identifier of the target bot
        :param photo: Profile photo to set; pass null to delete the chat photo
        :param request_timeout: Request timeout
        """
        return await self(
            SetBotProfilePhoto(
                bot_user_id=bot_user_id,
                photo=photo,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_bot_username_is_active(
        self,
        bot_user_id: int,
        username: str,
        is_active: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes active state for a username of a bot. The editable username can't be disabled. May return an error with a message 'USERNAMES_ACTIVE_TOO_MUCH' if the maximum number of active usernames has been reached. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param username: The username to change
        :param is_active: Pass true to activate the username; pass false to disable it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleBotUsernameIsActive(
                bot_user_id=bot_user_id,
                username=username,
                is_active=is_active,
            ),
            request_timeout=request_timeout,
        )

    async def reorder_bot_active_usernames(
        self,
        bot_user_id: int,
        usernames: list[str],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes order of active usernames of a bot. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param usernames: The new order of active usernames. All currently active usernames must be specified
        :param request_timeout: Request timeout
        """
        return await self(
            ReorderBotActiveUsernames(
                bot_user_id=bot_user_id,
                usernames=usernames,
            ),
            request_timeout=request_timeout,
        )

    async def set_bot_info_description(
        self,
        bot_user_id: int,
        language_code: str,
        description: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the text shown in the chat with a bot if the chat is empty. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param language_code: A two-letter ISO 639-1 language code. If empty, the description will be shown to all users for whose languages there is no dedicated description
        :param description: New bot's description on the specified language
        :param request_timeout: Request timeout
        """
        return await self(
            SetBotInfoDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
                description=description,
            ),
            request_timeout=request_timeout,
        )

    async def get_bot_info_description(
        self,
        bot_user_id: int,
        language_code: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns the text shown in the chat with a bot if the chat is empty in the given language. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :param request_timeout: Request timeout
        """
        return await self(
            GetBotInfoDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
            ),
            request_timeout=request_timeout,
        )

    async def set_bot_info_short_description(
        self,
        bot_user_id: int,
        language_code: str,
        short_description: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the text shown on a bot's profile page and sent together with the link when users share the bot. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param language_code: A two-letter ISO 639-1 language code. If empty, the short description will be shown to all users for whose languages there is no dedicated description
        :param short_description: New bot's short description on the specified language
        :param request_timeout: Request timeout
        """
        return await self(
            SetBotInfoShortDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
                short_description=short_description,
            ),
            request_timeout=request_timeout,
        )

    async def get_bot_info_short_description(
        self,
        bot_user_id: int,
        language_code: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns the text shown on a bot's profile page and sent together with the link when users share the bot in the given language. Can be called only if userTypeBot.can_be_edited == true
        :param bot_user_id: Identifier of the target bot
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :param request_timeout: Request timeout
        """
        return await self(
            GetBotInfoShortDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
            ),
            request_timeout=request_timeout,
        )

    async def get_active_sessions(
        self,
        request_timeout: float = 10.0,
    ) -> Sessions:
        """
        Returns all active sessions of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetActiveSessions(),
            request_timeout=request_timeout,
        )

    async def terminate_session(
        self,
        session_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Terminates a session of the current user
        :param session_id: Session identifier
        :param request_timeout: Request timeout
        """
        return await self(
            TerminateSession(
                session_id=session_id,
            ),
            request_timeout=request_timeout,
        )

    async def terminate_all_other_sessions(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Terminates all other sessions of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            TerminateAllOtherSessions(),
            request_timeout=request_timeout,
        )

    async def confirm_session(
        self,
        session_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Confirms an unconfirmed session of the current user from another device
        :param session_id: Session identifier
        :param request_timeout: Request timeout
        """
        return await self(
            ConfirmSession(
                session_id=session_id,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_session_can_accept_calls(
        self,
        session_id: int,
        can_accept_calls: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether a session can accept incoming calls
        :param session_id: Session identifier
        :param can_accept_calls: Pass true to allow accepting incoming calls by the session; pass false otherwise
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSessionCanAcceptCalls(
                session_id=session_id,
                can_accept_calls=can_accept_calls,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_session_can_accept_secret_chats(
        self,
        session_id: int,
        can_accept_secret_chats: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether a session can accept incoming secret chats
        :param session_id: Session identifier
        :param can_accept_secret_chats: Pass true to allow accepting secret chats by the session; pass false otherwise
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSessionCanAcceptSecretChats(
                session_id=session_id,
                can_accept_secret_chats=can_accept_secret_chats,
            ),
            request_timeout=request_timeout,
        )

    async def set_inactive_session_ttl(
        self,
        inactive_session_ttl_days: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the period of inactivity after which sessions will automatically be terminated
        :param inactive_session_ttl_days: New number of days of inactivity before sessions will be automatically terminated; 1-366 days
        :param request_timeout: Request timeout
        """
        return await self(
            SetInactiveSessionTtl(
                inactive_session_ttl_days=inactive_session_ttl_days,
            ),
            request_timeout=request_timeout,
        )

    async def get_connected_websites(
        self,
        request_timeout: float = 10.0,
    ) -> ConnectedWebsites:
        """
        Returns all website where the current user used Telegram to log in
        :param request_timeout: Request timeout
        """
        return await self(
            GetConnectedWebsites(),
            request_timeout=request_timeout,
        )

    async def disconnect_website(
        self,
        website_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Disconnects website from the current user's Telegram account
        :param website_id: Website identifier
        :param request_timeout: Request timeout
        """
        return await self(
            DisconnectWebsite(
                website_id=website_id,
            ),
            request_timeout=request_timeout,
        )

    async def disconnect_all_websites(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Disconnects all websites from the current user's Telegram account
        :param request_timeout: Request timeout
        """
        return await self(
            DisconnectAllWebsites(),
            request_timeout=request_timeout,
        )

    async def set_supergroup_username(
        self,
        supergroup_id: int,
        username: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the editable username of a supergroup or channel, requires owner privileges in the supergroup or channel
        :param supergroup_id: Identifier of the supergroup or channel
        :param username: New value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username
        :param request_timeout: Request timeout
        """
        return await self(
            SetSupergroupUsername(
                supergroup_id=supergroup_id,
                username=username,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_username_is_active(
        self,
        supergroup_id: int,
        username: str,
        is_active: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes active state for a username of a supergroup or channel, requires owner privileges in the supergroup or channel. The editable username can't be disabled.
        :param supergroup_id: Identifier of the supergroup or channel
        :param username: The username to change
        :param is_active: Pass true to activate the username; pass false to disable it
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupUsernameIsActive(
                supergroup_id=supergroup_id,
                username=username,
                is_active=is_active,
            ),
            request_timeout=request_timeout,
        )

    async def disable_all_supergroup_usernames(
        self,
        supergroup_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Disables all active non-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel
        :param supergroup_id: Identifier of the supergroup or channel
        :param request_timeout: Request timeout
        """
        return await self(
            DisableAllSupergroupUsernames(
                supergroup_id=supergroup_id,
            ),
            request_timeout=request_timeout,
        )

    async def reorder_supergroup_active_usernames(
        self,
        supergroup_id: int,
        usernames: list[str],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes order of active usernames of a supergroup or channel, requires owner privileges in the supergroup or channel
        :param supergroup_id: Identifier of the supergroup or channel
        :param usernames: The new order of active usernames. All currently active usernames must be specified
        :param request_timeout: Request timeout
        """
        return await self(
            ReorderSupergroupActiveUsernames(
                supergroup_id=supergroup_id,
                usernames=usernames,
            ),
            request_timeout=request_timeout,
        )

    async def set_supergroup_sticker_set(
        self,
        supergroup_id: int,
        sticker_set_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the sticker set of a supergroup; requires can_change_info administrator right
        :param supergroup_id: Identifier of the supergroup
        :param sticker_set_id: New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set
        :param request_timeout: Request timeout
        """
        return await self(
            SetSupergroupStickerSet(
                supergroup_id=supergroup_id,
                sticker_set_id=sticker_set_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_supergroup_custom_emoji_sticker_set(
        self,
        supergroup_id: int,
        custom_emoji_sticker_set_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the custom emoji sticker set of a supergroup; requires can_change_info administrator right. The chat must have at least chatBoostFeatures.min_custom_emoji_sticker_set_boost_level boost level to pass the corresponding color
        :param supergroup_id: Identifier of the supergroup
        :param custom_emoji_sticker_set_id: New value of the custom emoji sticker set identifier for the supergroup. Use 0 to remove the custom emoji sticker set in the supergroup
        :param request_timeout: Request timeout
        """
        return await self(
            SetSupergroupCustomEmojiStickerSet(
                supergroup_id=supergroup_id,
                custom_emoji_sticker_set_id=custom_emoji_sticker_set_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_supergroup_unrestrict_boost_count(
        self,
        supergroup_id: int,
        unrestrict_boost_count: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the number of times the supergroup must be boosted by a user to ignore slow mode and chat permission restrictions; requires can_restrict_members administrator right
        :param supergroup_id: Identifier of the supergroup
        :param unrestrict_boost_count: New value of the unrestrict_boost_count supergroup setting; 0-8. Use 0 to remove the setting
        :param request_timeout: Request timeout
        """
        return await self(
            SetSupergroupUnrestrictBoostCount(
                supergroup_id=supergroup_id,
                unrestrict_boost_count=unrestrict_boost_count,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_sign_messages(
        self,
        supergroup_id: int,
        sign_messages: bool,
        show_message_sender: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether sender signature or link to the account is added to sent messages in a channel; requires can_change_info member right
        :param supergroup_id: Identifier of the channel
        :param sign_messages: New value of sign_messages
        :param show_message_sender: New value of show_message_sender
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupSignMessages(
                supergroup_id=supergroup_id,
                sign_messages=sign_messages,
                show_message_sender=show_message_sender,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_join_to_send_messages(
        self,
        supergroup_id: int,
        join_to_send_messages: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can_restrict_members administrator right
        :param supergroup_id: Identifier of the supergroup that isn't a broadcast group
        :param join_to_send_messages: New value of join_to_send_messages
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupJoinToSendMessages(
                supergroup_id=supergroup_id,
                join_to_send_messages=join_to_send_messages,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_join_by_request(
        self,
        supergroup_id: int,
        join_by_request: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can_restrict_members administrator right
        :param supergroup_id: Identifier of the supergroup that isn't a broadcast group
        :param join_by_request: New value of join_by_request
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupJoinByRequest(
                supergroup_id=supergroup_id,
                join_by_request=join_by_request,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_all_history_available(
        self,
        supergroup_id: int,
        is_all_history_available: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether the message history of a supergroup is available to new members; requires can_change_info member right
        :param supergroup_id: The identifier of the supergroup
        :param is_all_history_available: The new value of is_all_history_available
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupIsAllHistoryAvailable(
                supergroup_id=supergroup_id,
                is_all_history_available=is_all_history_available,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_can_have_sponsored_messages(
        self,
        supergroup_id: int,
        can_have_sponsored_messages: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether sponsored messages are shown in the channel chat; requires owner privileges in the channel. The chat must have at least chatBoostFeatures.min_sponsored_message_disable_boost_level boost level to disable sponsored messages
        :param supergroup_id: The identifier of the channel
        :param can_have_sponsored_messages: The new value of can_have_sponsored_messages
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupCanHaveSponsoredMessages(
                supergroup_id=supergroup_id,
                can_have_sponsored_messages=can_have_sponsored_messages,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_has_hidden_members(
        self,
        supergroup_id: int,
        has_hidden_members: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether non-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers. Can be called only if supergroupFullInfo.can_hide_members == true
        :param supergroup_id: Identifier of the supergroup
        :param has_hidden_members: New value of has_hidden_members
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupHasHiddenMembers(
                supergroup_id=supergroup_id,
                has_hidden_members=has_hidden_members,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_has_aggressive_anti_spam_enabled(
        self,
        supergroup_id: int,
        has_aggressive_anti_spam_enabled: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether aggressive anti-spam checks are enabled in the supergroup. Can be called only if supergroupFullInfo.can_toggle_aggressive_anti_spam == true
        :param supergroup_id: The identifier of the supergroup, which isn't a broadcast group
        :param has_aggressive_anti_spam_enabled: The new value of has_aggressive_anti_spam_enabled
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupHasAggressiveAntiSpamEnabled(
                supergroup_id=supergroup_id,
                has_aggressive_anti_spam_enabled=has_aggressive_anti_spam_enabled,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_forum(
        self,
        supergroup_id: int,
        is_forum: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Toggles whether the supergroup is a forum; requires owner privileges in the supergroup. Discussion supergroups can't be converted to forums
        :param supergroup_id: Identifier of the supergroup
        :param is_forum: New value of is_forum
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupIsForum(
                supergroup_id=supergroup_id,
                is_forum=is_forum,
            ),
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_broadcast_group(
        self,
        supergroup_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup
        :param supergroup_id: Identifier of the supergroup
        :param request_timeout: Request timeout
        """
        return await self(
            ToggleSupergroupIsBroadcastGroup(
                supergroup_id=supergroup_id,
            ),
            request_timeout=request_timeout,
        )

    async def report_supergroup_spam(
        self,
        supergroup_id: int,
        message_ids: list[int],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports messages in a supergroup as spam; requires administrator rights in the supergroup
        :param supergroup_id: Supergroup identifier
        :param message_ids: Identifiers of messages to report. Use messageProperties.can_be_reported to check whether the message can be reported
        :param request_timeout: Request timeout
        """
        return await self(
            ReportSupergroupSpam(
                supergroup_id=supergroup_id,
                message_ids=message_ids,
            ),
            request_timeout=request_timeout,
        )

    async def report_supergroup_anti_spam_false_positive(
        self,
        supergroup_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports a false deletion of a message by aggressive anti-spam checks; requires administrator rights in the supergroup. Can be called only for messages from chatEventMessageDeleted with can_report_anti_spam_false_positive == true
        :param supergroup_id: Supergroup identifier
        :param message_id: Identifier of the erroneously deleted message from chatEventMessageDeleted
        :param request_timeout: Request timeout
        """
        return await self(
            ReportSupergroupAntiSpamFalsePositive(
                supergroup_id=supergroup_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_supergroup_members(
        self,
        supergroup_id: int,
        offset: int,
        limit: int,
        filter: SupergroupMembersFilter | None = None,
        request_timeout: float = 10.0,
    ) -> ChatMembers:
        """
        Returns information about members or banned users in a supergroup or channel. Can be used only if supergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters
        :param supergroup_id: Identifier of the supergroup or channel
        :param offset: Number of users to skip
        :param limit: The maximum number of users to be returned; up to 200
        :param filter: The type of users to return; pass null to use supergroupMembersFilterRecent
        :param request_timeout: Request timeout
        """
        return await self(
            GetSupergroupMembers(
                supergroup_id=supergroup_id,
                offset=offset,
                limit=limit,
                filter=filter,
            ),
            request_timeout=request_timeout,
        )

    async def close_secret_chat(
        self,
        secret_chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Closes a secret chat, effectively transferring its state to secretChatStateClosed
        :param secret_chat_id: Secret chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            CloseSecretChat(
                secret_chat_id=secret_chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_event_log(
        self,
        chat_id: int,
        query: str,
        from_event_id: int,
        limit: int,
        user_ids: list[int],
        filters: ChatEventLogFilters | None = None,
        request_timeout: float = 10.0,
    ) -> ChatEvents:
        """
        Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i.e., in order of decreasing event_id)
        :param chat_id: Chat identifier
        :param query: Search query by which to filter events
        :param from_event_id: Identifier of an event from which to return results. Use 0 to get results from the latest events
        :param limit: The maximum number of events to return; up to 100
        :param user_ids: User identifiers by which to filter events. By default, events relating to all users will be returned
        :param filters: The types of events to return; pass null to get chat events of all types
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatEventLog(
                chat_id=chat_id,
                query=query,
                from_event_id=from_event_id,
                limit=limit,
                user_ids=user_ids,
                filters=filters,
            ),
            request_timeout=request_timeout,
        )

    async def get_time_zones(
        self,
        request_timeout: float = 10.0,
    ) -> TimeZones:
        """
        Returns the list of supported time zones
        :param request_timeout: Request timeout
        """
        return await self(
            GetTimeZones(),
            request_timeout=request_timeout,
        )

    async def get_payment_form(
        self,
        input_invoice: InputInvoice,
        theme: ThemeParameters | None = None,
        request_timeout: float = 10.0,
    ) -> PaymentForm:
        """
        Returns an invoice payment form. This method must be called when the user presses inline button of the type inlineKeyboardButtonTypeBuy, or wants to buy access to media in a messagePaidMedia message
        :param input_invoice: The invoice
        :param theme: Preferred payment form theme; pass null to use the default theme
        :param request_timeout: Request timeout
        """
        return await self(
            GetPaymentForm(
                input_invoice=input_invoice,
                theme=theme,
            ),
            request_timeout=request_timeout,
        )

    async def validate_order_info(
        self,
        input_invoice: InputInvoice,
        allow_save: bool,
        order_info: OrderInfo | None = None,
        request_timeout: float = 10.0,
    ) -> ValidatedOrderInfo:
        """
        Validates the order information provided by a user and returns the available shipping options for a flexible invoice
        :param input_invoice: The invoice
        :param allow_save: Pass true to save the order information
        :param order_info: The order information, provided by the user; pass null if empty
        :param request_timeout: Request timeout
        """
        return await self(
            ValidateOrderInfo(
                input_invoice=input_invoice,
                allow_save=allow_save,
                order_info=order_info,
            ),
            request_timeout=request_timeout,
        )

    async def send_payment_form(
        self,
        input_invoice: InputInvoice,
        payment_form_id: int,
        order_info_id: str,
        shipping_option_id: str,
        tip_amount: int,
        credentials: InputCredentials | None = None,
        request_timeout: float = 10.0,
    ) -> PaymentResult:
        """
        Sends a filled-out payment form to the bot for final verification
        :param input_invoice: The invoice
        :param payment_form_id: Payment form identifier returned by getPaymentForm
        :param order_info_id: Identifier returned by validateOrderInfo, or an empty string
        :param shipping_option_id: Identifier of a chosen shipping option, if applicable
        :param tip_amount: Chosen by the user amount of tip in the smallest units of the currency
        :param credentials: The credentials chosen by user for payment; pass null for a payment in Telegram Stars
        :param request_timeout: Request timeout
        """
        return await self(
            SendPaymentForm(
                input_invoice=input_invoice,
                payment_form_id=payment_form_id,
                order_info_id=order_info_id,
                shipping_option_id=shipping_option_id,
                tip_amount=tip_amount,
                credentials=credentials,
            ),
            request_timeout=request_timeout,
        )

    async def get_payment_receipt(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> PaymentReceipt:
        """
        Returns information about a successful payment
        :param chat_id: Chat identifier of the messagePaymentSuccessful message
        :param message_id: Message identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetPaymentReceipt(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_saved_order_info(
        self,
        request_timeout: float = 10.0,
    ) -> OrderInfo:
        """
        Returns saved order information. Returns a 404 error if there is no saved order information
        :param request_timeout: Request timeout
        """
        return await self(
            GetSavedOrderInfo(),
            request_timeout=request_timeout,
        )

    async def delete_saved_order_info(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes saved order information
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteSavedOrderInfo(),
            request_timeout=request_timeout,
        )

    async def delete_saved_credentials(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes saved credentials for all payment provider bots
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteSavedCredentials(),
            request_timeout=request_timeout,
        )

    async def create_invoice_link(
        self,
        invoice: InputMessageContent,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Creates a link for the given invoice; for bots only
        :param invoice: Information about the invoice of the type inputMessageInvoice
        :param request_timeout: Request timeout
        """
        return await self(
            CreateInvoiceLink(
                invoice=invoice,
            ),
            request_timeout=request_timeout,
        )

    async def refund_star_payment(
        self,
        user_id: int,
        telegram_payment_charge_id: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Refunds a previously done payment in Telegram Stars
        :param user_id: Identifier of the user that did the payment
        :param telegram_payment_charge_id: Telegram payment identifier
        :param request_timeout: Request timeout
        """
        return await self(
            RefundStarPayment(
                user_id=user_id,
                telegram_payment_charge_id=telegram_payment_charge_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_support_user(
        self,
        request_timeout: float = 10.0,
    ) -> User:
        """
        Returns a user that can be contacted to get support
        :param request_timeout: Request timeout
        """
        return await self(
            GetSupportUser(),
            request_timeout=request_timeout,
        )

    async def get_background_url(
        self,
        name: str,
        type: BackgroundType,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Constructs a persistent HTTP URL for a background
        :param name: Background name
        :param type: Background type; backgroundTypeChatTheme isn't supported
        :param request_timeout: Request timeout
        """
        return await self(
            GetBackgroundUrl(
                name=name,
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def search_background(
        self,
        name: str,
        request_timeout: float = 10.0,
    ) -> Background:
        """
        Searches for a background by its name
        :param name: The name of the background
        :param request_timeout: Request timeout
        """
        return await self(
            SearchBackground(
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def set_default_background(
        self,
        for_dark_theme: bool,
        background: InputBackground | None = None,
        type: BackgroundType | None = None,
        request_timeout: float = 10.0,
    ) -> Background:
        """
        Sets default background for chats; adds the background to the list of installed backgrounds
        :param for_dark_theme: Pass true if the background is set for a dark theme
        :param background: The input background to use; pass null to create a new filled background
        :param type: Background type; pass null to use the default type of the remote background; backgroundTypeChatTheme isn't supported
        :param request_timeout: Request timeout
        """
        return await self(
            SetDefaultBackground(
                for_dark_theme=for_dark_theme,
                background=background,
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def delete_default_background(
        self,
        for_dark_theme: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes default background for chats
        :param for_dark_theme: Pass true if the background is deleted for a dark theme
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteDefaultBackground(
                for_dark_theme=for_dark_theme,
            ),
            request_timeout=request_timeout,
        )

    async def get_installed_backgrounds(
        self,
        for_dark_theme: bool,
        request_timeout: float = 10.0,
    ) -> Backgrounds:
        """
        Returns backgrounds installed by the user
        :param for_dark_theme: Pass true to order returned backgrounds for a dark theme
        :param request_timeout: Request timeout
        """
        return await self(
            GetInstalledBackgrounds(
                for_dark_theme=for_dark_theme,
            ),
            request_timeout=request_timeout,
        )

    async def remove_installed_background(
        self,
        background_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes background from the list of installed backgrounds
        :param background_id: The background identifier
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveInstalledBackground(
                background_id=background_id,
            ),
            request_timeout=request_timeout,
        )

    async def reset_installed_backgrounds(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Resets list of installed backgrounds to its default value
        :param request_timeout: Request timeout
        """
        return await self(
            ResetInstalledBackgrounds(),
            request_timeout=request_timeout,
        )

    async def get_localization_target_info(
        self,
        only_local: bool,
        request_timeout: float = 10.0,
    ) -> LocalizationTargetInfo:
        """
        Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization
        :param only_local: Pass true to get only locally available information without sending network requests
        :param request_timeout: Request timeout
        """
        return await self(
            GetLocalizationTargetInfo(
                only_local=only_local,
            ),
            request_timeout=request_timeout,
        )

    async def get_language_pack_info(
        self,
        language_pack_id: str,
        request_timeout: float = 10.0,
    ) -> LanguagePackInfo:
        """
        Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization
        :param language_pack_id: Language pack identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetLanguagePackInfo(
                language_pack_id=language_pack_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_language_pack_strings(
        self,
        language_pack_id: str,
        keys: list[str],
        request_timeout: float = 10.0,
    ) -> LanguagePackStrings:
        """
        Returns strings from a language pack in the current localization target by their keys. Can be called before authorization
        :param language_pack_id: Language pack identifier of the strings to be returned
        :param keys: Language pack keys of the strings to be returned; leave empty to request all available strings
        :param request_timeout: Request timeout
        """
        return await self(
            GetLanguagePackStrings(
                language_pack_id=language_pack_id,
                keys=keys,
            ),
            request_timeout=request_timeout,
        )

    async def synchronize_language_pack(
        self,
        language_pack_id: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Fetches the latest versions of all strings from a language pack in the current localization target from the server.
        :param language_pack_id: Language pack identifier
        :param request_timeout: Request timeout
        """
        return await self(
            SynchronizeLanguagePack(
                language_pack_id=language_pack_id,
            ),
            request_timeout=request_timeout,
        )

    async def add_custom_server_language_pack(
        self,
        language_pack_id: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization
        :param language_pack_id: Identifier of a language pack to be added
        :param request_timeout: Request timeout
        """
        return await self(
            AddCustomServerLanguagePack(
                language_pack_id=language_pack_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_custom_language_pack(
        self,
        info: LanguagePackInfo,
        strings: list[LanguagePackString],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds or changes a custom local language pack to the current localization target
        :param info: Information about the language pack. Language pack identifier must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization
        :param strings: Strings of the new language pack
        :param request_timeout: Request timeout
        """
        return await self(
            SetCustomLanguagePack(
                info=info,
                strings=strings,
            ),
            request_timeout=request_timeout,
        )

    async def edit_custom_language_pack_info(
        self,
        info: LanguagePackInfo,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Edits information about a custom local language pack in the current localization target. Can be called before authorization
        :param info: New information about the custom local language pack
        :param request_timeout: Request timeout
        """
        return await self(
            EditCustomLanguagePackInfo(
                info=info,
            ),
            request_timeout=request_timeout,
        )

    async def set_custom_language_pack_string(
        self,
        language_pack_id: str,
        new_string: LanguagePackString,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds, edits or deletes a string in a custom local language pack. Can be called before authorization
        :param language_pack_id: Identifier of a previously added custom local language pack in the current localization target
        :param new_string: New language pack string
        :param request_timeout: Request timeout
        """
        return await self(
            SetCustomLanguagePackString(
                language_pack_id=language_pack_id,
                new_string=new_string,
            ),
            request_timeout=request_timeout,
        )

    async def delete_language_pack(
        self,
        language_pack_id: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted.
        :param language_pack_id: Identifier of the language pack to delete
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteLanguagePack(
                language_pack_id=language_pack_id,
            ),
            request_timeout=request_timeout,
        )

    async def register_device(
        self,
        device_token: DeviceToken,
        other_user_ids: list[int],
        request_timeout: float = 10.0,
    ) -> PushReceiverId:
        """
        Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription
        :param device_token: Device token
        :param other_user_ids: List of user identifiers of other users currently using the application
        :param request_timeout: Request timeout
        """
        return await self(
            RegisterDevice(
                device_token=device_token,
                other_user_ids=other_user_ids,
            ),
            request_timeout=request_timeout,
        )

    async def process_push_notification(
        self,
        payload: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization
        :param payload: JSON-encoded push notification payload with all fields sent by the server, and 'google.sent_time' and 'google.notification.sound' fields added
        :param request_timeout: Request timeout
        """
        return await self(
            ProcessPushNotification(
                payload=payload,
            ),
            request_timeout=request_timeout,
        )

    async def get_push_receiver_id(
        self,
        payload: str,
        request_timeout: float = 10.0,
    ) -> PushReceiverId:
        """
        Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously
        :param payload: JSON-encoded push notification payload
        :param request_timeout: Request timeout
        """
        return await self(
            GetPushReceiverId(
                payload=payload,
            ),
            request_timeout=request_timeout,
        )

    async def get_recently_visited_t_me_urls(
        self,
        referrer: str,
        request_timeout: float = 10.0,
    ) -> TMeUrls:
        """
        Returns t.me URLs recently visited by a newly registered user
        :param referrer: Google Play referrer to identify the user
        :param request_timeout: Request timeout
        """
        return await self(
            GetRecentlyVisitedTMeUrls(
                referrer=referrer,
            ),
            request_timeout=request_timeout,
        )

    async def set_user_privacy_setting_rules(
        self,
        setting: UserPrivacySetting,
        rules: UserPrivacySettingRules,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes user privacy settings
        :param setting: The privacy setting
        :param rules: The new privacy rules
        :param request_timeout: Request timeout
        """
        return await self(
            SetUserPrivacySettingRules(
                setting=setting,
                rules=rules,
            ),
            request_timeout=request_timeout,
        )

    async def get_user_privacy_setting_rules(
        self,
        setting: UserPrivacySetting,
        request_timeout: float = 10.0,
    ) -> UserPrivacySettingRules:
        """
        Returns the current privacy settings
        :param setting: The privacy setting
        :param request_timeout: Request timeout
        """
        return await self(
            GetUserPrivacySettingRules(
                setting=setting,
            ),
            request_timeout=request_timeout,
        )

    async def set_read_date_privacy_settings(
        self,
        settings: ReadDatePrivacySettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes privacy settings for message read date
        :param settings: New settings
        :param request_timeout: Request timeout
        """
        return await self(
            SetReadDatePrivacySettings(
                settings=settings,
            ),
            request_timeout=request_timeout,
        )

    async def get_read_date_privacy_settings(
        self,
        request_timeout: float = 10.0,
    ) -> ReadDatePrivacySettings:
        """
        Returns privacy settings for message read date
        :param request_timeout: Request timeout
        """
        return await self(
            GetReadDatePrivacySettings(),
            request_timeout=request_timeout,
        )

    async def set_new_chat_privacy_settings(
        self,
        settings: NewChatPrivacySettings,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes privacy settings for new chat creation; can be used only if getOption('can_set_new_chat_privacy_settings')
        :param settings: New settings
        :param request_timeout: Request timeout
        """
        return await self(
            SetNewChatPrivacySettings(
                settings=settings,
            ),
            request_timeout=request_timeout,
        )

    async def get_new_chat_privacy_settings(
        self,
        request_timeout: float = 10.0,
    ) -> NewChatPrivacySettings:
        """
        Returns privacy settings for new chat creation
        :param request_timeout: Request timeout
        """
        return await self(
            GetNewChatPrivacySettings(),
            request_timeout=request_timeout,
        )

    async def can_send_message_to_user(
        self,
        user_id: int,
        only_local: bool,
        request_timeout: float = 10.0,
    ) -> CanSendMessageToUserResult:
        """
        Check whether the current user can message another user or try to create a chat with them
        :param user_id: Identifier of the other user
        :param only_local: Pass true to get only locally available information without sending network requests
        :param request_timeout: Request timeout
        """
        return await self(
            CanSendMessageToUser(
                user_id=user_id,
                only_local=only_local,
            ),
            request_timeout=request_timeout,
        )

    async def get_option(
        self,
        name: str,
        request_timeout: float = 10.0,
    ) -> OptionValue:
        """
        Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization. Can be called synchronously for options 'version' and 'commit_hash'
        :param name: The name of the option
        :param request_timeout: Request timeout
        """
        return await self(
            GetOption(
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def set_option(
        self,
        name: str,
        value: OptionValue | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization
        :param name: The name of the option
        :param value: The new value of the option; pass null to reset option value to a default value
        :param request_timeout: Request timeout
        """
        return await self(
            SetOption(
                name=name,
                value=value,
            ),
            request_timeout=request_timeout,
        )

    async def set_account_ttl(
        self,
        ttl: AccountTtl,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the period of inactivity after which the account of the current user will automatically be deleted
        :param ttl: New account TTL
        :param request_timeout: Request timeout
        """
        return await self(
            SetAccountTtl(
                ttl=ttl,
            ),
            request_timeout=request_timeout,
        )

    async def get_account_ttl(
        self,
        request_timeout: float = 10.0,
    ) -> AccountTtl:
        """
        Returns the period of inactivity after which the account of the current user will automatically be deleted
        :param request_timeout: Request timeout
        """
        return await self(
            GetAccountTtl(),
            request_timeout=request_timeout,
        )

    async def delete_account(
        self,
        reason: str,
        password: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account.
        :param reason: The reason why the account was deleted; optional
        :param password: The 2-step verification password of the current user. If the current user isn't authorized, then an empty string can be passed and account deletion can be canceled within one week
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteAccount(
                reason=reason,
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def set_default_message_auto_delete_time(
        self,
        message_auto_delete_time: MessageAutoDeleteTime,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the default message auto-delete time for new chats
        :param message_auto_delete_time: New default message auto-delete time; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :param request_timeout: Request timeout
        """
        return await self(
            SetDefaultMessageAutoDeleteTime(
                message_auto_delete_time=message_auto_delete_time,
            ),
            request_timeout=request_timeout,
        )

    async def get_default_message_auto_delete_time(
        self,
        request_timeout: float = 10.0,
    ) -> MessageAutoDeleteTime:
        """
        Returns default message auto-delete time setting for new chats
        :param request_timeout: Request timeout
        """
        return await self(
            GetDefaultMessageAutoDeleteTime(),
            request_timeout=request_timeout,
        )

    async def remove_chat_action_bar(
        self,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a chat action bar without any other action
        :param chat_id: Chat identifier
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveChatActionBar(
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def report_chat(
        self,
        chat_id: int,
        reason: ReportReason,
        text: str,
        message_ids: list[int] | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported
        :param chat_id: Chat identifier
        :param reason: The reason for reporting the chat
        :param text: Additional report details; 0-1024 characters
        :param message_ids: Identifiers of reported messages; may be empty to report the whole chat. Use messageProperties.can_be_reported to check whether the message can be reported
        :param request_timeout: Request timeout
        """
        return await self(
            ReportChat(
                chat_id=chat_id,
                reason=reason,
                text=text,
                message_ids=message_ids,
            ),
            request_timeout=request_timeout,
        )

    async def report_chat_photo(
        self,
        chat_id: int,
        file_id: int,
        reason: ReportReason,
        text: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports a chat photo to the Telegram moderators. A chat photo can be reported only if chat.can_be_reported
        :param chat_id: Chat identifier
        :param file_id: Identifier of the photo to report. Only full photos from chatPhoto can be reported
        :param reason: The reason for reporting the chat photo
        :param text: Additional report details; 0-1024 characters
        :param request_timeout: Request timeout
        """
        return await self(
            ReportChatPhoto(
                chat_id=chat_id,
                file_id=file_id,
                reason=reason,
                text=text,
            ),
            request_timeout=request_timeout,
        )

    async def report_message_reactions(
        self,
        chat_id: int,
        message_id: int,
        sender_id: MessageSender,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reports reactions set on a message to the Telegram moderators. Reactions on a message can be reported only if messageProperties.can_report_reactions
        :param chat_id: Chat identifier
        :param message_id: Message identifier
        :param sender_id: Identifier of the sender, which added the reaction
        :param request_timeout: Request timeout
        """
        return await self(
            ReportMessageReactions(
                chat_id=chat_id,
                message_id=message_id,
                sender_id=sender_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_revenue_statistics(
        self,
        chat_id: int,
        is_dark: bool,
        request_timeout: float = 10.0,
    ) -> ChatRevenueStatistics:
        """
        Returns detailed revenue statistics about a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true
        :param chat_id: Chat identifier
        :param is_dark: Pass true if a dark theme is used by the application
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatRevenueStatistics(
                chat_id=chat_id,
                is_dark=is_dark,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_revenue_withdrawal_url(
        self,
        chat_id: int,
        password: str,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns a URL for chat revenue withdrawal; requires owner privileges in the chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true and getOption('can_withdraw_chat_revenue')
        :param chat_id: Chat identifier
        :param password: The 2-step verification password of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatRevenueWithdrawalUrl(
                chat_id=chat_id,
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_revenue_transactions(
        self,
        chat_id: int,
        offset: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> ChatRevenueTransactions:
        """
        Returns the list of revenue transactions for a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true
        :param chat_id: Chat identifier
        :param offset: Number of transactions to skip
        :param limit: The maximum number of transactions to be returned; up to 200
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatRevenueTransactions(
                chat_id=chat_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_star_revenue_statistics(
        self,
        owner_id: MessageSender,
        is_dark: bool,
        request_timeout: float = 10.0,
    ) -> StarRevenueStatistics:
        """
        Returns detailed Telegram Star revenue statistics
        :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of a channel chat with supergroupFullInfo.can_get_star_revenue_statistics == true
        :param is_dark: Pass true if a dark theme is used by the application
        :param request_timeout: Request timeout
        """
        return await self(
            GetStarRevenueStatistics(
                owner_id=owner_id,
                is_dark=is_dark,
            ),
            request_timeout=request_timeout,
        )

    async def get_star_withdrawal_url(
        self,
        owner_id: MessageSender,
        star_count: int,
        password: str,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns a URL for Telegram Star withdrawal
        :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat
        :param star_count: The number of Telegram Stars to withdraw. Must be at least getOption('star_withdrawal_count_min')
        :param password: The 2-step verification password of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetStarWithdrawalUrl(
                owner_id=owner_id,
                star_count=star_count,
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def get_star_ad_account_url(
        self,
        owner_id: MessageSender,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns a URL for a Telegram Ad platform account that can be used to set up advertisements for the chat paid in the owned Telegram Stars
        :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetStarAdAccountUrl(
                owner_id=owner_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_chat_statistics(
        self,
        chat_id: int,
        is_dark: bool,
        request_timeout: float = 10.0,
    ) -> ChatStatistics:
        """
        Returns detailed statistics about a chat. Currently, this method can be used only for supergroups and channels. Can be used only if supergroupFullInfo.can_get_statistics == true
        :param chat_id: Chat identifier
        :param is_dark: Pass true if a dark theme is used by the application
        :param request_timeout: Request timeout
        """
        return await self(
            GetChatStatistics(
                chat_id=chat_id,
                is_dark=is_dark,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_statistics(
        self,
        chat_id: int,
        message_id: int,
        is_dark: bool,
        request_timeout: float = 10.0,
    ) -> MessageStatistics:
        """
        Returns detailed statistics about a message. Can be used only if messageProperties.can_get_statistics == true
        :param chat_id: Chat identifier
        :param message_id: Message identifier
        :param is_dark: Pass true if a dark theme is used by the application
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessageStatistics(
                chat_id=chat_id,
                message_id=message_id,
                is_dark=is_dark,
            ),
            request_timeout=request_timeout,
        )

    async def get_message_public_forwards(
        self,
        chat_id: int,
        message_id: int,
        offset: str,
        limit: int,
        request_timeout: float = 10.0,
    ) -> PublicForwards:
        """
        Returns forwarded copies of a channel message to different public channels and public reposts as a story. Can be used only if messageProperties.can_get_statistics == true. For optimal performance, the number of returned messages and stories is chosen by TDLib
        :param chat_id: Chat identifier of the message
        :param message_id: Message identifier
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of messages and stories to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            GetMessagePublicForwards(
                chat_id=chat_id,
                message_id=message_id,
                offset=offset,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_story_statistics(
        self,
        chat_id: int,
        story_id: int,
        is_dark: bool,
        request_timeout: float = 10.0,
    ) -> StoryStatistics:
        """
        Returns detailed statistics about a story. Can be used only if story.can_get_statistics == true
        :param chat_id: Chat identifier
        :param story_id: Story identifier
        :param is_dark: Pass true if a dark theme is used by the application
        :param request_timeout: Request timeout
        """
        return await self(
            GetStoryStatistics(
                chat_id=chat_id,
                story_id=story_id,
                is_dark=is_dark,
            ),
            request_timeout=request_timeout,
        )

    async def get_statistical_graph(
        self,
        chat_id: int,
        token: str,
        x: int,
        request_timeout: float = 10.0,
    ) -> StatisticalGraph:
        """
        Loads an asynchronous or a zoomed in statistical graph
        :param chat_id: Chat identifier
        :param token: The token for graph loading
        :param x: X-value for zoomed in graph or 0 otherwise
        :param request_timeout: Request timeout
        """
        return await self(
            GetStatisticalGraph(
                chat_id=chat_id,
                token=token,
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def get_storage_statistics(
        self,
        chat_limit: int,
        request_timeout: float = 10.0,
    ) -> StorageStatistics:
        """
        Returns storage usage statistics. Can be called before authorization
        :param chat_limit: The maximum number of chats with the largest storage usage for which separate statistics need to be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0
        :param request_timeout: Request timeout
        """
        return await self(
            GetStorageStatistics(
                chat_limit=chat_limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_storage_statistics_fast(
        self,
        request_timeout: float = 10.0,
    ) -> StorageStatisticsFast:
        """
        Quickly returns approximate storage usage statistics. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            GetStorageStatisticsFast(),
            request_timeout=request_timeout,
        )

    async def get_database_statistics(
        self,
        request_timeout: float = 10.0,
    ) -> DatabaseStatistics:
        """
        Returns database statistics
        :param request_timeout: Request timeout
        """
        return await self(
            GetDatabaseStatistics(),
            request_timeout=request_timeout,
        )

    async def optimize_storage(
        self,
        size: int,
        ttl: int,
        count: int,
        immunity_delay: int,
        return_deleted_file_statistics: bool,
        chat_limit: int,
        file_types: list[FileType] | None = None,
        chat_ids: list[int] | None = None,
        exclude_chat_ids: list[int] | None = None,
        request_timeout: float = 10.0,
    ) -> StorageStatistics:
        """
        Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted
        :param size: Limit on the total size of files after deletion, in bytes. Pass -1 to use the default limit
        :param ttl: Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit
        :param count: Limit on the total number of files after deletion. Pass -1 to use the default limit
        :param immunity_delay: The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value
        :param return_deleted_file_statistics: Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics
        :param chat_limit: Same as in getStorageStatistics. Affects only returned statistics
        :param file_types: If non-empty, only files with the given types are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
        :param chat_ids: If non-empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)
        :param exclude_chat_ids: If non-empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)
        :param request_timeout: Request timeout
        """
        return await self(
            OptimizeStorage(
                size=size,
                ttl=ttl,
                count=count,
                immunity_delay=immunity_delay,
                return_deleted_file_statistics=return_deleted_file_statistics,
                chat_limit=chat_limit,
                file_types=file_types,
                chat_ids=chat_ids,
                exclude_chat_ids=exclude_chat_ids,
            ),
            request_timeout=request_timeout,
        )

    async def set_network_type(
        self,
        type: NetworkType | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks,
        :param type: The new network type; pass null to set network type to networkTypeOther
        :param request_timeout: Request timeout
        """
        return await self(
            SetNetworkType(
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def get_network_statistics(
        self,
        only_current: bool,
        request_timeout: float = 10.0,
    ) -> NetworkStatistics:
        """
        Returns network data usage statistics. Can be called before authorization
        :param only_current: Pass true to get statistics only for the current library launch
        :param request_timeout: Request timeout
        """
        return await self(
            GetNetworkStatistics(
                only_current=only_current,
            ),
            request_timeout=request_timeout,
        )

    async def add_network_statistics(
        self,
        entry: NetworkStatisticsEntry,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds the specified data to data usage statistics. Can be called before authorization
        :param entry: The network statistics entry with the data to be added to statistics
        :param request_timeout: Request timeout
        """
        return await self(
            AddNetworkStatistics(
                entry=entry,
            ),
            request_timeout=request_timeout,
        )

    async def reset_network_statistics(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Resets all network data usage statistics to zero. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            ResetNetworkStatistics(),
            request_timeout=request_timeout,
        )

    async def get_auto_download_settings_presets(
        self,
        request_timeout: float = 10.0,
    ) -> AutoDownloadSettingsPresets:
        """
        Returns auto-download settings presets for the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetAutoDownloadSettingsPresets(),
            request_timeout=request_timeout,
        )

    async def set_auto_download_settings(
        self,
        settings: AutoDownloadSettings,
        type: NetworkType,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets auto-download settings
        :param settings: New user auto-download settings
        :param type: Type of the network for which the new settings are relevant
        :param request_timeout: Request timeout
        """
        return await self(
            SetAutoDownloadSettings(
                settings=settings,
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def get_autosave_settings(
        self,
        request_timeout: float = 10.0,
    ) -> AutosaveSettings:
        """
        Returns autosave settings for the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetAutosaveSettings(),
            request_timeout=request_timeout,
        )

    async def set_autosave_settings(
        self,
        scope: AutosaveSettingsScope,
        settings: ScopeAutosaveSettings | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets autosave settings for the given scope. The method is guaranteed to work only after at least one call to getAutosaveSettings
        :param scope: Autosave settings scope
        :param settings: New autosave settings for the scope; pass null to set autosave settings to default
        :param request_timeout: Request timeout
        """
        return await self(
            SetAutosaveSettings(
                scope=scope,
                settings=settings,
            ),
            request_timeout=request_timeout,
        )

    async def clear_autosave_settings_exceptions(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Clears the list of all autosave settings exceptions. The method is guaranteed to work only after at least one call to getAutosaveSettings
        :param request_timeout: Request timeout
        """
        return await self(
            ClearAutosaveSettingsExceptions(),
            request_timeout=request_timeout,
        )

    async def get_bank_card_info(
        self,
        bank_card_number: str,
        request_timeout: float = 10.0,
    ) -> BankCardInfo:
        """
        Returns information about a bank card
        :param bank_card_number: The bank card number
        :param request_timeout: Request timeout
        """
        return await self(
            GetBankCardInfo(
                bank_card_number=bank_card_number,
            ),
            request_timeout=request_timeout,
        )

    async def get_passport_element(
        self,
        type: PassportElementType,
        password: str,
        request_timeout: float = 10.0,
    ) -> PassportElement:
        """
        Returns one of the available Telegram Passport elements
        :param type: Telegram Passport element type
        :param password: The 2-step verification password of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetPassportElement(
                type=type,
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def get_all_passport_elements(
        self,
        password: str,
        request_timeout: float = 10.0,
    ) -> PassportElements:
        """
        Returns all available Telegram Passport elements
        :param password: The 2-step verification password of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetAllPassportElements(
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def set_passport_element(
        self,
        element: InputPassportElement,
        password: str,
        request_timeout: float = 10.0,
    ) -> PassportElement:
        """
        Adds an element to the user's Telegram Passport. May return an error with a message 'PHONE_VERIFICATION_NEEDED' or 'EMAIL_VERIFICATION_NEEDED' if the chosen phone number or the chosen email address must be verified first
        :param element: Input Telegram Passport element
        :param password: The 2-step verification password of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            SetPassportElement(
                element=element,
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def delete_passport_element(
        self,
        type: PassportElementType,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Deletes a Telegram Passport element
        :param type: Element type
        :param request_timeout: Request timeout
        """
        return await self(
            DeletePassportElement(
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def set_passport_element_errors(
        self,
        user_id: int,
        errors: list[InputPassportElementError],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed
        :param user_id: User identifier
        :param errors: The errors
        :param request_timeout: Request timeout
        """
        return await self(
            SetPassportElementErrors(
                user_id=user_id,
                errors=errors,
            ),
            request_timeout=request_timeout,
        )

    async def get_preferred_country_language(
        self,
        country_code: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown
        :param country_code: A two-letter ISO 3166-1 alpha-2 country code
        :param request_timeout: Request timeout
        """
        return await self(
            GetPreferredCountryLanguage(
                country_code=country_code,
            ),
            request_timeout=request_timeout,
        )

    async def send_email_address_verification_code(
        self,
        email_address: str,
        request_timeout: float = 10.0,
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Sends a code to verify an email address to be added to a user's Telegram Passport
        :param email_address: Email address
        :param request_timeout: Request timeout
        """
        return await self(
            SendEmailAddressVerificationCode(
                email_address=email_address,
            ),
            request_timeout=request_timeout,
        )

    async def resend_email_address_verification_code(
        self,
        request_timeout: float = 10.0,
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Resends the code to verify an email address to be added to a user's Telegram Passport
        :param request_timeout: Request timeout
        """
        return await self(
            ResendEmailAddressVerificationCode(),
            request_timeout=request_timeout,
        )

    async def check_email_address_verification_code(
        self,
        code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks the email address verification code for Telegram Passport
        :param code: Verification code to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckEmailAddressVerificationCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def get_passport_authorization_form(
        self,
        bot_user_id: int,
        scope: str,
        public_key: str,
        nonce: str,
        request_timeout: float = 10.0,
    ) -> PassportAuthorizationForm:
        """
        Returns a Telegram Passport authorization form for sharing data with a service
        :param bot_user_id: User identifier of the service's bot
        :param scope: Telegram Passport element types requested by the service
        :param public_key: Service's public key
        :param nonce: Unique request identifier provided by the service
        :param request_timeout: Request timeout
        """
        return await self(
            GetPassportAuthorizationForm(
                bot_user_id=bot_user_id,
                scope=scope,
                public_key=public_key,
                nonce=nonce,
            ),
            request_timeout=request_timeout,
        )

    async def get_passport_authorization_form_available_elements(
        self,
        authorization_form_id: int,
        password: str,
        request_timeout: float = 10.0,
    ) -> PassportElementsWithErrors:
        """
        Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form
        :param authorization_form_id: Authorization form identifier
        :param password: The 2-step verification password of the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetPassportAuthorizationFormAvailableElements(
                authorization_form_id=authorization_form_id,
                password=password,
            ),
            request_timeout=request_timeout,
        )

    async def send_passport_authorization_form(
        self,
        authorization_form_id: int,
        types: list[PassportElementType],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused
        :param authorization_form_id: Authorization form identifier
        :param types: Types of Telegram Passport elements chosen by user to complete the authorization form
        :param request_timeout: Request timeout
        """
        return await self(
            SendPassportAuthorizationForm(
                authorization_form_id=authorization_form_id,
                types=types,
            ),
            request_timeout=request_timeout,
        )

    async def set_bot_updates_status(
        self,
        pending_update_count: int,
        error_message: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only
        :param pending_update_count: The number of pending updates
        :param error_message: The last error message
        :param request_timeout: Request timeout
        """
        return await self(
            SetBotUpdatesStatus(
                pending_update_count=pending_update_count,
                error_message=error_message,
            ),
            request_timeout=request_timeout,
        )

    async def upload_sticker_file(
        self,
        user_id: int,
        sticker_format: StickerFormat,
        sticker: InputFile,
        request_timeout: float = 10.0,
    ) -> File:
        """
        Uploads a file with a sticker; returns the uploaded file
        :param user_id: Sticker file owner; ignored for regular users
        :param sticker_format: Sticker format
        :param sticker: File file to upload; must fit in a 512x512 square. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server-side.
        :param request_timeout: Request timeout
        """
        return await self(
            UploadStickerFile(
                user_id=user_id,
                sticker_format=sticker_format,
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def get_suggested_sticker_set_name(
        self,
        title: str,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns a suggested name for a new sticker set with a given title
        :param title: Sticker set title; 1-64 characters
        :param request_timeout: Request timeout
        """
        return await self(
            GetSuggestedStickerSetName(
                title=title,
            ),
            request_timeout=request_timeout,
        )

    async def check_sticker_set_name(
        self,
        name: str,
        request_timeout: float = 10.0,
    ) -> CheckStickerSetNameResult:
        """
        Checks whether a name can be used for a new sticker set
        :param name: Name to be checked
        :param request_timeout: Request timeout
        """
        return await self(
            CheckStickerSetName(
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def create_new_sticker_set(
        self,
        user_id: int,
        title: str,
        name: str,
        sticker_type: StickerType,
        needs_repainting: bool,
        stickers: list[InputSticker],
        source: str | None = None,
        request_timeout: float = 10.0,
    ) -> StickerSet:
        """
        Creates a new sticker set. Returns the newly created sticker set
        :param user_id: Sticker set owner; ignored for regular users
        :param title: Sticker set title; 1-64 characters
        :param name: Sticker set name. Can contain only English letters, digits and underscores. Must end with *'_by_<bot username>'* (*<bot_username>* is case insensitive) for bots; 0-64 characters.
        :param sticker_type: Type of the stickers in the set
        :param needs_repainting: Pass true if stickers in the sticker set must be repainted; for custom emoji sticker sets only
        :param stickers: List of stickers to be added to the set; 1-200 stickers for custom emoji sticker sets, and 1-120 stickers otherwise. For TGS stickers, uploadStickerFile must be used before the sticker is shown
        :param source: Source of the sticker set; may be empty if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            CreateNewStickerSet(
                user_id=user_id,
                title=title,
                name=name,
                sticker_type=sticker_type,
                needs_repainting=needs_repainting,
                stickers=stickers,
                source=source,
            ),
            request_timeout=request_timeout,
        )

    async def add_sticker_to_set(
        self,
        user_id: int,
        name: str,
        sticker: InputSticker,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a new sticker to a set
        :param user_id: Sticker set owner; ignored for regular users
        :param name: Sticker set name. The sticker set must be owned by the current user, and contain less than 200 stickers for custom emoji sticker sets and less than 120 otherwise
        :param sticker: Sticker to add to the set
        :param request_timeout: Request timeout
        """
        return await self(
            AddStickerToSet(
                user_id=user_id,
                name=name,
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def replace_sticker_in_set(
        self,
        user_id: int,
        name: str,
        old_sticker: InputFile,
        new_sticker: InputSticker,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Replaces existing sticker in a set. The function is equivalent to removeStickerFromSet, then addStickerToSet, then setStickerPositionInSet
        :param user_id: Sticker set owner; ignored for regular users
        :param name: Sticker set name. The sticker set must be owned by the current user
        :param old_sticker: Sticker to remove from the set
        :param new_sticker: Sticker to add to the set
        :param request_timeout: Request timeout
        """
        return await self(
            ReplaceStickerInSet(
                user_id=user_id,
                name=name,
                old_sticker=old_sticker,
                new_sticker=new_sticker,
            ),
            request_timeout=request_timeout,
        )

    async def set_sticker_set_thumbnail(
        self,
        user_id: int,
        name: str,
        thumbnail: InputFile | None = None,
        format: StickerFormat | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets a sticker set thumbnail
        :param user_id: Sticker set owner; ignored for regular users
        :param name: Sticker set name. The sticker set must be owned by the current user
        :param thumbnail: Thumbnail to set; pass null to remove the sticker set thumbnail
        :param format: Format of the thumbnail; pass null if thumbnail is removed
        :param request_timeout: Request timeout
        """
        return await self(
            SetStickerSetThumbnail(
                user_id=user_id,
                name=name,
                thumbnail=thumbnail,
                format=format,
            ),
            request_timeout=request_timeout,
        )

    async def set_custom_emoji_sticker_set_thumbnail(
        self,
        name: str,
        custom_emoji_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets a custom emoji sticker set thumbnail
        :param name: Sticker set name. The sticker set must be owned by the current user
        :param custom_emoji_id: Identifier of the custom emoji from the sticker set, which will be set as sticker set thumbnail; pass 0 to remove the sticker set thumbnail
        :param request_timeout: Request timeout
        """
        return await self(
            SetCustomEmojiStickerSetThumbnail(
                name=name,
                custom_emoji_id=custom_emoji_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_sticker_set_title(
        self,
        name: str,
        title: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets a sticker set title
        :param name: Sticker set name. The sticker set must be owned by the current user
        :param title: New sticker set title
        :param request_timeout: Request timeout
        """
        return await self(
            SetStickerSetTitle(
                name=name,
                title=title,
            ),
            request_timeout=request_timeout,
        )

    async def delete_sticker_set(
        self,
        name: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Completely deletes a sticker set
        :param name: Sticker set name. The sticker set must be owned by the current user
        :param request_timeout: Request timeout
        """
        return await self(
            DeleteStickerSet(
                name=name,
            ),
            request_timeout=request_timeout,
        )

    async def set_sticker_position_in_set(
        self,
        sticker: InputFile,
        position: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the position of a sticker in the set to which it belongs. The sticker set must be owned by the current user
        :param sticker: Sticker
        :param position: New position of the sticker in the set, 0-based
        :param request_timeout: Request timeout
        """
        return await self(
            SetStickerPositionInSet(
                sticker=sticker,
                position=position,
            ),
            request_timeout=request_timeout,
        )

    async def remove_sticker_from_set(
        self,
        sticker: InputFile,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a sticker from the set to which it belongs. The sticker set must be owned by the current user
        :param sticker: Sticker to remove from the set
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveStickerFromSet(
                sticker=sticker,
            ),
            request_timeout=request_timeout,
        )

    async def set_sticker_emojis(
        self,
        sticker: InputFile,
        emojis: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the list of emojis corresponding to a sticker. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user
        :param sticker: Sticker
        :param emojis: New string with 1-20 emoji corresponding to the sticker
        :param request_timeout: Request timeout
        """
        return await self(
            SetStickerEmojis(
                sticker=sticker,
                emojis=emojis,
            ),
            request_timeout=request_timeout,
        )

    async def set_sticker_keywords(
        self,
        sticker: InputFile,
        keywords: list[str],
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the list of keywords of a sticker. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user
        :param sticker: Sticker
        :param keywords: List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker
        :param request_timeout: Request timeout
        """
        return await self(
            SetStickerKeywords(
                sticker=sticker,
                keywords=keywords,
            ),
            request_timeout=request_timeout,
        )

    async def set_sticker_mask_position(
        self,
        sticker: InputFile,
        mask_position: MaskPosition | None = None,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Changes the mask position of a mask sticker. The sticker must belong to a mask sticker set that is owned by the current user
        :param sticker: Sticker
        :param mask_position: Position where the mask is placed; pass null to remove mask position
        :param request_timeout: Request timeout
        """
        return await self(
            SetStickerMaskPosition(
                sticker=sticker,
                mask_position=mask_position,
            ),
            request_timeout=request_timeout,
        )

    async def get_owned_sticker_sets(
        self,
        offset_sticker_set_id: int,
        limit: int,
        request_timeout: float = 10.0,
    ) -> StickerSets:
        """
        Returns sticker sets owned by the current user
        :param offset_sticker_set_id: Identifier of the sticker set from which to return owned sticker sets; use 0 to get results from the beginning
        :param limit: The maximum number of sticker sets to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit
        :param request_timeout: Request timeout
        """
        return await self(
            GetOwnedStickerSets(
                offset_sticker_set_id=offset_sticker_set_id,
                limit=limit,
            ),
            request_timeout=request_timeout,
        )

    async def get_map_thumbnail_file(
        self,
        location: Location,
        zoom: int,
        width: int,
        height: int,
        scale: int,
        chat_id: int,
        request_timeout: float = 10.0,
    ) -> File:
        """
        Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded
        :param location: Location of the map center
        :param zoom: Map zoom level; 13-20
        :param width: Map width in pixels before applying scale; 16-1024
        :param height: Map height in pixels before applying scale; 16-1024
        :param scale: Map scale; 1-3
        :param chat_id: Identifier of a chat in which the thumbnail will be shown. Use 0 if unknown
        :param request_timeout: Request timeout
        """
        return await self(
            GetMapThumbnailFile(
                location=location,
                zoom=zoom,
                width=width,
                height=height,
                scale=scale,
                chat_id=chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_premium_limit(
        self,
        limit_type: PremiumLimitType,
        request_timeout: float = 10.0,
    ) -> PremiumLimit:
        """
        Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown
        :param limit_type: Type of the limit
        :param request_timeout: Request timeout
        """
        return await self(
            GetPremiumLimit(
                limit_type=limit_type,
            ),
            request_timeout=request_timeout,
        )

    async def get_premium_features(
        self,
        source: PremiumSource | None = None,
        request_timeout: float = 10.0,
    ) -> PremiumFeatures:
        """
        Returns information about features, available to Premium users
        :param source: Source of the request; pass null if the method is called from some non-standard source
        :param request_timeout: Request timeout
        """
        return await self(
            GetPremiumFeatures(
                source=source,
            ),
            request_timeout=request_timeout,
        )

    async def get_premium_sticker_examples(
        self,
        request_timeout: float = 10.0,
    ) -> Stickers:
        """
        Returns examples of premium stickers for demonstration purposes
        :param request_timeout: Request timeout
        """
        return await self(
            GetPremiumStickerExamples(),
            request_timeout=request_timeout,
        )

    async def view_premium_feature(
        self,
        feature: PremiumFeature,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen
        :param feature: The viewed premium feature
        :param request_timeout: Request timeout
        """
        return await self(
            ViewPremiumFeature(
                feature=feature,
            ),
            request_timeout=request_timeout,
        )

    async def click_premium_subscription_button(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs TDLib that the user clicked Premium subscription button on the Premium features screen
        :param request_timeout: Request timeout
        """
        return await self(
            ClickPremiumSubscriptionButton(),
            request_timeout=request_timeout,
        )

    async def get_premium_state(
        self,
        request_timeout: float = 10.0,
    ) -> PremiumState:
        """
        Returns state of Telegram Premium subscription and promotion videos for Premium features
        :param request_timeout: Request timeout
        """
        return await self(
            GetPremiumState(),
            request_timeout=request_timeout,
        )

    async def get_premium_gift_code_payment_options(
        self,
        boosted_chat_id: int,
        request_timeout: float = 10.0,
    ) -> PremiumGiftCodePaymentOptions:
        """
        Returns available options for Telegram Premium gift code or giveaway creation
        :param boosted_chat_id: Identifier of the supergroup or channel chat, which will be automatically boosted by receivers of the gift codes and which is administered by the user; 0 if none
        :param request_timeout: Request timeout
        """
        return await self(
            GetPremiumGiftCodePaymentOptions(
                boosted_chat_id=boosted_chat_id,
            ),
            request_timeout=request_timeout,
        )

    async def check_premium_gift_code(
        self,
        code: str,
        request_timeout: float = 10.0,
    ) -> PremiumGiftCodeInfo:
        """
        Return information about a Telegram Premium gift code
        :param code: The code to check
        :param request_timeout: Request timeout
        """
        return await self(
            CheckPremiumGiftCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def apply_premium_gift_code(
        self,
        code: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Applies a Telegram Premium gift code
        :param code: The code to apply
        :param request_timeout: Request timeout
        """
        return await self(
            ApplyPremiumGiftCode(
                code=code,
            ),
            request_timeout=request_timeout,
        )

    async def launch_prepaid_premium_giveaway(
        self,
        giveaway_id: int,
        parameters: PremiumGiveawayParameters,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Launches a prepaid Telegram Premium giveaway
        :param giveaway_id: Unique identifier of the prepaid giveaway
        :param parameters: Giveaway parameters
        :param request_timeout: Request timeout
        """
        return await self(
            LaunchPrepaidPremiumGiveaway(
                giveaway_id=giveaway_id,
                parameters=parameters,
            ),
            request_timeout=request_timeout,
        )

    async def get_premium_giveaway_info(
        self,
        chat_id: int,
        message_id: int,
        request_timeout: float = 10.0,
    ) -> PremiumGiveawayInfo:
        """
        Returns information about a Telegram Premium giveaway
        :param chat_id: Identifier of the channel chat which started the giveaway
        :param message_id: Identifier of the giveaway or a giveaway winners message in the chat
        :param request_timeout: Request timeout
        """
        return await self(
            GetPremiumGiveawayInfo(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_star_payment_options(
        self,
        request_timeout: float = 10.0,
    ) -> StarPaymentOptions:
        """
        Returns available options for Telegram Stars purchase
        :param request_timeout: Request timeout
        """
        return await self(
            GetStarPaymentOptions(),
            request_timeout=request_timeout,
        )

    async def get_star_gift_payment_options(
        self,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> StarPaymentOptions:
        """
        Returns available options for Telegram Stars gifting
        :param user_id: Identifier of the user that will receive Telegram Stars; pass 0 to get options for an unspecified user
        :param request_timeout: Request timeout
        """
        return await self(
            GetStarGiftPaymentOptions(
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_star_transactions(
        self,
        owner_id: MessageSender,
        offset: str,
        limit: int,
        subscription_id: str | None = None,
        direction: StarTransactionDirection | None = None,
        request_timeout: float = 10.0,
    ) -> StarTransactions:
        """
        Returns the list of Telegram Star transactions for the specified owner
        :param owner_id: Identifier of the owner of the Telegram Stars; can be the identifier of the current user, identifier of an owned bot,
        :param offset: Offset of the first transaction to return as received from the previous request; use empty string to get the first chunk of results
        :param limit: The maximum number of transactions to return
        :param subscription_id: If non-empty, only transactions related to the Star Subscription will be returned
        :param direction: Direction of the transactions to receive; pass null to get all transactions
        :param request_timeout: Request timeout
        """
        return await self(
            GetStarTransactions(
                owner_id=owner_id,
                offset=offset,
                limit=limit,
                subscription_id=subscription_id,
                direction=direction,
            ),
            request_timeout=request_timeout,
        )

    async def get_star_subscriptions(
        self,
        only_expiring: bool,
        offset: str,
        request_timeout: float = 10.0,
    ) -> StarSubscriptions:
        """
        Returns the list of Telegram Star subscriptions for the current user
        :param only_expiring: Pass true to receive only expiring subscriptions for which there are no enough Telegram Stars to extend
        :param offset: Offset of the first subscription to return as received from the previous request; use empty string to get the first chunk of results
        :param request_timeout: Request timeout
        """
        return await self(
            GetStarSubscriptions(
                only_expiring=only_expiring,
                offset=offset,
            ),
            request_timeout=request_timeout,
        )

    async def can_purchase_from_store(
        self,
        purpose: StorePaymentPurpose,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Checks whether an in-store purchase is possible. Must be called before any in-store purchase
        :param purpose: Transaction purpose
        :param request_timeout: Request timeout
        """
        return await self(
            CanPurchaseFromStore(
                purpose=purpose,
            ),
            request_timeout=request_timeout,
        )

    async def assign_app_store_transaction(
        self,
        receipt: bytes,
        purpose: StorePaymentPurpose,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs server about a purchase through App Store. For official applications only
        :param receipt: App Store receipt
        :param purpose: Transaction purpose
        :param request_timeout: Request timeout
        """
        return await self(
            AssignAppStoreTransaction(
                receipt=receipt,
                purpose=purpose,
            ),
            request_timeout=request_timeout,
        )

    async def assign_google_play_transaction(
        self,
        package_name: str,
        store_product_id: str,
        purchase_token: str,
        purpose: StorePaymentPurpose,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Informs server about a purchase through Google Play. For official applications only
        :param package_name: Application package name
        :param store_product_id: Identifier of the purchased store product
        :param purchase_token: Google Play purchase token
        :param purpose: Transaction purpose
        :param request_timeout: Request timeout
        """
        return await self(
            AssignGooglePlayTransaction(
                package_name=package_name,
                store_product_id=store_product_id,
                purchase_token=purchase_token,
                purpose=purpose,
            ),
            request_timeout=request_timeout,
        )

    async def edit_star_subscription(
        self,
        subscription_id: str,
        is_canceled: bool,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Cancels or reenables Telegram Star subscription to a channel
        :param subscription_id: Identifier of the subscription to change
        :param is_canceled: New value of is_canceled
        :param request_timeout: Request timeout
        """
        return await self(
            EditStarSubscription(
                subscription_id=subscription_id,
                is_canceled=is_canceled,
            ),
            request_timeout=request_timeout,
        )

    async def reuse_star_subscription(
        self,
        subscription_id: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Reuses an active subscription and joins the subscribed chat again
        :param subscription_id: Identifier of the subscription
        :param request_timeout: Request timeout
        """
        return await self(
            ReuseStarSubscription(
                subscription_id=subscription_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_business_features(
        self,
        source: BusinessFeature | None = None,
        request_timeout: float = 10.0,
    ) -> BusinessFeatures:
        """
        Returns information about features, available to Business users
        :param source: Source of the request; pass null if the method is called from settings or some non-standard source
        :param request_timeout: Request timeout
        """
        return await self(
            GetBusinessFeatures(
                source=source,
            ),
            request_timeout=request_timeout,
        )

    async def accept_terms_of_service(
        self,
        terms_of_service_id: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Accepts Telegram terms of services
        :param terms_of_service_id: Terms of service identifier
        :param request_timeout: Request timeout
        """
        return await self(
            AcceptTermsOfService(
                terms_of_service_id=terms_of_service_id,
            ),
            request_timeout=request_timeout,
        )

    async def search_strings_by_prefix(
        self,
        strings: list[str],
        query: str,
        limit: int,
        return_none_for_empty_query: bool,
        request_timeout: float = 10.0,
    ) -> FoundPositions:
        """
        Searches specified query by word prefixes in the provided strings. Returns 0-based positions of strings that matched. Can be called synchronously
        :param strings: The strings to search in for the query
        :param query: Query to search for
        :param limit: The maximum number of objects to return
        :param return_none_for_empty_query: Pass true to receive no results for an empty query
        :param request_timeout: Request timeout
        """
        return await self(
            SearchStringsByPrefix(
                strings=strings,
                query=query,
                limit=limit,
                return_none_for_empty_query=return_none_for_empty_query,
            ),
            request_timeout=request_timeout,
        )

    async def send_custom_request(
        self,
        method: str,
        parameters: str,
        request_timeout: float = 10.0,
    ) -> CustomRequestResult:
        """
        Sends a custom request; for bots only
        :param method: The method name
        :param parameters: JSON-serialized method parameters
        :param request_timeout: Request timeout
        """
        return await self(
            SendCustomRequest(
                method=method,
                parameters=parameters,
            ),
            request_timeout=request_timeout,
        )

    async def answer_custom_query(
        self,
        custom_query_id: int,
        data: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Answers a custom query; for bots only
        :param custom_query_id: Identifier of a custom query
        :param data: JSON-serialized answer to the query
        :param request_timeout: Request timeout
        """
        return await self(
            AnswerCustomQuery(
                custom_query_id=custom_query_id,
                data=data,
            ),
            request_timeout=request_timeout,
        )

    async def set_alarm(
        self,
        seconds: float,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Succeeds after a specified amount of time has passed. Can be called before initialization
        :param seconds: Number of seconds before the function returns
        :param request_timeout: Request timeout
        """
        return await self(
            SetAlarm(
                seconds=seconds,
            ),
            request_timeout=request_timeout,
        )

    async def get_countries(
        self,
        request_timeout: float = 10.0,
    ) -> Countries:
        """
        Returns information about existing countries. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            GetCountries(),
            request_timeout=request_timeout,
        )

    async def get_country_code(
        self,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Uses the current IP address to find the current country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            GetCountryCode(),
            request_timeout=request_timeout,
        )

    async def get_phone_number_info(
        self,
        phone_number_prefix: str,
        request_timeout: float = 10.0,
    ) -> PhoneNumberInfo:
        """
        Returns information about a phone number by its prefix. Can be called before authorization
        :param phone_number_prefix: The phone number prefix
        :param request_timeout: Request timeout
        """
        return await self(
            GetPhoneNumberInfo(
                phone_number_prefix=phone_number_prefix,
            ),
            request_timeout=request_timeout,
        )

    async def get_phone_number_info_sync(
        self,
        language_code: str,
        phone_number_prefix: str,
        request_timeout: float = 10.0,
    ) -> PhoneNumberInfo:
        """
        Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously
        :param language_code: A two-letter ISO 639-1 language code for country information localization
        :param phone_number_prefix: The phone number prefix
        :param request_timeout: Request timeout
        """
        return await self(
            GetPhoneNumberInfoSync(
                language_code=language_code,
                phone_number_prefix=phone_number_prefix,
            ),
            request_timeout=request_timeout,
        )

    async def get_collectible_item_info(
        self,
        type: CollectibleItemType,
        request_timeout: float = 10.0,
    ) -> CollectibleItemInfo:
        """
        Returns information about a given collectible item that was purchased at https://fragment.com
        :param type: Type of the collectible item. The item must be used by a user and must be visible to the current user
        :param request_timeout: Request timeout
        """
        return await self(
            GetCollectibleItemInfo(
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def get_deep_link_info(
        self,
        link: str,
        request_timeout: float = 10.0,
    ) -> DeepLinkInfo:
        """
        Returns information about a tg:// deep link. Use 'tg://need_update_for_some_feature' or 'tg:some_unsupported_feature' for testing. Returns a 404 error for unknown links. Can be called before authorization
        :param link: The link
        :param request_timeout: Request timeout
        """
        return await self(
            GetDeepLinkInfo(
                link=link,
            ),
            request_timeout=request_timeout,
        )

    async def get_application_config(
        self,
        request_timeout: float = 10.0,
    ) -> JsonValue:
        """
        Returns application config, provided by the server. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            GetApplicationConfig(),
            request_timeout=request_timeout,
        )

    async def save_application_log_event(
        self,
        type: str,
        chat_id: int,
        data: JsonValue,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Saves application log event on the server. Can be called before authorization
        :param type: Event type
        :param chat_id: Optional chat identifier, associated with the event
        :param data: The log event data
        :param request_timeout: Request timeout
        """
        return await self(
            SaveApplicationLogEvent(
                type=type,
                chat_id=chat_id,
                data=data,
            ),
            request_timeout=request_timeout,
        )

    async def get_application_download_link(
        self,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram
        :param request_timeout: Request timeout
        """
        return await self(
            GetApplicationDownloadLink(),
            request_timeout=request_timeout,
        )

    async def add_proxy(
        self,
        server: str,
        port: int,
        enable: bool,
        type: ProxyType,
        request_timeout: float = 10.0,
    ) -> Proxy:
        """
        Adds a proxy server for network requests. Can be called before authorization
        :param server: Proxy server domain or IP address
        :param port: Proxy server port
        :param enable: Pass true to immediately enable the proxy
        :param type: Proxy type
        :param request_timeout: Request timeout
        """
        return await self(
            AddProxy(
                server=server,
                port=port,
                enable=enable,
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def edit_proxy(
        self,
        proxy_id: int,
        server: str,
        port: int,
        enable: bool,
        type: ProxyType,
        request_timeout: float = 10.0,
    ) -> Proxy:
        """
        Edits an existing proxy server for network requests. Can be called before authorization
        :param proxy_id: Proxy identifier
        :param server: Proxy server domain or IP address
        :param port: Proxy server port
        :param enable: Pass true to immediately enable the proxy
        :param type: Proxy type
        :param request_timeout: Request timeout
        """
        return await self(
            EditProxy(
                proxy_id=proxy_id,
                server=server,
                port=port,
                enable=enable,
                type=type,
            ),
            request_timeout=request_timeout,
        )

    async def enable_proxy(
        self,
        proxy_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Enables a proxy. Only one proxy can be enabled at a time. Can be called before authorization
        :param proxy_id: Proxy identifier
        :param request_timeout: Request timeout
        """
        return await self(
            EnableProxy(
                proxy_id=proxy_id,
            ),
            request_timeout=request_timeout,
        )

    async def disable_proxy(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Disables the currently enabled proxy. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            DisableProxy(),
            request_timeout=request_timeout,
        )

    async def remove_proxy(
        self,
        proxy_id: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Removes a proxy server. Can be called before authorization
        :param proxy_id: Proxy identifier
        :param request_timeout: Request timeout
        """
        return await self(
            RemoveProxy(
                proxy_id=proxy_id,
            ),
            request_timeout=request_timeout,
        )

    async def get_proxies(
        self,
        request_timeout: float = 10.0,
    ) -> Proxies:
        """
        Returns the list of proxies that are currently set up. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            GetProxies(),
            request_timeout=request_timeout,
        )

    async def get_proxy_link(
        self,
        proxy_id: int,
        request_timeout: float = 10.0,
    ) -> HttpUrl:
        """
        Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization
        :param proxy_id: Proxy identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetProxyLink(
                proxy_id=proxy_id,
            ),
            request_timeout=request_timeout,
        )

    async def ping_proxy(
        self,
        proxy_id: int,
        request_timeout: float = 10.0,
    ) -> Seconds:
        """
        Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization
        :param proxy_id: Proxy identifier. Use 0 to ping a Telegram server without a proxy
        :param request_timeout: Request timeout
        """
        return await self(
            PingProxy(
                proxy_id=proxy_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_log_stream(
        self,
        log_stream: LogStream,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets new log stream for internal logging of TDLib. Can be called synchronously
        :param log_stream: New log stream
        :param request_timeout: Request timeout
        """
        return await self(
            SetLogStream(
                log_stream=log_stream,
            ),
            request_timeout=request_timeout,
        )

    async def get_log_stream(
        self,
        request_timeout: float = 10.0,
    ) -> LogStream:
        """
        Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
        :param request_timeout: Request timeout
        """
        return await self(
            GetLogStream(),
            request_timeout=request_timeout,
        )

    async def set_log_verbosity_level(
        self,
        new_verbosity_level: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the verbosity level of the internal logging of TDLib. Can be called synchronously
        :param new_verbosity_level: New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings,
        :param request_timeout: Request timeout
        """
        return await self(
            SetLogVerbosityLevel(
                new_verbosity_level=new_verbosity_level,
            ),
            request_timeout=request_timeout,
        )

    async def get_log_verbosity_level(
        self,
        request_timeout: float = 10.0,
    ) -> LogVerbosityLevel:
        """
        Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
        :param request_timeout: Request timeout
        """
        return await self(
            GetLogVerbosityLevel(),
            request_timeout=request_timeout,
        )

    async def get_log_tags(
        self,
        request_timeout: float = 10.0,
    ) -> LogTags:
        """
        Returns the list of available TDLib internal log tags, for example, ['actor', 'binlog', 'connections', 'notifications', 'proxy']. Can be called synchronously
        :param request_timeout: Request timeout
        """
        return await self(
            GetLogTags(),
            request_timeout=request_timeout,
        )

    async def set_log_tag_verbosity_level(
        self,
        tag: str,
        new_verbosity_level: int,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously
        :param tag: Logging tag to change verbosity level
        :param new_verbosity_level: New verbosity level; 1-1024
        :param request_timeout: Request timeout
        """
        return await self(
            SetLogTagVerbosityLevel(
                tag=tag,
                new_verbosity_level=new_verbosity_level,
            ),
            request_timeout=request_timeout,
        )

    async def get_log_tag_verbosity_level(
        self,
        tag: str,
        request_timeout: float = 10.0,
    ) -> LogVerbosityLevel:
        """
        Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously
        :param tag: Logging tag to change verbosity level
        :param request_timeout: Request timeout
        """
        return await self(
            GetLogTagVerbosityLevel(
                tag=tag,
            ),
            request_timeout=request_timeout,
        )

    async def add_log_message(
        self,
        verbosity_level: int,
        text: str,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Adds a message to TDLib internal log. Can be called synchronously
        :param verbosity_level: The minimum verbosity level needed for the message to be logged; 0-1023
        :param text: Text of a message to log
        :param request_timeout: Request timeout
        """
        return await self(
            AddLogMessage(
                verbosity_level=verbosity_level,
                text=text,
            ),
            request_timeout=request_timeout,
        )

    async def get_user_support_info(
        self,
        user_id: int,
        request_timeout: float = 10.0,
    ) -> UserSupportInfo:
        """
        Returns support information for the given user; for Telegram support only
        :param user_id: User identifier
        :param request_timeout: Request timeout
        """
        return await self(
            GetUserSupportInfo(
                user_id=user_id,
            ),
            request_timeout=request_timeout,
        )

    async def set_user_support_info(
        self,
        user_id: int,
        message: FormattedText,
        request_timeout: float = 10.0,
    ) -> UserSupportInfo:
        """
        Sets support information for the given user; for Telegram support only
        :param user_id: User identifier
        :param message: New information message
        :param request_timeout: Request timeout
        """
        return await self(
            SetUserSupportInfo(
                user_id=user_id,
                message=message,
            ),
            request_timeout=request_timeout,
        )

    async def get_support_name(
        self,
        request_timeout: float = 10.0,
    ) -> Text:
        """
        Returns localized name of the Telegram support user; for Telegram support only
        :param request_timeout: Request timeout
        """
        return await self(
            GetSupportName(),
            request_timeout=request_timeout,
        )

    async def test_call_empty(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Does nothing; for testing only. This is an offline method. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            TestCallEmpty(),
            request_timeout=request_timeout,
        )

    async def test_call_string(
        self,
        x: str,
        request_timeout: float = 10.0,
    ) -> TestString:
        """
        Returns the received string; for testing only. This is an offline method. Can be called before authorization
        :param x: String to return
        :param request_timeout: Request timeout
        """
        return await self(
            TestCallString(
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def test_call_bytes(
        self,
        x: bytes,
        request_timeout: float = 10.0,
    ) -> TestBytes:
        """
        Returns the received bytes; for testing only. This is an offline method. Can be called before authorization
        :param x: Bytes to return
        :param request_timeout: Request timeout
        """
        return await self(
            TestCallBytes(
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def test_call_vector_int(
        self,
        x: list[int],
        request_timeout: float = 10.0,
    ) -> TestVectorInt:
        """
        Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization
        :param x: Vector of numbers to return
        :param request_timeout: Request timeout
        """
        return await self(
            TestCallVectorInt(
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def test_call_vector_int_object(
        self,
        x: list[TestInt],
        request_timeout: float = 10.0,
    ) -> TestVectorIntObject:
        """
        Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization
        :param x: Vector of objects to return
        :param request_timeout: Request timeout
        """
        return await self(
            TestCallVectorIntObject(
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def test_call_vector_string(
        self,
        x: list[str],
        request_timeout: float = 10.0,
    ) -> TestVectorString:
        """
        Returns the received vector of strings; for testing only. This is an offline method. Can be called before authorization
        :param x: Vector of strings to return
        :param request_timeout: Request timeout
        """
        return await self(
            TestCallVectorString(
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def test_call_vector_string_object(
        self,
        x: list[TestString],
        request_timeout: float = 10.0,
    ) -> TestVectorStringObject:
        """
        Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization
        :param x: Vector of objects to return
        :param request_timeout: Request timeout
        """
        return await self(
            TestCallVectorStringObject(
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def test_square_int(
        self,
        x: int,
        request_timeout: float = 10.0,
    ) -> TestInt:
        """
        Returns the squared received number; for testing only. This is an offline method. Can be called before authorization
        :param x: Number to square
        :param request_timeout: Request timeout
        """
        return await self(
            TestSquareInt(
                x=x,
            ),
            request_timeout=request_timeout,
        )

    async def test_network(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            TestNetwork(),
            request_timeout=request_timeout,
        )

    async def test_proxy(
        self,
        server: str,
        port: int,
        type: ProxyType,
        dc_id: int,
        timeout: float,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization
        :param server: Proxy server domain or IP address
        :param port: Proxy server port
        :param type: Proxy type
        :param dc_id: Identifier of a datacenter with which to test connection
        :param timeout: The maximum overall timeout for the request
        :param request_timeout: Request timeout
        """
        return await self(
            TestProxy(
                server=server,
                port=port,
                type=type,
                dc_id=dc_id,
                timeout=timeout,
            ),
            request_timeout=request_timeout,
        )

    async def test_get_difference(
        self,
        request_timeout: float = 10.0,
    ) -> Ok:
        """
        Forces an updates.getDifference call to the Telegram servers; for testing only
        :param request_timeout: Request timeout
        """
        return await self(
            TestGetDifference(),
            request_timeout=request_timeout,
        )

    async def test_use_update(
        self,
        request_timeout: float = 10.0,
    ) -> Update:
        """
        Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization
        :param request_timeout: Request timeout
        """
        return await self(
            TestUseUpdate(),
            request_timeout=request_timeout,
        )

    async def test_return_error(
        self,
        error: Error,
        request_timeout: float = 10.0,
    ) -> Error:
        """
        Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously
        :param error: The error to be returned
        :param request_timeout: Request timeout
        """
        return await self(
            TestReturnError(
                error=error,
            ),
            request_timeout=request_timeout,
        )
