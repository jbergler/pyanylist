from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListItem(_message.Message):
    __slots__ = ["category", "categoryAssignments", "categoryMatchId", "checked", "deprecatedQuantity", "details", "eventId", "identifier", "ingredients", "itemPackageSizeShouldOverrideIngredientPackageSize", "itemQuantityShouldOverrideIngredientQuantity", "listId", "manualSortIndex", "name", "packageSizePb", "photoIds", "priceId", "priceMatchupTag", "pricePackageSizePb", "pricePackageSizeShouldOverrideItemPackageSize", "priceQuantityPb", "priceQuantityShouldOverrideItemQuantity", "prices", "productUpc", "quantityPb", "rawIngredient", "recipeId", "serverModTime", "storeIds", "userId"]
    CATEGORYASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    CATEGORYMATCHID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CHECKED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    ITEMPACKAGESIZESHOULDOVERRIDEINGREDIENTPACKAGESIZE_FIELD_NUMBER: _ClassVar[int]
    ITEMQUANTITYSHOULDOVERRIDEINGREDIENTQUANTITY_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    MANUALSORTINDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGESIZEPB_FIELD_NUMBER: _ClassVar[int]
    PHOTOIDS_FIELD_NUMBER: _ClassVar[int]
    PRICEID_FIELD_NUMBER: _ClassVar[int]
    PRICEMATCHUPTAG_FIELD_NUMBER: _ClassVar[int]
    PRICEPACKAGESIZEPB_FIELD_NUMBER: _ClassVar[int]
    PRICEPACKAGESIZESHOULDOVERRIDEITEMPACKAGESIZE_FIELD_NUMBER: _ClassVar[int]
    PRICEQUANTITYPB_FIELD_NUMBER: _ClassVar[int]
    PRICEQUANTITYSHOULDOVERRIDEITEMQUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    PRODUCTUPC_FIELD_NUMBER: _ClassVar[int]
    QUANTITYPB_FIELD_NUMBER: _ClassVar[int]
    RAWINGREDIENT_FIELD_NUMBER: _ClassVar[int]
    RECIPEID_FIELD_NUMBER: _ClassVar[int]
    SERVERMODTIME_FIELD_NUMBER: _ClassVar[int]
    STOREIDS_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    category: str
    categoryAssignments: _containers.RepeatedCompositeFieldContainer[PBListItemCategoryAssignment]
    categoryMatchId: str
    checked: bool
    deprecatedQuantity: str
    details: str
    eventId: str
    identifier: str
    ingredients: _containers.RepeatedCompositeFieldContainer[PBItemIngredient]
    itemPackageSizeShouldOverrideIngredientPackageSize: bool
    itemQuantityShouldOverrideIngredientQuantity: bool
    listId: str
    manualSortIndex: int
    name: str
    packageSizePb: PBItemPackageSize
    photoIds: _containers.RepeatedScalarFieldContainer[str]
    priceId: str
    priceMatchupTag: str
    pricePackageSizePb: PBItemPackageSize
    pricePackageSizeShouldOverrideItemPackageSize: bool
    priceQuantityPb: PBItemQuantity
    priceQuantityShouldOverrideItemQuantity: bool
    prices: _containers.RepeatedCompositeFieldContainer[PBItemPrice]
    productUpc: str
    quantityPb: PBItemQuantity
    rawIngredient: str
    recipeId: str
    serverModTime: float
    storeIds: _containers.RepeatedScalarFieldContainer[str]
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., serverModTime: _Optional[float] = ..., listId: _Optional[str] = ..., name: _Optional[str] = ..., details: _Optional[str] = ..., checked: bool = ..., recipeId: _Optional[str] = ..., rawIngredient: _Optional[str] = ..., priceMatchupTag: _Optional[str] = ..., priceId: _Optional[str] = ..., category: _Optional[str] = ..., userId: _Optional[str] = ..., categoryMatchId: _Optional[str] = ..., photoIds: _Optional[_Iterable[str]] = ..., eventId: _Optional[str] = ..., storeIds: _Optional[_Iterable[str]] = ..., prices: _Optional[_Iterable[_Union[PBItemPrice, _Mapping]]] = ..., categoryAssignments: _Optional[_Iterable[_Union[PBListItemCategoryAssignment, _Mapping]]] = ..., quantityPb: _Optional[_Union[PBItemQuantity, _Mapping]] = ..., priceQuantityPb: _Optional[_Union[PBItemQuantity, _Mapping]] = ..., priceQuantityShouldOverrideItemQuantity: bool = ..., packageSizePb: _Optional[_Union[PBItemPackageSize, _Mapping]] = ..., pricePackageSizePb: _Optional[_Union[PBItemPackageSize, _Mapping]] = ..., pricePackageSizeShouldOverrideItemPackageSize: bool = ..., ingredients: _Optional[_Iterable[_Union[PBItemIngredient, _Mapping]]] = ..., itemQuantityShouldOverrideIngredientQuantity: bool = ..., itemPackageSizeShouldOverrideIngredientPackageSize: bool = ..., productUpc: _Optional[str] = ..., manualSortIndex: _Optional[int] = ..., deprecatedQuantity: _Optional[str] = ...) -> None: ...

class PBAccountChangePasswordResponse(_message.Message):
    __slots__ = ["accessToken", "errorMessage", "errorTitle", "refreshToken", "statusCode"]
    ACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORTITLE_FIELD_NUMBER: _ClassVar[int]
    REFRESHTOKEN_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    accessToken: str
    errorMessage: str
    errorTitle: str
    refreshToken: str
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., errorTitle: _Optional[str] = ..., errorMessage: _Optional[str] = ..., refreshToken: _Optional[str] = ..., accessToken: _Optional[str] = ...) -> None: ...

class PBAccountInfoResponse(_message.Message):
    __slots__ = ["email", "expirationTimestampMs", "expirationTimestampMsStr", "firstName", "icalendarId", "isPremiumUser", "lastName", "masterUser", "statusCode", "subscriptionIsCanceled", "subscriptionIsPendingDowngrade", "subscriptionManagementSystem", "subscriptionType", "subusers"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIMESTAMPMSSTR_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    ICALENDARID_FIELD_NUMBER: _ClassVar[int]
    ISPREMIUMUSER_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    MASTERUSER_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONISCANCELED_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONISPENDINGDOWNGRADE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONMANAGEMENTSYSTEM_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    SUBUSERS_FIELD_NUMBER: _ClassVar[int]
    email: str
    expirationTimestampMs: int
    expirationTimestampMsStr: str
    firstName: str
    icalendarId: str
    isPremiumUser: bool
    lastName: str
    masterUser: PBEmailUserIDPair
    statusCode: int
    subscriptionIsCanceled: bool
    subscriptionIsPendingDowngrade: bool
    subscriptionManagementSystem: int
    subscriptionType: int
    subusers: _containers.RepeatedCompositeFieldContainer[PBEmailUserIDPair]
    def __init__(self, statusCode: _Optional[int] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., email: _Optional[str] = ..., isPremiumUser: bool = ..., subscriptionType: _Optional[int] = ..., subscriptionManagementSystem: _Optional[int] = ..., expirationTimestampMsStr: _Optional[str] = ..., expirationTimestampMs: _Optional[int] = ..., masterUser: _Optional[_Union[PBEmailUserIDPair, _Mapping]] = ..., subusers: _Optional[_Iterable[_Union[PBEmailUserIDPair, _Mapping]]] = ..., subscriptionIsCanceled: bool = ..., subscriptionIsPendingDowngrade: bool = ..., icalendarId: _Optional[str] = ...) -> None: ...

class PBAlexaList(_message.Message):
    __slots__ = ["alexaListId", "alexaUserId", "anylistListId", "identifier", "items", "name", "state", "version"]
    ALEXALISTID_FIELD_NUMBER: _ClassVar[int]
    ALEXAUSERID_FIELD_NUMBER: _ClassVar[int]
    ANYLISTLISTID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    alexaListId: str
    alexaUserId: str
    anylistListId: str
    identifier: str
    items: _containers.RepeatedCompositeFieldContainer[PBAlexaListItem]
    name: str
    state: str
    version: int
    def __init__(self, identifier: _Optional[str] = ..., alexaListId: _Optional[str] = ..., anylistListId: _Optional[str] = ..., alexaUserId: _Optional[str] = ..., name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[PBAlexaListItem, _Mapping]]] = ..., state: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class PBAlexaListItem(_message.Message):
    __slots__ = ["alexaItemId", "alexaListId", "alexaUserId", "anylistItemId", "identifier", "itemValue", "status", "version"]
    ALEXAITEMID_FIELD_NUMBER: _ClassVar[int]
    ALEXALISTID_FIELD_NUMBER: _ClassVar[int]
    ALEXAUSERID_FIELD_NUMBER: _ClassVar[int]
    ANYLISTITEMID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMVALUE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    alexaItemId: str
    alexaListId: str
    alexaUserId: str
    anylistItemId: str
    identifier: str
    itemValue: str
    status: str
    version: int
    def __init__(self, identifier: _Optional[str] = ..., alexaItemId: _Optional[str] = ..., anylistItemId: _Optional[str] = ..., alexaListId: _Optional[str] = ..., alexaUserId: _Optional[str] = ..., version: _Optional[int] = ..., itemValue: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class PBAlexaListOperation(_message.Message):
    __slots__ = ["alexaUserId", "identifier", "operationItems", "operationLists", "operationType"]
    ALEXAUSERID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OPERATIONITEMS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONLISTS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    alexaUserId: str
    identifier: str
    operationItems: _containers.RepeatedCompositeFieldContainer[PBAlexaListItem]
    operationLists: _containers.RepeatedCompositeFieldContainer[PBAlexaList]
    operationType: str
    def __init__(self, identifier: _Optional[str] = ..., operationType: _Optional[str] = ..., alexaUserId: _Optional[str] = ..., operationItems: _Optional[_Iterable[_Union[PBAlexaListItem, _Mapping]]] = ..., operationLists: _Optional[_Iterable[_Union[PBAlexaList, _Mapping]]] = ...) -> None: ...

class PBAlexaTask(_message.Message):
    __slots__ = ["alexaUserId", "eventJson", "identifier", "listOperation"]
    ALEXAUSERID_FIELD_NUMBER: _ClassVar[int]
    EVENTJSON_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LISTOPERATION_FIELD_NUMBER: _ClassVar[int]
    alexaUserId: str
    eventJson: str
    identifier: str
    listOperation: PBAlexaListOperation
    def __init__(self, identifier: _Optional[str] = ..., alexaUserId: _Optional[str] = ..., eventJson: _Optional[str] = ..., listOperation: _Optional[_Union[PBAlexaListOperation, _Mapping]] = ...) -> None: ...

class PBAlexaUser(_message.Message):
    __slots__ = ["accountLinkedTimestamp", "alexaApiEndpoint", "alexaUserId", "anylistUserId", "hasListReadPermission", "hasListWritePermission", "identifier", "isSkillEnabled", "skillEnabledTimestamp", "skillPermissionTimestamp"]
    ACCOUNTLINKEDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ALEXAAPIENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ALEXAUSERID_FIELD_NUMBER: _ClassVar[int]
    ANYLISTUSERID_FIELD_NUMBER: _ClassVar[int]
    HASLISTREADPERMISSION_FIELD_NUMBER: _ClassVar[int]
    HASLISTWRITEPERMISSION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISSKILLENABLED_FIELD_NUMBER: _ClassVar[int]
    SKILLENABLEDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SKILLPERMISSIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    accountLinkedTimestamp: str
    alexaApiEndpoint: str
    alexaUserId: str
    anylistUserId: str
    hasListReadPermission: bool
    hasListWritePermission: bool
    identifier: str
    isSkillEnabled: bool
    skillEnabledTimestamp: str
    skillPermissionTimestamp: str
    def __init__(self, identifier: _Optional[str] = ..., alexaUserId: _Optional[str] = ..., anylistUserId: _Optional[str] = ..., hasListReadPermission: bool = ..., hasListWritePermission: bool = ..., isSkillEnabled: bool = ..., accountLinkedTimestamp: _Optional[str] = ..., skillEnabledTimestamp: _Optional[str] = ..., skillPermissionTimestamp: _Optional[str] = ..., alexaApiEndpoint: _Optional[str] = ...) -> None: ...

class PBAppNotice(_message.Message):
    __slots__ = ["bodyCss", "bodyHtml", "context", "identifier", "isDraft", "maxUserCreationTime", "notificationSubtitle", "notificationTitle", "timestamp", "title", "userId"]
    BODYCSS_FIELD_NUMBER: _ClassVar[int]
    BODYHTML_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISDRAFT_FIELD_NUMBER: _ClassVar[int]
    MAXUSERCREATIONTIME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONSUBTITLE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONTITLE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    bodyCss: str
    bodyHtml: str
    context: str
    identifier: str
    isDraft: bool
    maxUserCreationTime: float
    notificationSubtitle: str
    notificationTitle: str
    timestamp: float
    title: str
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., title: _Optional[str] = ..., notificationTitle: _Optional[str] = ..., notificationSubtitle: _Optional[str] = ..., bodyHtml: _Optional[str] = ..., bodyCss: _Optional[str] = ..., userId: _Optional[str] = ..., context: _Optional[str] = ..., isDraft: bool = ..., maxUserCreationTime: _Optional[float] = ...) -> None: ...

class PBAppNoticeList(_message.Message):
    __slots__ = ["notices"]
    NOTICES_FIELD_NUMBER: _ClassVar[int]
    notices: _containers.RepeatedCompositeFieldContainer[PBAppNotice]
    def __init__(self, notices: _Optional[_Iterable[_Union[PBAppNotice, _Mapping]]] = ...) -> None: ...

class PBAppNoticeOperation(_message.Message):
    __slots__ = ["metadata", "noticeIds"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NOTICEIDS_FIELD_NUMBER: _ClassVar[int]
    metadata: PBOperationMetadata
    noticeIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., noticeIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBAppNoticeOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBAppNoticeOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBAppNoticeOperation, _Mapping]]] = ...) -> None: ...

class PBAppNoticesResponse(_message.Message):
    __slots__ = ["newGlobalNotices", "newUserNotices", "removedGlobalNoticeIds", "removedUserNoticeIds", "updatedGlobalNotices", "updatedUserNotices", "userData"]
    NEWGLOBALNOTICES_FIELD_NUMBER: _ClassVar[int]
    NEWUSERNOTICES_FIELD_NUMBER: _ClassVar[int]
    REMOVEDGLOBALNOTICEIDS_FIELD_NUMBER: _ClassVar[int]
    REMOVEDUSERNOTICEIDS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDGLOBALNOTICES_FIELD_NUMBER: _ClassVar[int]
    UPDATEDUSERNOTICES_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    newGlobalNotices: _containers.RepeatedCompositeFieldContainer[PBAppNotice]
    newUserNotices: _containers.RepeatedCompositeFieldContainer[PBAppNotice]
    removedGlobalNoticeIds: _containers.RepeatedScalarFieldContainer[str]
    removedUserNoticeIds: _containers.RepeatedScalarFieldContainer[str]
    updatedGlobalNotices: _containers.RepeatedCompositeFieldContainer[PBAppNotice]
    updatedUserNotices: _containers.RepeatedCompositeFieldContainer[PBAppNotice]
    userData: PBAppNoticesUserData
    def __init__(self, newGlobalNotices: _Optional[_Iterable[_Union[PBAppNotice, _Mapping]]] = ..., updatedGlobalNotices: _Optional[_Iterable[_Union[PBAppNotice, _Mapping]]] = ..., removedGlobalNoticeIds: _Optional[_Iterable[str]] = ..., newUserNotices: _Optional[_Iterable[_Union[PBAppNotice, _Mapping]]] = ..., updatedUserNotices: _Optional[_Iterable[_Union[PBAppNotice, _Mapping]]] = ..., removedUserNoticeIds: _Optional[_Iterable[str]] = ..., userData: _Optional[_Union[PBAppNoticesUserData, _Mapping]] = ...) -> None: ...

class PBAppNoticesUserData(_message.Message):
    __slots__ = ["dismissedGlobalNoticeIds", "identifier", "readNoticeIds", "timestamp"]
    DISMISSEDGLOBALNOTICEIDS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    READNOTICEIDS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    dismissedGlobalNoticeIds: _containers.RepeatedScalarFieldContainer[str]
    identifier: str
    readNoticeIds: _containers.RepeatedScalarFieldContainer[str]
    timestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., readNoticeIds: _Optional[_Iterable[str]] = ..., dismissedGlobalNoticeIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBAuthTokenInfo(_message.Message):
    __slots__ = ["blacklistedTimestamp", "clientPlatform", "creationTimestamp", "expirationTimestamp", "identifier", "isBlacklisted", "lastUsedForRefreshTimestamp", "replacementTokenGenerationTimestamp", "replacementTokenId", "replacementTokenStr", "userId"]
    BLACKLISTEDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENTPLATFORM_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISBLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    LASTUSEDFORREFRESHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENTTOKENGENERATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENTTOKENID_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENTTOKENSTR_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    blacklistedTimestamp: int
    clientPlatform: str
    creationTimestamp: int
    expirationTimestamp: int
    identifier: str
    isBlacklisted: bool
    lastUsedForRefreshTimestamp: int
    replacementTokenGenerationTimestamp: int
    replacementTokenId: str
    replacementTokenStr: str
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., isBlacklisted: bool = ..., userId: _Optional[str] = ..., creationTimestamp: _Optional[int] = ..., expirationTimestamp: _Optional[int] = ..., blacklistedTimestamp: _Optional[int] = ..., lastUsedForRefreshTimestamp: _Optional[int] = ..., replacementTokenId: _Optional[str] = ..., replacementTokenStr: _Optional[str] = ..., replacementTokenGenerationTimestamp: _Optional[int] = ..., clientPlatform: _Optional[str] = ...) -> None: ...

class PBCalendar(_message.Message):
    __slots__ = ["identifier", "logicalClockTime"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOGICALCLOCKTIME_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    logicalClockTime: int
    def __init__(self, identifier: _Optional[str] = ..., logicalClockTime: _Optional[int] = ...) -> None: ...

class PBCalendarEvent(_message.Message):
    __slots__ = ["calendarId", "date", "details", "identifier", "labelId", "labelSortIndex", "logicalTimestamp", "orderAddedSortIndex", "recipeId", "recipeScaleFactor", "title"]
    CALENDARID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LABELID_FIELD_NUMBER: _ClassVar[int]
    LABELSORTINDEX_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDERADDEDSORTINDEX_FIELD_NUMBER: _ClassVar[int]
    RECIPEID_FIELD_NUMBER: _ClassVar[int]
    RECIPESCALEFACTOR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    calendarId: str
    date: str
    details: str
    identifier: str
    labelId: str
    labelSortIndex: int
    logicalTimestamp: int
    orderAddedSortIndex: int
    recipeId: str
    recipeScaleFactor: float
    title: str
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., calendarId: _Optional[str] = ..., date: _Optional[str] = ..., title: _Optional[str] = ..., details: _Optional[str] = ..., recipeId: _Optional[str] = ..., labelId: _Optional[str] = ..., orderAddedSortIndex: _Optional[int] = ..., labelSortIndex: _Optional[int] = ..., recipeScaleFactor: _Optional[float] = ...) -> None: ...

class PBCalendarLabel(_message.Message):
    __slots__ = ["calendarId", "hexColor", "identifier", "logicalTimestamp", "name", "sortIndex"]
    CALENDARID_FIELD_NUMBER: _ClassVar[int]
    HEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SORTINDEX_FIELD_NUMBER: _ClassVar[int]
    calendarId: str
    hexColor: str
    identifier: str
    logicalTimestamp: int
    name: str
    sortIndex: int
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., calendarId: _Optional[str] = ..., hexColor: _Optional[str] = ..., name: _Optional[str] = ..., sortIndex: _Optional[int] = ...) -> None: ...

class PBCalendarOperation(_message.Message):
    __slots__ = ["calendarId", "eventIds", "metadata", "originalEvent", "originalEvents", "originalLabel", "sortedLabelIds", "updatedEvent", "updatedEvents", "updatedLabel"]
    CALENDARID_FIELD_NUMBER: _ClassVar[int]
    EVENTIDS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORIGINALEVENTS_FIELD_NUMBER: _ClassVar[int]
    ORIGINALEVENT_FIELD_NUMBER: _ClassVar[int]
    ORIGINALLABEL_FIELD_NUMBER: _ClassVar[int]
    SORTEDLABELIDS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDEVENTS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDEVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDLABEL_FIELD_NUMBER: _ClassVar[int]
    calendarId: str
    eventIds: _containers.RepeatedScalarFieldContainer[str]
    metadata: PBOperationMetadata
    originalEvent: PBCalendarEvent
    originalEvents: _containers.RepeatedCompositeFieldContainer[PBCalendarEvent]
    originalLabel: PBCalendarLabel
    sortedLabelIds: _containers.RepeatedScalarFieldContainer[str]
    updatedEvent: PBCalendarEvent
    updatedEvents: _containers.RepeatedCompositeFieldContainer[PBCalendarEvent]
    updatedLabel: PBCalendarLabel
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., calendarId: _Optional[str] = ..., updatedEvent: _Optional[_Union[PBCalendarEvent, _Mapping]] = ..., originalEvent: _Optional[_Union[PBCalendarEvent, _Mapping]] = ..., updatedLabel: _Optional[_Union[PBCalendarLabel, _Mapping]] = ..., originalLabel: _Optional[_Union[PBCalendarLabel, _Mapping]] = ..., sortedLabelIds: _Optional[_Iterable[str]] = ..., eventIds: _Optional[_Iterable[str]] = ..., updatedEvents: _Optional[_Iterable[_Union[PBCalendarEvent, _Mapping]]] = ..., originalEvents: _Optional[_Iterable[_Union[PBCalendarEvent, _Mapping]]] = ...) -> None: ...

class PBCalendarOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBCalendarOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBCalendarOperation, _Mapping]]] = ...) -> None: ...

class PBCalendarResponse(_message.Message):
    __slots__ = ["calendarId", "deletedEventIds", "deletedLabelIds", "events", "isFullSync", "labels", "logicalTimestamp"]
    CALENDARID_FIELD_NUMBER: _ClassVar[int]
    DELETEDEVENTIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDLABELIDS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    ISFULLSYNC_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    calendarId: str
    deletedEventIds: _containers.RepeatedScalarFieldContainer[str]
    deletedLabelIds: _containers.RepeatedScalarFieldContainer[str]
    events: _containers.RepeatedCompositeFieldContainer[PBCalendarEvent]
    isFullSync: bool
    labels: _containers.RepeatedCompositeFieldContainer[PBCalendarLabel]
    logicalTimestamp: int
    def __init__(self, calendarId: _Optional[str] = ..., isFullSync: bool = ..., logicalTimestamp: _Optional[int] = ..., events: _Optional[_Iterable[_Union[PBCalendarEvent, _Mapping]]] = ..., deletedEventIds: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[PBCalendarLabel, _Mapping]]] = ..., deletedLabelIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBCategorizeItemOperation(_message.Message):
    __slots__ = ["listItem", "metadata"]
    LISTITEM_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    listItem: ListItem
    metadata: PBOperationMetadata
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., listItem: _Optional[_Union[ListItem, _Mapping]] = ...) -> None: ...

class PBCategorizeItemOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBCategorizeItemOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBCategorizeItemOperation, _Mapping]]] = ...) -> None: ...

class PBCategorizedItemsList(_message.Message):
    __slots__ = ["categorizedItems", "timestamp"]
    CATEGORIZEDITEMS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    categorizedItems: _containers.RepeatedCompositeFieldContainer[ListItem]
    timestamp: PBTimestamp
    def __init__(self, timestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., categorizedItems: _Optional[_Iterable[_Union[ListItem, _Mapping]]] = ...) -> None: ...

class PBCategoryGrouping(_message.Message):
    __slots__ = ["categoryIds", "identifier", "name", "sharingId", "shouldHideFromBrowseListCategoryGroupsScreen", "timestamp", "userId"]
    CATEGORYIDS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHARINGID_FIELD_NUMBER: _ClassVar[int]
    SHOULDHIDEFROMBROWSELISTCATEGORYGROUPSSCREEN_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    categoryIds: _containers.RepeatedScalarFieldContainer[str]
    identifier: str
    name: str
    sharingId: str
    shouldHideFromBrowseListCategoryGroupsScreen: bool
    timestamp: float
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., userId: _Optional[str] = ..., name: _Optional[str] = ..., timestamp: _Optional[float] = ..., sharingId: _Optional[str] = ..., categoryIds: _Optional[_Iterable[str]] = ..., shouldHideFromBrowseListCategoryGroupsScreen: bool = ...) -> None: ...

class PBCategoryOrdering(_message.Message):
    __slots__ = ["categories", "identifier", "name"]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedScalarFieldContainer[str]
    identifier: str
    name: str
    def __init__(self, identifier: _Optional[str] = ..., name: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ...) -> None: ...

class PBDeletedObjectID(_message.Message):
    __slots__ = ["identifier", "logicalTimestamp"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    logicalTimestamp: int
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ...) -> None: ...

class PBDeletedObjectIDList(_message.Message):
    __slots__ = ["containerId", "creationLogicalTimestamp", "deletedObjectIds", "identifier", "logicalClockId", "logicalTimestamp"]
    CONTAINERID_FIELD_NUMBER: _ClassVar[int]
    CREATIONLOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELETEDOBJECTIDS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOGICALCLOCKID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    containerId: str
    creationLogicalTimestamp: int
    deletedObjectIds: _containers.RepeatedCompositeFieldContainer[PBDeletedObjectID]
    identifier: str
    logicalClockId: str
    logicalTimestamp: int
    def __init__(self, identifier: _Optional[str] = ..., containerId: _Optional[str] = ..., logicalClockId: _Optional[str] = ..., creationLogicalTimestamp: _Optional[int] = ..., logicalTimestamp: _Optional[int] = ..., deletedObjectIds: _Optional[_Iterable[_Union[PBDeletedObjectID, _Mapping]]] = ...) -> None: ...

class PBDeletedUserInfo(_message.Message):
    __slots__ = ["adminEmail", "adminNote", "deletionTimestamp", "identifier", "ipAddress", "supportTicketUrl", "timestamp", "userEmail"]
    ADMINEMAIL_FIELD_NUMBER: _ClassVar[int]
    ADMINNOTE_FIELD_NUMBER: _ClassVar[int]
    DELETIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTTICKETURL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USEREMAIL_FIELD_NUMBER: _ClassVar[int]
    adminEmail: str
    adminNote: str
    deletionTimestamp: float
    identifier: str
    ipAddress: str
    supportTicketUrl: str
    timestamp: float
    userEmail: str
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., deletionTimestamp: _Optional[float] = ..., userEmail: _Optional[str] = ..., adminEmail: _Optional[str] = ..., adminNote: _Optional[str] = ..., supportTicketUrl: _Optional[str] = ..., ipAddress: _Optional[str] = ...) -> None: ...

class PBEditOperationResponse(_message.Message):
    __slots__ = ["currentLogicalTimestamps", "fullRefreshTimestampIds", "newTimestamps", "originalLogicalTimestamps", "originalTimestamps", "processedOperations"]
    CURRENTLOGICALTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    FULLREFRESHTIMESTAMPIDS_FIELD_NUMBER: _ClassVar[int]
    NEWTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    ORIGINALLOGICALTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    ORIGINALTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    PROCESSEDOPERATIONS_FIELD_NUMBER: _ClassVar[int]
    currentLogicalTimestamps: _containers.RepeatedCompositeFieldContainer[PBLogicalTimestamp]
    fullRefreshTimestampIds: _containers.RepeatedScalarFieldContainer[str]
    newTimestamps: _containers.RepeatedCompositeFieldContainer[PBTimestamp]
    originalLogicalTimestamps: _containers.RepeatedCompositeFieldContainer[PBLogicalTimestamp]
    originalTimestamps: _containers.RepeatedCompositeFieldContainer[PBTimestamp]
    processedOperations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, originalTimestamps: _Optional[_Iterable[_Union[PBTimestamp, _Mapping]]] = ..., newTimestamps: _Optional[_Iterable[_Union[PBTimestamp, _Mapping]]] = ..., processedOperations: _Optional[_Iterable[str]] = ..., originalLogicalTimestamps: _Optional[_Iterable[_Union[PBLogicalTimestamp, _Mapping]]] = ..., currentLogicalTimestamps: _Optional[_Iterable[_Union[PBLogicalTimestamp, _Mapping]]] = ..., fullRefreshTimestampIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBEmailEvent(_message.Message):
    __slots__ = ["description", "eventData", "eventType"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EVENTDATA_FIELD_NUMBER: _ClassVar[int]
    EVENTTYPE_FIELD_NUMBER: _ClassVar[int]
    description: str
    eventData: str
    eventType: str
    def __init__(self, eventType: _Optional[str] = ..., eventData: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class PBEmailSuppressionInfo(_message.Message):
    __slots__ = ["emailAddress", "emailEvents", "identifier", "shouldSuppressAllMessages"]
    EMAILADDRESS_FIELD_NUMBER: _ClassVar[int]
    EMAILEVENTS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SHOULDSUPPRESSALLMESSAGES_FIELD_NUMBER: _ClassVar[int]
    emailAddress: str
    emailEvents: _containers.RepeatedCompositeFieldContainer[PBEmailEvent]
    identifier: str
    shouldSuppressAllMessages: bool
    def __init__(self, identifier: _Optional[str] = ..., emailAddress: _Optional[str] = ..., shouldSuppressAllMessages: bool = ..., emailEvents: _Optional[_Iterable[_Union[PBEmailEvent, _Mapping]]] = ...) -> None: ...

class PBEmailUserIDPair(_message.Message):
    __slots__ = ["email", "fullName", "userId"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FULLNAME_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    email: str
    fullName: str
    userId: str
    def __init__(self, email: _Optional[str] = ..., userId: _Optional[str] = ..., fullName: _Optional[str] = ...) -> None: ...

class PBEmailUserIDPairList(_message.Message):
    __slots__ = ["emailUserIdPair"]
    EMAILUSERIDPAIR_FIELD_NUMBER: _ClassVar[int]
    emailUserIdPair: _containers.RepeatedCompositeFieldContainer[PBEmailUserIDPair]
    def __init__(self, emailUserIdPair: _Optional[_Iterable[_Union[PBEmailUserIDPair, _Mapping]]] = ...) -> None: ...

class PBFavoriteProductOperation(_message.Message):
    __slots__ = ["metadata", "productId"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    metadata: PBOperationMetadata
    productId: str
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., productId: _Optional[str] = ...) -> None: ...

class PBFavoriteProductOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBFavoriteProductOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBFavoriteProductOperation, _Mapping]]] = ...) -> None: ...

class PBGoogleAssistantList(_message.Message):
    __slots__ = ["anylistListId", "anylistUserId", "createTime", "googleAssistantCreateToken", "identifier", "isArchived", "items", "title", "updateTime"]
    ANYLISTLISTID_FIELD_NUMBER: _ClassVar[int]
    ANYLISTUSERID_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    GOOGLEASSISTANTCREATETOKEN_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    anylistListId: str
    anylistUserId: str
    createTime: str
    googleAssistantCreateToken: str
    identifier: str
    isArchived: bool
    items: _containers.RepeatedCompositeFieldContainer[PBGoogleAssistantListItem]
    title: str
    updateTime: str
    def __init__(self, identifier: _Optional[str] = ..., googleAssistantCreateToken: _Optional[str] = ..., anylistListId: _Optional[str] = ..., anylistUserId: _Optional[str] = ..., title: _Optional[str] = ..., items: _Optional[_Iterable[_Union[PBGoogleAssistantListItem, _Mapping]]] = ..., isArchived: bool = ..., createTime: _Optional[str] = ..., updateTime: _Optional[str] = ...) -> None: ...

class PBGoogleAssistantListItem(_message.Message):
    __slots__ = ["anylistItemId", "anylistUserId", "content", "createTime", "googleAssistantCreateToken", "googleAssistantListId", "identifier", "isChecked", "updateTime"]
    ANYLISTITEMID_FIELD_NUMBER: _ClassVar[int]
    ANYLISTUSERID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    GOOGLEASSISTANTCREATETOKEN_FIELD_NUMBER: _ClassVar[int]
    GOOGLEASSISTANTLISTID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISCHECKED_FIELD_NUMBER: _ClassVar[int]
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    anylistItemId: str
    anylistUserId: str
    content: str
    createTime: str
    googleAssistantCreateToken: str
    googleAssistantListId: str
    identifier: str
    isChecked: bool
    updateTime: str
    def __init__(self, identifier: _Optional[str] = ..., googleAssistantCreateToken: _Optional[str] = ..., anylistItemId: _Optional[str] = ..., googleAssistantListId: _Optional[str] = ..., anylistUserId: _Optional[str] = ..., content: _Optional[str] = ..., isChecked: bool = ..., createTime: _Optional[str] = ..., updateTime: _Optional[str] = ...) -> None: ...

class PBGoogleAssistantListOperation(_message.Message):
    __slots__ = ["anylistUserId", "googleAssistantListId", "identifier", "operationItems", "operationLists", "operationType"]
    ANYLISTUSERID_FIELD_NUMBER: _ClassVar[int]
    GOOGLEASSISTANTLISTID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OPERATIONITEMS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONLISTS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    anylistUserId: str
    googleAssistantListId: str
    identifier: str
    operationItems: _containers.RepeatedCompositeFieldContainer[PBGoogleAssistantListItem]
    operationLists: _containers.RepeatedCompositeFieldContainer[PBGoogleAssistantList]
    operationType: str
    def __init__(self, identifier: _Optional[str] = ..., operationType: _Optional[str] = ..., anylistUserId: _Optional[str] = ..., operationItems: _Optional[_Iterable[_Union[PBGoogleAssistantListItem, _Mapping]]] = ..., operationLists: _Optional[_Iterable[_Union[PBGoogleAssistantList, _Mapping]]] = ..., googleAssistantListId: _Optional[str] = ...) -> None: ...

class PBGoogleAssistantTask(_message.Message):
    __slots__ = ["anylistUserId", "identifier", "listOperation"]
    ANYLISTUSERID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LISTOPERATION_FIELD_NUMBER: _ClassVar[int]
    anylistUserId: str
    identifier: str
    listOperation: PBGoogleAssistantListOperation
    def __init__(self, identifier: _Optional[str] = ..., anylistUserId: _Optional[str] = ..., listOperation: _Optional[_Union[PBGoogleAssistantListOperation, _Mapping]] = ...) -> None: ...

class PBGoogleAssistantUser(_message.Message):
    __slots__ = ["anylistAccessToken", "anylistRefreshToken", "anylistUserId", "identifier", "isActiveGoogleAssistantProvider", "isGoogleAssistantAccountLinked", "listActionsApiRefreshToken"]
    ANYLISTACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    ANYLISTREFRESHTOKEN_FIELD_NUMBER: _ClassVar[int]
    ANYLISTUSERID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISACTIVEGOOGLEASSISTANTPROVIDER_FIELD_NUMBER: _ClassVar[int]
    ISGOOGLEASSISTANTACCOUNTLINKED_FIELD_NUMBER: _ClassVar[int]
    LISTACTIONSAPIREFRESHTOKEN_FIELD_NUMBER: _ClassVar[int]
    anylistAccessToken: str
    anylistRefreshToken: str
    anylistUserId: str
    identifier: str
    isActiveGoogleAssistantProvider: bool
    isGoogleAssistantAccountLinked: bool
    listActionsApiRefreshToken: str
    def __init__(self, identifier: _Optional[str] = ..., anylistUserId: _Optional[str] = ..., listActionsApiRefreshToken: _Optional[str] = ..., isGoogleAssistantAccountLinked: bool = ..., anylistRefreshToken: _Optional[str] = ..., anylistAccessToken: _Optional[str] = ..., isActiveGoogleAssistantProvider: bool = ...) -> None: ...

class PBGooglePlayPurchase(_message.Message):
    __slots__ = ["orderId", "purchaseInfo", "purchaseToken"]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    PURCHASEINFO_FIELD_NUMBER: _ClassVar[int]
    PURCHASETOKEN_FIELD_NUMBER: _ClassVar[int]
    orderId: str
    purchaseInfo: str
    purchaseToken: str
    def __init__(self, orderId: _Optional[str] = ..., purchaseToken: _Optional[str] = ..., purchaseInfo: _Optional[str] = ...) -> None: ...

class PBHintBannerDisplayStats(_message.Message):
    __slots__ = ["displayTimestamps", "identifier"]
    DISPLAYTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    displayTimestamps: _containers.RepeatedScalarFieldContainer[float]
    identifier: str
    def __init__(self, identifier: _Optional[str] = ..., displayTimestamps: _Optional[_Iterable[float]] = ...) -> None: ...

class PBIAPReceipt(_message.Message):
    __slots__ = ["parsedReceipt", "receiptData", "transactionId"]
    PARSEDRECEIPT_FIELD_NUMBER: _ClassVar[int]
    RECEIPTDATA_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    parsedReceipt: str
    receiptData: bytes
    transactionId: str
    def __init__(self, transactionId: _Optional[str] = ..., receiptData: _Optional[bytes] = ..., parsedReceipt: _Optional[str] = ...) -> None: ...

class PBIcon(_message.Message):
    __slots__ = ["iconName", "tintHexColor"]
    ICONNAME_FIELD_NUMBER: _ClassVar[int]
    TINTHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    iconName: str
    tintHexColor: str
    def __init__(self, iconName: _Optional[str] = ..., tintHexColor: _Optional[str] = ...) -> None: ...

class PBIdentifierList(_message.Message):
    __slots__ = ["identifiers", "timestamp"]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedScalarFieldContainer[str]
    timestamp: float
    def __init__(self, timestamp: _Optional[float] = ..., identifiers: _Optional[_Iterable[str]] = ...) -> None: ...

class PBIngredient(_message.Message):
    __slots__ = ["identifier", "isHeading", "name", "note", "quantity", "rawIngredient"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISHEADING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RAWINGREDIENT_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    isHeading: bool
    name: str
    note: str
    quantity: str
    rawIngredient: str
    def __init__(self, identifier: _Optional[str] = ..., rawIngredient: _Optional[str] = ..., name: _Optional[str] = ..., quantity: _Optional[str] = ..., note: _Optional[str] = ..., isHeading: bool = ...) -> None: ...

class PBItemIngredient(_message.Message):
    __slots__ = ["eventDate", "eventId", "ingredient", "packageSizePb", "quantityPb", "recipeId", "recipeName"]
    EVENTDATE_FIELD_NUMBER: _ClassVar[int]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    INGREDIENT_FIELD_NUMBER: _ClassVar[int]
    PACKAGESIZEPB_FIELD_NUMBER: _ClassVar[int]
    QUANTITYPB_FIELD_NUMBER: _ClassVar[int]
    RECIPEID_FIELD_NUMBER: _ClassVar[int]
    RECIPENAME_FIELD_NUMBER: _ClassVar[int]
    eventDate: str
    eventId: str
    ingredient: PBIngredient
    packageSizePb: PBItemPackageSize
    quantityPb: PBItemQuantity
    recipeId: str
    recipeName: str
    def __init__(self, ingredient: _Optional[_Union[PBIngredient, _Mapping]] = ..., quantityPb: _Optional[_Union[PBItemQuantity, _Mapping]] = ..., packageSizePb: _Optional[_Union[PBItemPackageSize, _Mapping]] = ..., recipeId: _Optional[str] = ..., eventId: _Optional[str] = ..., recipeName: _Optional[str] = ..., eventDate: _Optional[str] = ...) -> None: ...

class PBItemPackageSize(_message.Message):
    __slots__ = ["packageType", "rawPackageSize", "size", "unit"]
    PACKAGETYPE_FIELD_NUMBER: _ClassVar[int]
    RAWPACKAGESIZE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    packageType: str
    rawPackageSize: str
    size: str
    unit: str
    def __init__(self, size: _Optional[str] = ..., unit: _Optional[str] = ..., packageType: _Optional[str] = ..., rawPackageSize: _Optional[str] = ...) -> None: ...

class PBItemPrice(_message.Message):
    __slots__ = ["amount", "date", "details", "storeId"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    STOREID_FIELD_NUMBER: _ClassVar[int]
    amount: float
    date: str
    details: str
    storeId: str
    def __init__(self, amount: _Optional[float] = ..., details: _Optional[str] = ..., storeId: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class PBItemQuantity(_message.Message):
    __slots__ = ["amount", "rawQuantity", "unit"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    RAWQUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    amount: str
    rawQuantity: str
    unit: str
    def __init__(self, amount: _Optional[str] = ..., unit: _Optional[str] = ..., rawQuantity: _Optional[str] = ...) -> None: ...

class PBItemQuantityAndPackageSize(_message.Message):
    __slots__ = ["packageSizePb", "quantityPb"]
    PACKAGESIZEPB_FIELD_NUMBER: _ClassVar[int]
    QUANTITYPB_FIELD_NUMBER: _ClassVar[int]
    packageSizePb: PBItemPackageSize
    quantityPb: PBItemQuantity
    def __init__(self, quantityPb: _Optional[_Union[PBItemQuantity, _Mapping]] = ..., packageSizePb: _Optional[_Union[PBItemPackageSize, _Mapping]] = ...) -> None: ...

class PBListCategorizationRule(_message.Message):
    __slots__ = ["categoryGroupId", "categoryId", "identifier", "itemName", "listId", "logicalTimestamp"]
    CATEGORYGROUPID_FIELD_NUMBER: _ClassVar[int]
    CATEGORYID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    categoryGroupId: str
    categoryId: str
    identifier: str
    itemName: str
    listId: str
    logicalTimestamp: int
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., listId: _Optional[str] = ..., categoryGroupId: _Optional[str] = ..., itemName: _Optional[str] = ..., categoryId: _Optional[str] = ...) -> None: ...

class PBListCategorizationRuleList(_message.Message):
    __slots__ = ["categorizationRules", "categorizationRulesLogicalTimestamp", "deletedCategorizationRulesLogicalTimestamp", "identifier", "listId", "logicalTimestamp"]
    CATEGORIZATIONRULESLOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CATEGORIZATIONRULES_FIELD_NUMBER: _ClassVar[int]
    DELETEDCATEGORIZATIONRULESLOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    categorizationRules: _containers.RepeatedCompositeFieldContainer[PBListCategorizationRule]
    categorizationRulesLogicalTimestamp: int
    deletedCategorizationRulesLogicalTimestamp: int
    identifier: str
    listId: str
    logicalTimestamp: int
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., listId: _Optional[str] = ..., categorizationRules: _Optional[_Iterable[_Union[PBListCategorizationRule, _Mapping]]] = ..., categorizationRulesLogicalTimestamp: _Optional[int] = ..., deletedCategorizationRulesLogicalTimestamp: _Optional[int] = ...) -> None: ...

class PBListCategory(_message.Message):
    __slots__ = ["categoryGroupId", "icon", "identifier", "listId", "logicalTimestamp", "name", "sortIndex", "systemCategory"]
    CATEGORYGROUPID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SORTINDEX_FIELD_NUMBER: _ClassVar[int]
    SYSTEMCATEGORY_FIELD_NUMBER: _ClassVar[int]
    categoryGroupId: str
    icon: str
    identifier: str
    listId: str
    logicalTimestamp: int
    name: str
    sortIndex: int
    systemCategory: str
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., categoryGroupId: _Optional[str] = ..., listId: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., systemCategory: _Optional[str] = ..., sortIndex: _Optional[int] = ...) -> None: ...

class PBListCategoryGroup(_message.Message):
    __slots__ = ["categories", "categoriesLogicalTimestamp", "defaultCategoryId", "deletedCategoriesLogicalTimestamp", "identifier", "listId", "logicalTimestamp", "name"]
    CATEGORIESLOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    DEFAULTCATEGORYID_FIELD_NUMBER: _ClassVar[int]
    DELETEDCATEGORIESLOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[PBListCategory]
    categoriesLogicalTimestamp: int
    defaultCategoryId: str
    deletedCategoriesLogicalTimestamp: int
    identifier: str
    listId: str
    logicalTimestamp: int
    name: str
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., listId: _Optional[str] = ..., name: _Optional[str] = ..., categories: _Optional[_Iterable[_Union[PBListCategory, _Mapping]]] = ..., defaultCategoryId: _Optional[str] = ..., categoriesLogicalTimestamp: _Optional[int] = ..., deletedCategoriesLogicalTimestamp: _Optional[int] = ...) -> None: ...

class PBListCategoryGroupResponse(_message.Message):
    __slots__ = ["categoryGroup", "deletedCategoryIds"]
    CATEGORYGROUP_FIELD_NUMBER: _ClassVar[int]
    DELETEDCATEGORYIDS_FIELD_NUMBER: _ClassVar[int]
    categoryGroup: PBListCategoryGroup
    deletedCategoryIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, categoryGroup: _Optional[_Union[PBListCategoryGroup, _Mapping]] = ..., deletedCategoryIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBListFolder(_message.Message):
    __slots__ = ["folderSettings", "identifier", "items", "name", "timestamp"]
    FOLDERSETTINGS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    folderSettings: PBListFolderSettings
    identifier: str
    items: _containers.RepeatedCompositeFieldContainer[PBListFolderItem]
    name: str
    timestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[PBListFolderItem, _Mapping]]] = ..., folderSettings: _Optional[_Union[PBListFolderSettings, _Mapping]] = ...) -> None: ...

class PBListFolderArchive(_message.Message):
    __slots__ = ["folderSettings", "items", "name"]
    FOLDERSETTINGS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    folderSettings: PBListFolderSettings
    items: _containers.RepeatedCompositeFieldContainer[PBListFolderItemArchive]
    name: str
    def __init__(self, name: _Optional[str] = ..., folderSettings: _Optional[_Union[PBListFolderSettings, _Mapping]] = ..., items: _Optional[_Iterable[_Union[PBListFolderItemArchive, _Mapping]]] = ...) -> None: ...

class PBListFolderItem(_message.Message):
    __slots__ = ["identifier", "itemType"]
    class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FolderType: PBListFolderItem.ItemType
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMTYPE_FIELD_NUMBER: _ClassVar[int]
    ListType: PBListFolderItem.ItemType
    identifier: str
    itemType: int
    def __init__(self, identifier: _Optional[str] = ..., itemType: _Optional[int] = ...) -> None: ...

class PBListFolderItemArchive(_message.Message):
    __slots__ = ["folderArchive", "listArchive"]
    FOLDERARCHIVE_FIELD_NUMBER: _ClassVar[int]
    LISTARCHIVE_FIELD_NUMBER: _ClassVar[int]
    folderArchive: PBListFolderArchive
    listArchive: PBShoppingListArchive
    def __init__(self, listArchive: _Optional[_Union[PBShoppingListArchive, _Mapping]] = ..., folderArchive: _Optional[_Union[PBListFolderArchive, _Mapping]] = ...) -> None: ...

class PBListFolderOperation(_message.Message):
    __slots__ = ["folderItems", "listDataId", "listFolder", "metadata", "originalParentFolderId", "updatedParentFolderId"]
    FOLDERITEMS_FIELD_NUMBER: _ClassVar[int]
    LISTDATAID_FIELD_NUMBER: _ClassVar[int]
    LISTFOLDER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORIGINALPARENTFOLDERID_FIELD_NUMBER: _ClassVar[int]
    UPDATEDPARENTFOLDERID_FIELD_NUMBER: _ClassVar[int]
    folderItems: _containers.RepeatedCompositeFieldContainer[PBListFolderItem]
    listDataId: str
    listFolder: PBListFolder
    metadata: PBOperationMetadata
    originalParentFolderId: str
    updatedParentFolderId: str
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., listDataId: _Optional[str] = ..., listFolder: _Optional[_Union[PBListFolder, _Mapping]] = ..., folderItems: _Optional[_Iterable[_Union[PBListFolderItem, _Mapping]]] = ..., originalParentFolderId: _Optional[str] = ..., updatedParentFolderId: _Optional[str] = ...) -> None: ...

class PBListFolderOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBListFolderOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBListFolderOperation, _Mapping]]] = ...) -> None: ...

class PBListFolderSettings(_message.Message):
    __slots__ = ["folderHexColor", "folderSortPosition", "icon", "listsSortOrder"]
    class FolderSortPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AlphabeticalSortOrder: PBListFolderSettings.SortOrder
    FOLDERHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    FOLDERSORTPOSITION_FIELD_NUMBER: _ClassVar[int]
    FolderSortPositionAfterLists: PBListFolderSettings.FolderSortPosition
    FolderSortPositionBeforeLists: PBListFolderSettings.FolderSortPosition
    FolderSortPositionWithLists: PBListFolderSettings.FolderSortPosition
    ICON_FIELD_NUMBER: _ClassVar[int]
    LISTSSORTORDER_FIELD_NUMBER: _ClassVar[int]
    ManualSortOrder: PBListFolderSettings.SortOrder
    folderHexColor: str
    folderSortPosition: int
    icon: PBIcon
    listsSortOrder: int
    def __init__(self, listsSortOrder: _Optional[int] = ..., folderSortPosition: _Optional[int] = ..., folderHexColor: _Optional[str] = ..., icon: _Optional[_Union[PBIcon, _Mapping]] = ...) -> None: ...

class PBListFolderTimestamps(_message.Message):
    __slots__ = ["folderTimestamps", "rootFolderId"]
    FOLDERTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    ROOTFOLDERID_FIELD_NUMBER: _ClassVar[int]
    folderTimestamps: _containers.RepeatedCompositeFieldContainer[PBTimestamp]
    rootFolderId: str
    def __init__(self, rootFolderId: _Optional[str] = ..., folderTimestamps: _Optional[_Iterable[_Union[PBTimestamp, _Mapping]]] = ...) -> None: ...

class PBListFoldersResponse(_message.Message):
    __slots__ = ["deletedFolderIds", "hasMigratedListOrdering", "includesAllFolders", "listDataId", "listFolders", "rootFolderId"]
    DELETEDFOLDERIDS_FIELD_NUMBER: _ClassVar[int]
    HASMIGRATEDLISTORDERING_FIELD_NUMBER: _ClassVar[int]
    INCLUDESALLFOLDERS_FIELD_NUMBER: _ClassVar[int]
    LISTDATAID_FIELD_NUMBER: _ClassVar[int]
    LISTFOLDERS_FIELD_NUMBER: _ClassVar[int]
    ROOTFOLDERID_FIELD_NUMBER: _ClassVar[int]
    deletedFolderIds: _containers.RepeatedScalarFieldContainer[str]
    hasMigratedListOrdering: bool
    includesAllFolders: bool
    listDataId: str
    listFolders: _containers.RepeatedCompositeFieldContainer[PBListFolder]
    rootFolderId: str
    def __init__(self, listDataId: _Optional[str] = ..., rootFolderId: _Optional[str] = ..., includesAllFolders: bool = ..., listFolders: _Optional[_Iterable[_Union[PBListFolder, _Mapping]]] = ..., deletedFolderIds: _Optional[_Iterable[str]] = ..., hasMigratedListOrdering: bool = ...) -> None: ...

class PBListItemCategoryAssignment(_message.Message):
    __slots__ = ["categoryGroupId", "categoryId", "identifier"]
    CATEGORYGROUPID_FIELD_NUMBER: _ClassVar[int]
    CATEGORYID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    categoryGroupId: str
    categoryId: str
    identifier: str
    def __init__(self, identifier: _Optional[str] = ..., categoryGroupId: _Optional[str] = ..., categoryId: _Optional[str] = ...) -> None: ...

class PBListOperation(_message.Message):
    __slots__ = ["itemPrice", "list", "listFolderId", "listId", "listItem", "listItemId", "metadata", "notificationLocation", "originalCategorizationRule", "originalCategory", "originalCategoryGroup", "originalStore", "originalStoreFilter", "originalValue", "sortedStoreFilterIds", "sortedStoreIds", "updatedCategorizationRule", "updatedCategorizationRules", "updatedCategory", "updatedCategoryGroup", "updatedStore", "updatedStoreFilter", "updatedValue"]
    ITEMPRICE_FIELD_NUMBER: _ClassVar[int]
    LISTFOLDERID_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LISTITEMID_FIELD_NUMBER: _ClassVar[int]
    LISTITEM_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONLOCATION_FIELD_NUMBER: _ClassVar[int]
    ORIGINALCATEGORIZATIONRULE_FIELD_NUMBER: _ClassVar[int]
    ORIGINALCATEGORYGROUP_FIELD_NUMBER: _ClassVar[int]
    ORIGINALCATEGORY_FIELD_NUMBER: _ClassVar[int]
    ORIGINALSTOREFILTER_FIELD_NUMBER: _ClassVar[int]
    ORIGINALSTORE_FIELD_NUMBER: _ClassVar[int]
    ORIGINALVALUE_FIELD_NUMBER: _ClassVar[int]
    SORTEDSTOREFILTERIDS_FIELD_NUMBER: _ClassVar[int]
    SORTEDSTOREIDS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDCATEGORIZATIONRULES_FIELD_NUMBER: _ClassVar[int]
    UPDATEDCATEGORIZATIONRULE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDCATEGORYGROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATEDCATEGORY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDSTOREFILTER_FIELD_NUMBER: _ClassVar[int]
    UPDATEDSTORE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDVALUE_FIELD_NUMBER: _ClassVar[int]
    itemPrice: PBItemPrice
    list: ShoppingList
    listFolderId: str
    listId: str
    listItem: ListItem
    listItemId: str
    metadata: PBOperationMetadata
    notificationLocation: PBNotificationLocation
    originalCategorizationRule: PBListCategorizationRule
    originalCategory: PBListCategory
    originalCategoryGroup: PBListCategoryGroup
    originalStore: PBStore
    originalStoreFilter: PBStoreFilter
    originalValue: str
    sortedStoreFilterIds: _containers.RepeatedScalarFieldContainer[str]
    sortedStoreIds: _containers.RepeatedScalarFieldContainer[str]
    updatedCategorizationRule: PBListCategorizationRule
    updatedCategorizationRules: _containers.RepeatedCompositeFieldContainer[PBListCategorizationRule]
    updatedCategory: PBListCategory
    updatedCategoryGroup: PBListCategoryGroup
    updatedStore: PBStore
    updatedStoreFilter: PBStoreFilter
    updatedValue: str
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., listId: _Optional[str] = ..., listItemId: _Optional[str] = ..., updatedValue: _Optional[str] = ..., originalValue: _Optional[str] = ..., listItem: _Optional[_Union[ListItem, _Mapping]] = ..., list: _Optional[_Union[ShoppingList, _Mapping]] = ..., listFolderId: _Optional[str] = ..., notificationLocation: _Optional[_Union[PBNotificationLocation, _Mapping]] = ..., updatedStore: _Optional[_Union[PBStore, _Mapping]] = ..., originalStore: _Optional[_Union[PBStore, _Mapping]] = ..., sortedStoreIds: _Optional[_Iterable[str]] = ..., updatedStoreFilter: _Optional[_Union[PBStoreFilter, _Mapping]] = ..., originalStoreFilter: _Optional[_Union[PBStoreFilter, _Mapping]] = ..., sortedStoreFilterIds: _Optional[_Iterable[str]] = ..., itemPrice: _Optional[_Union[PBItemPrice, _Mapping]] = ..., updatedCategory: _Optional[_Union[PBListCategory, _Mapping]] = ..., originalCategory: _Optional[_Union[PBListCategory, _Mapping]] = ..., updatedCategoryGroup: _Optional[_Union[PBListCategoryGroup, _Mapping]] = ..., originalCategoryGroup: _Optional[_Union[PBListCategoryGroup, _Mapping]] = ..., updatedCategorizationRule: _Optional[_Union[PBListCategorizationRule, _Mapping]] = ..., originalCategorizationRule: _Optional[_Union[PBListCategorizationRule, _Mapping]] = ..., updatedCategorizationRules: _Optional[_Iterable[_Union[PBListCategorizationRule, _Mapping]]] = ...) -> None: ...

class PBListOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBListOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBListOperation, _Mapping]]] = ...) -> None: ...

class PBListResponse(_message.Message):
    __slots__ = ["categorizationRules", "categoryGroupResponses", "deletedCategorizationRuleIds", "deletedCategoryGroupIds", "deletedStoreFilterIds", "deletedStoreIds", "isFullSync", "listId", "logicalTimestamp", "storeFilters", "stores"]
    CATEGORIZATIONRULES_FIELD_NUMBER: _ClassVar[int]
    CATEGORYGROUPRESPONSES_FIELD_NUMBER: _ClassVar[int]
    DELETEDCATEGORIZATIONRULEIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDCATEGORYGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDSTOREFILTERIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDSTOREIDS_FIELD_NUMBER: _ClassVar[int]
    ISFULLSYNC_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STOREFILTERS_FIELD_NUMBER: _ClassVar[int]
    STORES_FIELD_NUMBER: _ClassVar[int]
    categorizationRules: _containers.RepeatedCompositeFieldContainer[PBListCategorizationRule]
    categoryGroupResponses: _containers.RepeatedCompositeFieldContainer[PBListCategoryGroupResponse]
    deletedCategorizationRuleIds: _containers.RepeatedScalarFieldContainer[str]
    deletedCategoryGroupIds: _containers.RepeatedScalarFieldContainer[str]
    deletedStoreFilterIds: _containers.RepeatedScalarFieldContainer[str]
    deletedStoreIds: _containers.RepeatedScalarFieldContainer[str]
    isFullSync: bool
    listId: str
    logicalTimestamp: int
    storeFilters: _containers.RepeatedCompositeFieldContainer[PBStoreFilter]
    stores: _containers.RepeatedCompositeFieldContainer[PBStore]
    def __init__(self, listId: _Optional[str] = ..., isFullSync: bool = ..., logicalTimestamp: _Optional[int] = ..., categoryGroupResponses: _Optional[_Iterable[_Union[PBListCategoryGroupResponse, _Mapping]]] = ..., deletedCategoryGroupIds: _Optional[_Iterable[str]] = ..., categorizationRules: _Optional[_Iterable[_Union[PBListCategorizationRule, _Mapping]]] = ..., deletedCategorizationRuleIds: _Optional[_Iterable[str]] = ..., stores: _Optional[_Iterable[_Union[PBStore, _Mapping]]] = ..., deletedStoreIds: _Optional[_Iterable[str]] = ..., storeFilters: _Optional[_Iterable[_Union[PBStoreFilter, _Mapping]]] = ..., deletedStoreFilterIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBListSettings(_message.Message):
    __slots__ = ["badgeMode", "categoryGroupingId", "categoryOrderings", "customDarkTheme", "customTheme", "favoritesAutocompleteEnabled", "genericGroceryAutocompleteEnabled", "hasShownAccountNamePrompt", "icon", "identifier", "isEnabledForAlexa", "leftRunningTotalType", "linkedAlexaListId", "linkedGoogleAssistantListId", "listCategoryGroupId", "listColorType", "listId", "listItemSortOrder", "listThemeId", "locationNotificationsEnabled", "migrationListCategoryGroupIdForNewList", "recentItemsAutocompleteEnabled", "rightRunningTotalType", "selectedCategoryOrdering", "shouldHideCategories", "shouldHideCompletedItems", "shouldHidePrices", "shouldHideRunningTotals", "shouldHideStoreNames", "shouldRememberItemCategories", "shouldShowSharedListCategoryOrderHintBanner", "storeFilterId", "timestamp", "userId"]
    BADGEMODE_FIELD_NUMBER: _ClassVar[int]
    CATEGORYGROUPINGID_FIELD_NUMBER: _ClassVar[int]
    CATEGORYORDERINGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMDARKTHEME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMTHEME_FIELD_NUMBER: _ClassVar[int]
    FAVORITESAUTOCOMPLETEENABLED_FIELD_NUMBER: _ClassVar[int]
    GENERICGROCERYAUTOCOMPLETEENABLED_FIELD_NUMBER: _ClassVar[int]
    HASSHOWNACCOUNTNAMEPROMPT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISENABLEDFORALEXA_FIELD_NUMBER: _ClassVar[int]
    LEFTRUNNINGTOTALTYPE_FIELD_NUMBER: _ClassVar[int]
    LINKEDALEXALISTID_FIELD_NUMBER: _ClassVar[int]
    LINKEDGOOGLEASSISTANTLISTID_FIELD_NUMBER: _ClassVar[int]
    LISTCATEGORYGROUPID_FIELD_NUMBER: _ClassVar[int]
    LISTCOLORTYPE_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LISTITEMSORTORDER_FIELD_NUMBER: _ClassVar[int]
    LISTTHEMEID_FIELD_NUMBER: _ClassVar[int]
    LOCATIONNOTIFICATIONSENABLED_FIELD_NUMBER: _ClassVar[int]
    MIGRATIONLISTCATEGORYGROUPIDFORNEWLIST_FIELD_NUMBER: _ClassVar[int]
    RECENTITEMSAUTOCOMPLETEENABLED_FIELD_NUMBER: _ClassVar[int]
    RIGHTRUNNINGTOTALTYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTEDCATEGORYORDERING_FIELD_NUMBER: _ClassVar[int]
    SHOULDHIDECATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SHOULDHIDECOMPLETEDITEMS_FIELD_NUMBER: _ClassVar[int]
    SHOULDHIDEPRICES_FIELD_NUMBER: _ClassVar[int]
    SHOULDHIDERUNNINGTOTALS_FIELD_NUMBER: _ClassVar[int]
    SHOULDHIDESTORENAMES_FIELD_NUMBER: _ClassVar[int]
    SHOULDREMEMBERITEMCATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SHOULDSHOWSHAREDLISTCATEGORYORDERHINTBANNER_FIELD_NUMBER: _ClassVar[int]
    STOREFILTERID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    badgeMode: str
    categoryGroupingId: str
    categoryOrderings: _containers.RepeatedCompositeFieldContainer[PBCategoryOrdering]
    customDarkTheme: PBListTheme
    customTheme: PBListTheme
    favoritesAutocompleteEnabled: bool
    genericGroceryAutocompleteEnabled: bool
    hasShownAccountNamePrompt: bool
    icon: PBIcon
    identifier: str
    isEnabledForAlexa: bool
    leftRunningTotalType: int
    linkedAlexaListId: str
    linkedGoogleAssistantListId: str
    listCategoryGroupId: str
    listColorType: int
    listId: str
    listItemSortOrder: str
    listThemeId: str
    locationNotificationsEnabled: bool
    migrationListCategoryGroupIdForNewList: str
    recentItemsAutocompleteEnabled: bool
    rightRunningTotalType: int
    selectedCategoryOrdering: str
    shouldHideCategories: bool
    shouldHideCompletedItems: bool
    shouldHidePrices: bool
    shouldHideRunningTotals: bool
    shouldHideStoreNames: bool
    shouldRememberItemCategories: bool
    shouldShowSharedListCategoryOrderHintBanner: bool
    storeFilterId: str
    timestamp: float
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., userId: _Optional[str] = ..., listId: _Optional[str] = ..., timestamp: _Optional[float] = ..., shouldHideCategories: bool = ..., genericGroceryAutocompleteEnabled: bool = ..., favoritesAutocompleteEnabled: bool = ..., recentItemsAutocompleteEnabled: bool = ..., shouldHideCompletedItems: bool = ..., listColorType: _Optional[int] = ..., listThemeId: _Optional[str] = ..., customTheme: _Optional[_Union[PBListTheme, _Mapping]] = ..., customDarkTheme: _Optional[_Union[PBListTheme, _Mapping]] = ..., icon: _Optional[_Union[PBIcon, _Mapping]] = ..., badgeMode: _Optional[str] = ..., locationNotificationsEnabled: bool = ..., storeFilterId: _Optional[str] = ..., shouldHideStoreNames: bool = ..., shouldHideRunningTotals: bool = ..., shouldHidePrices: bool = ..., leftRunningTotalType: _Optional[int] = ..., rightRunningTotalType: _Optional[int] = ..., listCategoryGroupId: _Optional[str] = ..., migrationListCategoryGroupIdForNewList: _Optional[str] = ..., shouldShowSharedListCategoryOrderHintBanner: bool = ..., hasShownAccountNamePrompt: bool = ..., isEnabledForAlexa: bool = ..., linkedAlexaListId: _Optional[str] = ..., linkedGoogleAssistantListId: _Optional[str] = ..., shouldRememberItemCategories: bool = ..., categoryGroupingId: _Optional[str] = ..., listItemSortOrder: _Optional[str] = ..., selectedCategoryOrdering: _Optional[str] = ..., categoryOrderings: _Optional[_Iterable[_Union[PBCategoryOrdering, _Mapping]]] = ...) -> None: ...

class PBListSettingsList(_message.Message):
    __slots__ = ["settings", "timestamp"]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[PBListSettings]
    timestamp: PBTimestamp
    def __init__(self, timestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., settings: _Optional[_Iterable[_Union[PBListSettings, _Mapping]]] = ...) -> None: ...

class PBListSettingsOperation(_message.Message):
    __slots__ = ["metadata", "updatedSettings"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATEDSETTINGS_FIELD_NUMBER: _ClassVar[int]
    metadata: PBOperationMetadata
    updatedSettings: PBListSettings
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., updatedSettings: _Optional[_Union[PBListSettings, _Mapping]] = ...) -> None: ...

class PBListSettingsOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBListSettingsOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBListSettingsOperation, _Mapping]]] = ...) -> None: ...

class PBListTheme(_message.Message):
    __slots__ = ["backgroundHexColor", "backgroundImage", "backgroundTexture", "bannerHexColor", "cellHexColor", "cellTexture", "controlHexColor", "fontName", "identifier", "itemDetailsHexColor", "itemNameHexColor", "name", "navigationBarHexColor", "selectionHexColor", "separatorHexColor", "tableHexColor", "tableTexture", "timestamp", "userId"]
    BACKGROUNDHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    BACKGROUNDIMAGE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUNDTEXTURE_FIELD_NUMBER: _ClassVar[int]
    BANNERHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    CELLHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    CELLTEXTURE_FIELD_NUMBER: _ClassVar[int]
    CONTROLHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    FONTNAME_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMDETAILSHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    ITEMNAMEHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAVIGATIONBARHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    SELECTIONHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    SEPARATORHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    TABLEHEXCOLOR_FIELD_NUMBER: _ClassVar[int]
    TABLETEXTURE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    backgroundHexColor: str
    backgroundImage: str
    backgroundTexture: str
    bannerHexColor: str
    cellHexColor: str
    cellTexture: str
    controlHexColor: str
    fontName: str
    identifier: str
    itemDetailsHexColor: str
    itemNameHexColor: str
    name: str
    navigationBarHexColor: str
    selectionHexColor: str
    separatorHexColor: str
    tableHexColor: str
    tableTexture: str
    timestamp: float
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., userId: _Optional[str] = ..., name: _Optional[str] = ..., fontName: _Optional[str] = ..., bannerHexColor: _Optional[str] = ..., backgroundHexColor: _Optional[str] = ..., backgroundTexture: _Optional[str] = ..., itemNameHexColor: _Optional[str] = ..., itemDetailsHexColor: _Optional[str] = ..., controlHexColor: _Optional[str] = ..., separatorHexColor: _Optional[str] = ..., navigationBarHexColor: _Optional[str] = ..., cellHexColor: _Optional[str] = ..., cellTexture: _Optional[str] = ..., tableHexColor: _Optional[str] = ..., tableTexture: _Optional[str] = ..., backgroundImage: _Optional[str] = ..., selectionHexColor: _Optional[str] = ...) -> None: ...

class PBListThemeList(_message.Message):
    __slots__ = ["themes", "timestamp"]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    themes: _containers.RepeatedCompositeFieldContainer[PBListTheme]
    timestamp: PBTimestamp
    def __init__(self, timestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., themes: _Optional[_Iterable[_Union[PBListTheme, _Mapping]]] = ...) -> None: ...

class PBLogicalTimestamp(_message.Message):
    __slots__ = ["description", "identifier", "logicalTimestamp"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    description: str
    identifier: str
    logicalTimestamp: int
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class PBLogicalTimestampList(_message.Message):
    __slots__ = ["timestamps"]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    timestamps: _containers.RepeatedCompositeFieldContainer[PBLogicalTimestamp]
    def __init__(self, timestamps: _Optional[_Iterable[_Union[PBLogicalTimestamp, _Mapping]]] = ...) -> None: ...

class PBMealPlanSetICalendarEnabledRequest(_message.Message):
    __slots__ = ["shouldEnableIcalendarGeneration"]
    SHOULDENABLEICALENDARGENERATION_FIELD_NUMBER: _ClassVar[int]
    shouldEnableIcalendarGeneration: bool
    def __init__(self, shouldEnableIcalendarGeneration: bool = ...) -> None: ...

class PBMealPlanSetICalendarEnabledRequestResponse(_message.Message):
    __slots__ = ["accountInfo", "errorMessage", "errorTitle", "statusCode"]
    ACCOUNTINFO_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORTITLE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    accountInfo: PBAccountInfoResponse
    errorMessage: str
    errorTitle: str
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., accountInfo: _Optional[_Union[PBAccountInfoResponse, _Mapping]] = ..., errorTitle: _Optional[str] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class PBMobileAppSettings(_message.Message):
    __slots__ = ["alexaApiEndpoint", "alexaSkillHasListReadPermission", "alexaSkillHasListWritePermission", "alexaSkillOnlySupportsBuiltInLists", "appBadgeMode", "clientHasShownAlexaOnboarding", "clientHasShownGoogleAssistantOnboarding", "crossOffGesture", "defaultListId", "defaultListIdForAlexa", "didSuppressAccountNamePrompt", "hasMigratedUserCategoriesToListCategories", "hintBannerDisplayStats", "identifier", "isAccountLinkedToAlexaSkill", "isAccountLinkedToGoogleAssistant", "isActiveGoogleAssistantProvider", "isOnlineShoppingDisabled", "keepScreenOnBehavior", "listIdForRecipeIngredients", "listsSortOrder", "promptToLoadPhotosOverCellularData", "recipeCookingStates", "remindersAppImportEnabled", "shouldAutoImportReminders", "shouldExcludeNewListsFromAlexaByDefault", "shouldNotLinkNewListsWithGoogleAssistantByDefault", "shouldPreventScreenAutolock", "shouldUseMetricUnits", "starterListsSortOrder", "timestamp", "unlinkedAlexaLists", "unlinkedGoogleAssistantLists", "webCurrencyCode", "webCurrencySymbol", "webDecimalSeparator", "webHasHiddenItemPricesHelp", "webHasHiddenStoresAndFiltersHelp", "webSelectedListFolderPath", "webSelectedListId", "webSelectedMealPlanTab", "webSelectedRecipeCollectionId", "webSelectedRecipeCollectionSettingsOverride", "webSelectedRecipeCollectionType", "webSelectedRecipeId", "webSelectedTabId"]
    class KeepScreenOnBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALEXAAPIENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ALEXASKILLHASLISTREADPERMISSION_FIELD_NUMBER: _ClassVar[int]
    ALEXASKILLHASLISTWRITEPERMISSION_FIELD_NUMBER: _ClassVar[int]
    ALEXASKILLONLYSUPPORTSBUILTINLISTS_FIELD_NUMBER: _ClassVar[int]
    APPBADGEMODE_FIELD_NUMBER: _ClassVar[int]
    Always: PBMobileAppSettings.KeepScreenOnBehavior
    CLIENTHASSHOWNALEXAONBOARDING_FIELD_NUMBER: _ClassVar[int]
    CLIENTHASSHOWNGOOGLEASSISTANTONBOARDING_FIELD_NUMBER: _ClassVar[int]
    CROSSOFFGESTURE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTLISTIDFORALEXA_FIELD_NUMBER: _ClassVar[int]
    DEFAULTLISTID_FIELD_NUMBER: _ClassVar[int]
    DIDSUPPRESSACCOUNTNAMEPROMPT_FIELD_NUMBER: _ClassVar[int]
    HASMIGRATEDUSERCATEGORIESTOLISTCATEGORIES_FIELD_NUMBER: _ClassVar[int]
    HINTBANNERDISPLAYSTATS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ISACCOUNTLINKEDTOALEXASKILL_FIELD_NUMBER: _ClassVar[int]
    ISACCOUNTLINKEDTOGOOGLEASSISTANT_FIELD_NUMBER: _ClassVar[int]
    ISACTIVEGOOGLEASSISTANTPROVIDER_FIELD_NUMBER: _ClassVar[int]
    ISONLINESHOPPINGDISABLED_FIELD_NUMBER: _ClassVar[int]
    KEEPSCREENONBEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    LISTIDFORRECIPEINGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    LISTSSORTORDER_FIELD_NUMBER: _ClassVar[int]
    Never: PBMobileAppSettings.KeepScreenOnBehavior
    PROMPTTOLOADPHOTOSOVERCELLULARDATA_FIELD_NUMBER: _ClassVar[int]
    RECIPECOOKINGSTATES_FIELD_NUMBER: _ClassVar[int]
    REMINDERSAPPIMPORTENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULDAUTOIMPORTREMINDERS_FIELD_NUMBER: _ClassVar[int]
    SHOULDEXCLUDENEWLISTSFROMALEXABYDEFAULT_FIELD_NUMBER: _ClassVar[int]
    SHOULDNOTLINKNEWLISTSWITHGOOGLEASSISTANTBYDEFAULT_FIELD_NUMBER: _ClassVar[int]
    SHOULDPREVENTSCREENAUTOLOCK_FIELD_NUMBER: _ClassVar[int]
    SHOULDUSEMETRICUNITS_FIELD_NUMBER: _ClassVar[int]
    STARTERLISTSSORTORDER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNLINKEDALEXALISTS_FIELD_NUMBER: _ClassVar[int]
    UNLINKEDGOOGLEASSISTANTLISTS_FIELD_NUMBER: _ClassVar[int]
    WEBCURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    WEBCURRENCYSYMBOL_FIELD_NUMBER: _ClassVar[int]
    WEBDECIMALSEPARATOR_FIELD_NUMBER: _ClassVar[int]
    WEBHASHIDDENITEMPRICESHELP_FIELD_NUMBER: _ClassVar[int]
    WEBHASHIDDENSTORESANDFILTERSHELP_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDLISTFOLDERPATH_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDLISTID_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDMEALPLANTAB_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDRECIPECOLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDRECIPECOLLECTIONSETTINGSOVERRIDE_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDRECIPECOLLECTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDRECIPEID_FIELD_NUMBER: _ClassVar[int]
    WEBSELECTEDTABID_FIELD_NUMBER: _ClassVar[int]
    WhileCooking: PBMobileAppSettings.KeepScreenOnBehavior
    alexaApiEndpoint: str
    alexaSkillHasListReadPermission: bool
    alexaSkillHasListWritePermission: bool
    alexaSkillOnlySupportsBuiltInLists: bool
    appBadgeMode: str
    clientHasShownAlexaOnboarding: bool
    clientHasShownGoogleAssistantOnboarding: bool
    crossOffGesture: str
    defaultListId: str
    defaultListIdForAlexa: str
    didSuppressAccountNamePrompt: bool
    hasMigratedUserCategoriesToListCategories: bool
    hintBannerDisplayStats: _containers.RepeatedCompositeFieldContainer[PBHintBannerDisplayStats]
    identifier: str
    isAccountLinkedToAlexaSkill: bool
    isAccountLinkedToGoogleAssistant: bool
    isActiveGoogleAssistantProvider: bool
    isOnlineShoppingDisabled: bool
    keepScreenOnBehavior: int
    listIdForRecipeIngredients: str
    listsSortOrder: str
    promptToLoadPhotosOverCellularData: bool
    recipeCookingStates: _containers.RepeatedCompositeFieldContainer[PBRecipeCookingState]
    remindersAppImportEnabled: bool
    shouldAutoImportReminders: bool
    shouldExcludeNewListsFromAlexaByDefault: bool
    shouldNotLinkNewListsWithGoogleAssistantByDefault: bool
    shouldPreventScreenAutolock: bool
    shouldUseMetricUnits: bool
    starterListsSortOrder: str
    timestamp: float
    unlinkedAlexaLists: _containers.RepeatedCompositeFieldContainer[PBAlexaList]
    unlinkedGoogleAssistantLists: _containers.RepeatedCompositeFieldContainer[PBGoogleAssistantList]
    webCurrencyCode: str
    webCurrencySymbol: str
    webDecimalSeparator: str
    webHasHiddenItemPricesHelp: bool
    webHasHiddenStoresAndFiltersHelp: bool
    webSelectedListFolderPath: str
    webSelectedListId: str
    webSelectedMealPlanTab: int
    webSelectedRecipeCollectionId: str
    webSelectedRecipeCollectionSettingsOverride: PBRecipeCollectionSettings
    webSelectedRecipeCollectionType: int
    webSelectedRecipeId: str
    webSelectedTabId: str
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., defaultListId: _Optional[str] = ..., crossOffGesture: _Optional[str] = ..., listsSortOrder: _Optional[str] = ..., starterListsSortOrder: _Optional[str] = ..., remindersAppImportEnabled: bool = ..., appBadgeMode: _Optional[str] = ..., shouldAutoImportReminders: bool = ..., shouldPreventScreenAutolock: bool = ..., keepScreenOnBehavior: _Optional[int] = ..., promptToLoadPhotosOverCellularData: bool = ..., listIdForRecipeIngredients: _Optional[str] = ..., webSelectedListId: _Optional[str] = ..., webSelectedRecipeId: _Optional[str] = ..., webSelectedRecipeCollectionId: _Optional[str] = ..., webSelectedTabId: _Optional[str] = ..., webSelectedListFolderPath: _Optional[str] = ..., webSelectedMealPlanTab: _Optional[int] = ..., webHasHiddenStoresAndFiltersHelp: bool = ..., webHasHiddenItemPricesHelp: bool = ..., webDecimalSeparator: _Optional[str] = ..., webCurrencyCode: _Optional[str] = ..., webCurrencySymbol: _Optional[str] = ..., webSelectedRecipeCollectionType: _Optional[int] = ..., hintBannerDisplayStats: _Optional[_Iterable[_Union[PBHintBannerDisplayStats, _Mapping]]] = ..., webSelectedRecipeCollectionSettingsOverride: _Optional[_Union[PBRecipeCollectionSettings, _Mapping]] = ..., shouldUseMetricUnits: bool = ..., isAccountLinkedToAlexaSkill: bool = ..., alexaApiEndpoint: _Optional[str] = ..., shouldExcludeNewListsFromAlexaByDefault: bool = ..., defaultListIdForAlexa: _Optional[str] = ..., clientHasShownAlexaOnboarding: bool = ..., hasMigratedUserCategoriesToListCategories: bool = ..., recipeCookingStates: _Optional[_Iterable[_Union[PBRecipeCookingState, _Mapping]]] = ..., didSuppressAccountNamePrompt: bool = ..., isOnlineShoppingDisabled: bool = ..., unlinkedAlexaLists: _Optional[_Iterable[_Union[PBAlexaList, _Mapping]]] = ..., alexaSkillHasListReadPermission: bool = ..., alexaSkillHasListWritePermission: bool = ..., alexaSkillOnlySupportsBuiltInLists: bool = ..., isAccountLinkedToGoogleAssistant: bool = ..., shouldNotLinkNewListsWithGoogleAssistantByDefault: bool = ..., clientHasShownGoogleAssistantOnboarding: bool = ..., unlinkedGoogleAssistantLists: _Optional[_Iterable[_Union[PBGoogleAssistantList, _Mapping]]] = ..., isActiveGoogleAssistantProvider: bool = ...) -> None: ...

class PBMobileAppSettingsOperation(_message.Message):
    __slots__ = ["metadata", "updatedSettings"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATEDSETTINGS_FIELD_NUMBER: _ClassVar[int]
    metadata: PBOperationMetadata
    updatedSettings: PBMobileAppSettings
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., updatedSettings: _Optional[_Union[PBMobileAppSettings, _Mapping]] = ...) -> None: ...

class PBMobileAppSettingsOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBMobileAppSettingsOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBMobileAppSettingsOperation, _Mapping]]] = ...) -> None: ...

class PBNotificationLocation(_message.Message):
    __slots__ = ["address", "identifier", "latitude", "longitude", "name"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    address: str
    identifier: str
    latitude: float
    longitude: float
    name: str
    def __init__(self, identifier: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., name: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class PBOperationMetadata(_message.Message):
    __slots__ = ["handlerId", "operationClass", "operationId", "userId"]
    class OperationClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    HANDLERID_FIELD_NUMBER: _ClassVar[int]
    ListCategorizationRuleOperation: PBOperationMetadata.OperationClass
    ListCategoryGroupOperation: PBOperationMetadata.OperationClass
    ListCategoryOperation: PBOperationMetadata.OperationClass
    OPERATIONCLASS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONID_FIELD_NUMBER: _ClassVar[int]
    StoreFilterOperation: PBOperationMetadata.OperationClass
    StoreOperation: PBOperationMetadata.OperationClass
    USERID_FIELD_NUMBER: _ClassVar[int]
    UndefinedOperation: PBOperationMetadata.OperationClass
    handlerId: str
    operationClass: int
    operationId: str
    userId: str
    def __init__(self, operationId: _Optional[str] = ..., handlerId: _Optional[str] = ..., userId: _Optional[str] = ..., operationClass: _Optional[int] = ...) -> None: ...

class PBOrderedShoppingListIDsOperation(_message.Message):
    __slots__ = ["metadata", "orderedListIds"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORDEREDLISTIDS_FIELD_NUMBER: _ClassVar[int]
    metadata: PBOperationMetadata
    orderedListIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., orderedListIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBOrderedShoppingListIDsOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBOrderedShoppingListIDsOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBOrderedShoppingListIDsOperation, _Mapping]]] = ...) -> None: ...

class PBOrderedStarterListIDsOperation(_message.Message):
    __slots__ = ["metadata", "orderedListIds"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORDEREDLISTIDS_FIELD_NUMBER: _ClassVar[int]
    metadata: PBOperationMetadata
    orderedListIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., orderedListIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBOrderedStarterListIDsOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBOrderedStarterListIDsOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBOrderedStarterListIDsOperation, _Mapping]]] = ...) -> None: ...

class PBProductLookupResponse(_message.Message):
    __slots__ = ["listItem"]
    LISTITEM_FIELD_NUMBER: _ClassVar[int]
    listItem: ListItem
    def __init__(self, listItem: _Optional[_Union[ListItem, _Mapping]] = ...) -> None: ...

class PBRecipe(_message.Message):
    __slots__ = ["adCampaignId", "cookTime", "creationTimestamp", "icon", "identifier", "ingredients", "name", "note", "nutritionalInfo", "paprikaIdentifier", "photoIds", "photoUrls", "prepTime", "preparationSteps", "rating", "recipeDataId", "scaleFactor", "servings", "sourceName", "sourceUrl", "timestamp"]
    ADCAMPAIGNID_FIELD_NUMBER: _ClassVar[int]
    COOKTIME_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NUTRITIONALINFO_FIELD_NUMBER: _ClassVar[int]
    PAPRIKAIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PHOTOIDS_FIELD_NUMBER: _ClassVar[int]
    PHOTOURLS_FIELD_NUMBER: _ClassVar[int]
    PREPARATIONSTEPS_FIELD_NUMBER: _ClassVar[int]
    PREPTIME_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    RECIPEDATAID_FIELD_NUMBER: _ClassVar[int]
    SCALEFACTOR_FIELD_NUMBER: _ClassVar[int]
    SERVINGS_FIELD_NUMBER: _ClassVar[int]
    SOURCENAME_FIELD_NUMBER: _ClassVar[int]
    SOURCEURL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    adCampaignId: str
    cookTime: int
    creationTimestamp: float
    icon: str
    identifier: str
    ingredients: _containers.RepeatedCompositeFieldContainer[PBIngredient]
    name: str
    note: str
    nutritionalInfo: str
    paprikaIdentifier: str
    photoIds: _containers.RepeatedScalarFieldContainer[str]
    photoUrls: _containers.RepeatedScalarFieldContainer[str]
    prepTime: int
    preparationSteps: _containers.RepeatedScalarFieldContainer[str]
    rating: int
    recipeDataId: str
    scaleFactor: float
    servings: str
    sourceName: str
    sourceUrl: str
    timestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., note: _Optional[str] = ..., sourceName: _Optional[str] = ..., sourceUrl: _Optional[str] = ..., ingredients: _Optional[_Iterable[_Union[PBIngredient, _Mapping]]] = ..., preparationSteps: _Optional[_Iterable[str]] = ..., photoIds: _Optional[_Iterable[str]] = ..., adCampaignId: _Optional[str] = ..., photoUrls: _Optional[_Iterable[str]] = ..., scaleFactor: _Optional[float] = ..., rating: _Optional[int] = ..., creationTimestamp: _Optional[float] = ..., nutritionalInfo: _Optional[str] = ..., cookTime: _Optional[int] = ..., prepTime: _Optional[int] = ..., servings: _Optional[str] = ..., paprikaIdentifier: _Optional[str] = ..., recipeDataId: _Optional[str] = ...) -> None: ...

class PBRecipeCollection(_message.Message):
    __slots__ = ["collectionSettings", "identifier", "name", "recipeIds", "timestamp"]
    COLLECTIONSETTINGS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPEIDS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    collectionSettings: PBRecipeCollectionSettings
    identifier: str
    name: str
    recipeIds: _containers.RepeatedScalarFieldContainer[str]
    timestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., name: _Optional[str] = ..., recipeIds: _Optional[_Iterable[str]] = ..., collectionSettings: _Optional[_Union[PBRecipeCollectionSettings, _Mapping]] = ...) -> None: ...

class PBRecipeCollectionSettings(_message.Message):
    __slots__ = ["collectionsSortOrder", "icon", "recipesSortOrder", "showOnlyRecipesWithNoCollection", "smartFilter", "timestamp", "useReversedCollectionsSortDirection", "useReversedSortDirection"]
    class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AlphabeticalSortOrder: PBRecipeCollectionSettings.SortOrder
    COLLECTIONSSORTORDER_FIELD_NUMBER: _ClassVar[int]
    CookTimeSortOrder: PBRecipeCollectionSettings.SortOrder
    DateCreatedSortOrder: PBRecipeCollectionSettings.SortOrder
    ICON_FIELD_NUMBER: _ClassVar[int]
    ManualSortOrder: PBRecipeCollectionSettings.SortOrder
    PrepTimeSortOrder: PBRecipeCollectionSettings.SortOrder
    RECIPESSORTORDER_FIELD_NUMBER: _ClassVar[int]
    RatingSortOrder: PBRecipeCollectionSettings.SortOrder
    RecipeCountSortOrder: PBRecipeCollectionSettings.SortOrder
    SHOWONLYRECIPESWITHNOCOLLECTION_FIELD_NUMBER: _ClassVar[int]
    SMARTFILTER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USEREVERSEDCOLLECTIONSSORTDIRECTION_FIELD_NUMBER: _ClassVar[int]
    USEREVERSEDSORTDIRECTION_FIELD_NUMBER: _ClassVar[int]
    collectionsSortOrder: int
    icon: PBIcon
    recipesSortOrder: int
    showOnlyRecipesWithNoCollection: bool
    smartFilter: PBSmartFilter
    timestamp: float
    useReversedCollectionsSortDirection: bool
    useReversedSortDirection: bool
    def __init__(self, timestamp: _Optional[float] = ..., recipesSortOrder: _Optional[int] = ..., useReversedSortDirection: bool = ..., collectionsSortOrder: _Optional[int] = ..., useReversedCollectionsSortDirection: bool = ..., smartFilter: _Optional[_Union[PBSmartFilter, _Mapping]] = ..., icon: _Optional[_Union[PBIcon, _Mapping]] = ..., showOnlyRecipesWithNoCollection: bool = ...) -> None: ...

class PBRecipeCookingState(_message.Message):
    __slots__ = ["checkedIngredientIds", "eventId", "lastOpenedTimestamp", "recipeId", "selectedStepNumber", "selectedTabId"]
    CHECKEDINGREDIENTIDS_FIELD_NUMBER: _ClassVar[int]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    LASTOPENEDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECIPEID_FIELD_NUMBER: _ClassVar[int]
    SELECTEDSTEPNUMBER_FIELD_NUMBER: _ClassVar[int]
    SELECTEDTABID_FIELD_NUMBER: _ClassVar[int]
    checkedIngredientIds: _containers.RepeatedScalarFieldContainer[str]
    eventId: str
    lastOpenedTimestamp: float
    recipeId: str
    selectedStepNumber: int
    selectedTabId: int
    def __init__(self, recipeId: _Optional[str] = ..., eventId: _Optional[str] = ..., lastOpenedTimestamp: _Optional[float] = ..., selectedTabId: _Optional[int] = ..., checkedIngredientIds: _Optional[_Iterable[str]] = ..., selectedStepNumber: _Optional[int] = ...) -> None: ...

class PBRecipeDataArchive(_message.Message):
    __slots__ = ["recipeCollections", "recipes"]
    RECIPECOLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    recipeCollections: _containers.RepeatedCompositeFieldContainer[PBRecipeCollection]
    recipes: _containers.RepeatedCompositeFieldContainer[PBRecipe]
    def __init__(self, recipes: _Optional[_Iterable[_Union[PBRecipe, _Mapping]]] = ..., recipeCollections: _Optional[_Iterable[_Union[PBRecipeCollection, _Mapping]]] = ...) -> None: ...

class PBRecipeDataResponse(_message.Message):
    __slots__ = ["allRecipesCollection", "hasImportedPunchforkRecipes", "includesRecipeCollectionIds", "linkedUsers", "maxRecipeCount", "pendingRecipeLinkRequests", "recipeCollectionIds", "recipeCollections", "recipeDataId", "recipeLinkRequestsToConfirm", "recipes", "settingsMapForSystemCollections", "timestamp"]
    ALLRECIPESCOLLECTION_FIELD_NUMBER: _ClassVar[int]
    HASIMPORTEDPUNCHFORKRECIPES_FIELD_NUMBER: _ClassVar[int]
    INCLUDESRECIPECOLLECTIONIDS_FIELD_NUMBER: _ClassVar[int]
    LINKEDUSERS_FIELD_NUMBER: _ClassVar[int]
    MAXRECIPECOUNT_FIELD_NUMBER: _ClassVar[int]
    PENDINGRECIPELINKREQUESTS_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTIONIDS_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    RECIPEDATAID_FIELD_NUMBER: _ClassVar[int]
    RECIPELINKREQUESTSTOCONFIRM_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    SETTINGSMAPFORSYSTEMCOLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    allRecipesCollection: PBRecipeCollection
    hasImportedPunchforkRecipes: bool
    includesRecipeCollectionIds: bool
    linkedUsers: _containers.RepeatedCompositeFieldContainer[PBEmailUserIDPair]
    maxRecipeCount: int
    pendingRecipeLinkRequests: _containers.RepeatedCompositeFieldContainer[PBRecipeLinkRequest]
    recipeCollectionIds: _containers.RepeatedScalarFieldContainer[str]
    recipeCollections: _containers.RepeatedCompositeFieldContainer[PBRecipeCollection]
    recipeDataId: str
    recipeLinkRequestsToConfirm: _containers.RepeatedCompositeFieldContainer[PBRecipeLinkRequest]
    recipes: _containers.RepeatedCompositeFieldContainer[PBRecipe]
    settingsMapForSystemCollections: PBRecipeCollectionSettings
    timestamp: float
    def __init__(self, timestamp: _Optional[float] = ..., allRecipesCollection: _Optional[_Union[PBRecipeCollection, _Mapping]] = ..., recipes: _Optional[_Iterable[_Union[PBRecipe, _Mapping]]] = ..., recipeCollectionIds: _Optional[_Iterable[str]] = ..., recipeCollections: _Optional[_Iterable[_Union[PBRecipeCollection, _Mapping]]] = ..., pendingRecipeLinkRequests: _Optional[_Iterable[_Union[PBRecipeLinkRequest, _Mapping]]] = ..., recipeLinkRequestsToConfirm: _Optional[_Iterable[_Union[PBRecipeLinkRequest, _Mapping]]] = ..., linkedUsers: _Optional[_Iterable[_Union[PBEmailUserIDPair, _Mapping]]] = ..., recipeDataId: _Optional[str] = ..., hasImportedPunchforkRecipes: bool = ..., includesRecipeCollectionIds: bool = ..., maxRecipeCount: _Optional[int] = ..., settingsMapForSystemCollections: _Optional[_Union[PBRecipeCollectionSettings, _Mapping]] = ...) -> None: ...

class PBRecipeLinkRequest(_message.Message):
    __slots__ = ["confirmingEmail", "confirmingName", "confirmingUserId", "identifier", "requestingEmail", "requestingName", "requestingUserId"]
    CONFIRMINGEMAIL_FIELD_NUMBER: _ClassVar[int]
    CONFIRMINGNAME_FIELD_NUMBER: _ClassVar[int]
    CONFIRMINGUSERID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REQUESTINGEMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUESTINGNAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTINGUSERID_FIELD_NUMBER: _ClassVar[int]
    confirmingEmail: str
    confirmingName: str
    confirmingUserId: str
    identifier: str
    requestingEmail: str
    requestingName: str
    requestingUserId: str
    def __init__(self, identifier: _Optional[str] = ..., requestingUserId: _Optional[str] = ..., requestingEmail: _Optional[str] = ..., requestingName: _Optional[str] = ..., confirmingUserId: _Optional[str] = ..., confirmingEmail: _Optional[str] = ..., confirmingName: _Optional[str] = ...) -> None: ...

class PBRecipeLinkRequestList(_message.Message):
    __slots__ = ["recipeLinkRequest"]
    RECIPELINKREQUEST_FIELD_NUMBER: _ClassVar[int]
    recipeLinkRequest: _containers.RepeatedCompositeFieldContainer[PBRecipeLinkRequest]
    def __init__(self, recipeLinkRequest: _Optional[_Iterable[_Union[PBRecipeLinkRequest, _Mapping]]] = ...) -> None: ...

class PBRecipeLinkRequestResponse(_message.Message):
    __slots__ = ["errorMessage", "errorTitle", "recipeDataResponse", "statusCode"]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORTITLE_FIELD_NUMBER: _ClassVar[int]
    RECIPEDATARESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    errorMessage: str
    errorTitle: str
    recipeDataResponse: PBRecipeDataResponse
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., recipeDataResponse: _Optional[_Union[PBRecipeDataResponse, _Mapping]] = ..., errorTitle: _Optional[str] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class PBRecipeList(_message.Message):
    __slots__ = ["recipes"]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    recipes: _containers.RepeatedCompositeFieldContainer[PBRecipe]
    def __init__(self, recipes: _Optional[_Iterable[_Union[PBRecipe, _Mapping]]] = ...) -> None: ...

class PBRecipeOperation(_message.Message):
    __slots__ = ["isNewRecipeFromWebImport", "maxRecipeCount", "metadata", "recipe", "recipeCollection", "recipeCollectionIds", "recipeDataId", "recipeEventIds", "recipeIds", "recipeLinkRequest", "recipes"]
    ISNEWRECIPEFROMWEBIMPORT_FIELD_NUMBER: _ClassVar[int]
    MAXRECIPECOUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTIONIDS_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTION_FIELD_NUMBER: _ClassVar[int]
    RECIPEDATAID_FIELD_NUMBER: _ClassVar[int]
    RECIPEEVENTIDS_FIELD_NUMBER: _ClassVar[int]
    RECIPEIDS_FIELD_NUMBER: _ClassVar[int]
    RECIPELINKREQUEST_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    isNewRecipeFromWebImport: bool
    maxRecipeCount: int
    metadata: PBOperationMetadata
    recipe: PBRecipe
    recipeCollection: PBRecipeCollection
    recipeCollectionIds: _containers.RepeatedScalarFieldContainer[str]
    recipeDataId: str
    recipeEventIds: _containers.RepeatedScalarFieldContainer[str]
    recipeIds: _containers.RepeatedScalarFieldContainer[str]
    recipeLinkRequest: PBRecipeLinkRequest
    recipes: _containers.RepeatedCompositeFieldContainer[PBRecipe]
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., recipeDataId: _Optional[str] = ..., recipe: _Optional[_Union[PBRecipe, _Mapping]] = ..., recipeCollection: _Optional[_Union[PBRecipeCollection, _Mapping]] = ..., recipeLinkRequest: _Optional[_Union[PBRecipeLinkRequest, _Mapping]] = ..., recipeCollectionIds: _Optional[_Iterable[str]] = ..., recipes: _Optional[_Iterable[_Union[PBRecipe, _Mapping]]] = ..., isNewRecipeFromWebImport: bool = ..., recipeIds: _Optional[_Iterable[str]] = ..., recipeEventIds: _Optional[_Iterable[str]] = ..., maxRecipeCount: _Optional[int] = ...) -> None: ...

class PBRecipeOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBRecipeOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBRecipeOperation, _Mapping]]] = ...) -> None: ...

class PBRecipeWebImportResponse(_message.Message):
    __slots__ = ["freeRecipeImportsRemainingCount", "isPremiumUser", "recipe", "siteSpecificHelpText", "statusCode"]
    FREERECIPEIMPORTSREMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISPREMIUMUSER_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    SITESPECIFICHELPTEXT_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    freeRecipeImportsRemainingCount: int
    isPremiumUser: bool
    recipe: PBRecipe
    siteSpecificHelpText: str
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., recipe: _Optional[_Union[PBRecipe, _Mapping]] = ..., isPremiumUser: bool = ..., siteSpecificHelpText: _Optional[str] = ..., freeRecipeImportsRemainingCount: _Optional[int] = ...) -> None: ...

class PBRedemptionCodeInfo(_message.Message):
    __slots__ = ["creationTimestamp", "identifier", "purchasingUserId", "redeemingUserId", "redemptionCode", "redemptionTimestamp", "subscriptionType", "wasPurchased"]
    CREATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PURCHASINGUSERID_FIELD_NUMBER: _ClassVar[int]
    REDEEMINGUSERID_FIELD_NUMBER: _ClassVar[int]
    REDEMPTIONCODE_FIELD_NUMBER: _ClassVar[int]
    REDEMPTIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    WASPURCHASED_FIELD_NUMBER: _ClassVar[int]
    creationTimestamp: float
    identifier: str
    purchasingUserId: str
    redeemingUserId: str
    redemptionCode: str
    redemptionTimestamp: float
    subscriptionType: int
    wasPurchased: bool
    def __init__(self, identifier: _Optional[str] = ..., redemptionCode: _Optional[str] = ..., purchasingUserId: _Optional[str] = ..., redeemingUserId: _Optional[str] = ..., redemptionTimestamp: _Optional[float] = ..., subscriptionType: _Optional[int] = ..., creationTimestamp: _Optional[float] = ..., wasPurchased: bool = ...) -> None: ...

class PBRedemptionCodeResponse(_message.Message):
    __slots__ = ["accountInfo", "errorMessage", "errorTitle", "statusCode"]
    ACCOUNTINFO_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORTITLE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    accountInfo: PBAccountInfoResponse
    errorMessage: str
    errorTitle: str
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., accountInfo: _Optional[_Union[PBAccountInfoResponse, _Mapping]] = ..., errorTitle: _Optional[str] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class PBSavedRecipeOperation(_message.Message):
    __slots__ = ["metadata", "recipeId"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RECIPEID_FIELD_NUMBER: _ClassVar[int]
    metadata: PBOperationMetadata
    recipeId: str
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., recipeId: _Optional[str] = ...) -> None: ...

class PBSavedRecipeOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBSavedRecipeOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBSavedRecipeOperation, _Mapping]]] = ...) -> None: ...

class PBShareListOperationResponse(_message.Message):
    __slots__ = ["errorMessage", "errorTitle", "originalListTimestamp", "sharedUser", "statusCode", "updatedListTimestamp"]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORTITLE_FIELD_NUMBER: _ClassVar[int]
    ORIGINALLISTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SHAREDUSER_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDLISTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    errorMessage: str
    errorTitle: str
    originalListTimestamp: float
    sharedUser: PBEmailUserIDPair
    statusCode: int
    updatedListTimestamp: float
    def __init__(self, sharedUser: _Optional[_Union[PBEmailUserIDPair, _Mapping]] = ..., originalListTimestamp: _Optional[float] = ..., updatedListTimestamp: _Optional[float] = ..., statusCode: _Optional[int] = ..., errorTitle: _Optional[str] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class PBShoppingListArchive(_message.Message):
    __slots__ = ["categorizationRules", "favoriteItems", "listCategoryGroups", "listSettings", "recentItems", "shoppingList", "storeFilters", "stores"]
    CATEGORIZATIONRULES_FIELD_NUMBER: _ClassVar[int]
    FAVORITEITEMS_FIELD_NUMBER: _ClassVar[int]
    LISTCATEGORYGROUPS_FIELD_NUMBER: _ClassVar[int]
    LISTSETTINGS_FIELD_NUMBER: _ClassVar[int]
    RECENTITEMS_FIELD_NUMBER: _ClassVar[int]
    SHOPPINGLIST_FIELD_NUMBER: _ClassVar[int]
    STOREFILTERS_FIELD_NUMBER: _ClassVar[int]
    STORES_FIELD_NUMBER: _ClassVar[int]
    categorizationRules: _containers.RepeatedCompositeFieldContainer[PBListCategorizationRule]
    favoriteItems: StarterList
    listCategoryGroups: _containers.RepeatedCompositeFieldContainer[PBListCategoryGroup]
    listSettings: PBListSettings
    recentItems: StarterList
    shoppingList: ShoppingList
    storeFilters: _containers.RepeatedCompositeFieldContainer[PBStoreFilter]
    stores: _containers.RepeatedCompositeFieldContainer[PBStore]
    def __init__(self, shoppingList: _Optional[_Union[ShoppingList, _Mapping]] = ..., listSettings: _Optional[_Union[PBListSettings, _Mapping]] = ..., listCategoryGroups: _Optional[_Iterable[_Union[PBListCategoryGroup, _Mapping]]] = ..., stores: _Optional[_Iterable[_Union[PBStore, _Mapping]]] = ..., storeFilters: _Optional[_Iterable[_Union[PBStoreFilter, _Mapping]]] = ..., categorizationRules: _Optional[_Iterable[_Union[PBListCategorizationRule, _Mapping]]] = ..., favoriteItems: _Optional[_Union[StarterList, _Mapping]] = ..., recentItems: _Optional[_Union[StarterList, _Mapping]] = ...) -> None: ...

class PBSmartCondition(_message.Message):
    __slots__ = ["fieldID", "operatorID", "value"]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    OPERATORID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    fieldID: str
    operatorID: str
    value: str
    def __init__(self, fieldID: _Optional[str] = ..., operatorID: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class PBSmartFilter(_message.Message):
    __slots__ = ["conditions", "identifier", "logicalTimestamp", "name", "requiresMatchingAllConditions"]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRESMATCHINGALLCONDITIONS_FIELD_NUMBER: _ClassVar[int]
    conditions: _containers.RepeatedCompositeFieldContainer[PBSmartCondition]
    identifier: str
    logicalTimestamp: int
    name: str
    requiresMatchingAllConditions: bool
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., name: _Optional[str] = ..., requiresMatchingAllConditions: bool = ..., conditions: _Optional[_Iterable[_Union[PBSmartCondition, _Mapping]]] = ...) -> None: ...

class PBStarterListOperation(_message.Message):
    __slots__ = ["itemPrice", "list", "listId", "listItem", "listItemId", "metadata", "originalValue", "updatedValue"]
    ITEMPRICE_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LISTITEMID_FIELD_NUMBER: _ClassVar[int]
    LISTITEM_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORIGINALVALUE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDVALUE_FIELD_NUMBER: _ClassVar[int]
    itemPrice: PBItemPrice
    list: StarterList
    listId: str
    listItem: ListItem
    listItemId: str
    metadata: PBOperationMetadata
    originalValue: str
    updatedValue: str
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., listId: _Optional[str] = ..., listItemId: _Optional[str] = ..., updatedValue: _Optional[str] = ..., originalValue: _Optional[str] = ..., listItem: _Optional[_Union[ListItem, _Mapping]] = ..., list: _Optional[_Union[StarterList, _Mapping]] = ..., itemPrice: _Optional[_Union[PBItemPrice, _Mapping]] = ...) -> None: ...

class PBStarterListOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBStarterListOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBStarterListOperation, _Mapping]]] = ...) -> None: ...

class PBStore(_message.Message):
    __slots__ = ["identifier", "listId", "logicalTimestamp", "name", "sortIndex"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SORTINDEX_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    listId: str
    logicalTimestamp: int
    name: str
    sortIndex: int
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., listId: _Optional[str] = ..., name: _Optional[str] = ..., sortIndex: _Optional[int] = ...) -> None: ...

class PBStoreFilter(_message.Message):
    __slots__ = ["identifier", "includesUnassignedItems", "listCategoryGroupId", "listId", "logicalTimestamp", "name", "showsAllItems", "sortIndex", "storeIds"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INCLUDESUNASSIGNEDITEMS_FIELD_NUMBER: _ClassVar[int]
    LISTCATEGORYGROUPID_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHOWSALLITEMS_FIELD_NUMBER: _ClassVar[int]
    SORTINDEX_FIELD_NUMBER: _ClassVar[int]
    STOREIDS_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    includesUnassignedItems: bool
    listCategoryGroupId: str
    listId: str
    logicalTimestamp: int
    name: str
    showsAllItems: bool
    sortIndex: int
    storeIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, identifier: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., listId: _Optional[str] = ..., name: _Optional[str] = ..., storeIds: _Optional[_Iterable[str]] = ..., includesUnassignedItems: bool = ..., sortIndex: _Optional[int] = ..., listCategoryGroupId: _Optional[str] = ..., showsAllItems: bool = ...) -> None: ...

class PBStripeCharge(_message.Message):
    __slots__ = ["charge", "chargeId"]
    CHARGEID_FIELD_NUMBER: _ClassVar[int]
    CHARGE_FIELD_NUMBER: _ClassVar[int]
    charge: str
    chargeId: str
    def __init__(self, chargeId: _Optional[str] = ..., charge: _Optional[str] = ...) -> None: ...

class PBStripeSubscriptionInvoice(_message.Message):
    __slots__ = ["invoiceId", "subscription", "subscriptionId"]
    INVOICEID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    invoiceId: str
    subscription: str
    subscriptionId: str
    def __init__(self, subscriptionId: _Optional[str] = ..., invoiceId: _Optional[str] = ..., subscription: _Optional[str] = ...) -> None: ...

class PBSyncOperation(_message.Message):
    __slots__ = ["encodedOperation", "identifier", "operationClassName", "operationQueueId"]
    ENCODEDOPERATION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OPERATIONCLASSNAME_FIELD_NUMBER: _ClassVar[int]
    OPERATIONQUEUEID_FIELD_NUMBER: _ClassVar[int]
    encodedOperation: bytes
    identifier: str
    operationClassName: str
    operationQueueId: str
    def __init__(self, identifier: _Optional[str] = ..., operationQueueId: _Optional[str] = ..., operationClassName: _Optional[str] = ..., encodedOperation: _Optional[bytes] = ...) -> None: ...

class PBTimestamp(_message.Message):
    __slots__ = ["identifier", "timestamp"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    timestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ...) -> None: ...

class PBTimestampList(_message.Message):
    __slots__ = ["timestamps"]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    timestamps: _containers.RepeatedCompositeFieldContainer[PBTimestamp]
    def __init__(self, timestamps: _Optional[_Iterable[_Union[PBTimestamp, _Mapping]]] = ...) -> None: ...

class PBUserCategory(_message.Message):
    __slots__ = ["categoryMatchId", "fromSharedList", "icon", "identifier", "name", "systemCategory", "timestamp", "userId"]
    CATEGORYMATCHID_FIELD_NUMBER: _ClassVar[int]
    FROMSHAREDLIST_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEMCATEGORY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    categoryMatchId: str
    fromSharedList: bool
    icon: str
    identifier: str
    name: str
    systemCategory: str
    timestamp: float
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., userId: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., systemCategory: _Optional[str] = ..., categoryMatchId: _Optional[str] = ..., fromSharedList: bool = ..., timestamp: _Optional[float] = ...) -> None: ...

class PBUserCategoryData(_message.Message):
    __slots__ = ["categories", "groupings", "hasMigratedCategoryOrderings", "identifier", "requiresRefreshTimestamp", "timestamp"]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    GROUPINGS_FIELD_NUMBER: _ClassVar[int]
    HASMIGRATEDCATEGORYORDERINGS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REQUIRESREFRESHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[PBUserCategory]
    groupings: _containers.RepeatedCompositeFieldContainer[PBCategoryGrouping]
    hasMigratedCategoryOrderings: bool
    identifier: str
    requiresRefreshTimestamp: float
    timestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., requiresRefreshTimestamp: _Optional[float] = ..., categories: _Optional[_Iterable[_Union[PBUserCategory, _Mapping]]] = ..., groupings: _Optional[_Iterable[_Union[PBCategoryGrouping, _Mapping]]] = ..., hasMigratedCategoryOrderings: bool = ...) -> None: ...

class PBUserCategoryOperation(_message.Message):
    __slots__ = ["category", "grouping", "metadata"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    GROUPING_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    category: PBUserCategory
    grouping: PBCategoryGrouping
    metadata: PBOperationMetadata
    def __init__(self, metadata: _Optional[_Union[PBOperationMetadata, _Mapping]] = ..., category: _Optional[_Union[PBUserCategory, _Mapping]] = ..., grouping: _Optional[_Union[PBCategoryGrouping, _Mapping]] = ...) -> None: ...

class PBUserCategoryOperationList(_message.Message):
    __slots__ = ["operations"]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[PBUserCategoryOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[PBUserCategoryOperation, _Mapping]]] = ...) -> None: ...

class PBUserDataClientTimestamps(_message.Message):
    __slots__ = ["categorizedItemsTimestamp", "favoriteItemTimestamps", "listFolderTimestamps", "listSettingsTimestamp", "mealPlanningCalendarTimestamp", "mobileAppSettingsTimestamp", "orderedStarterListIdsTimestamp", "recentItemTimestamps", "shoppingListLogicalTimestamps", "shoppingListTimestamps", "starterListSettingsTimestamp", "starterListTimestamps", "userCategoriesTimestamp", "userRecipeDataTimestamp"]
    CATEGORIZEDITEMSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FAVORITEITEMTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    LISTFOLDERTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    LISTSETTINGSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MEALPLANNINGCALENDARTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MOBILEAPPSETTINGSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDEREDSTARTERLISTIDSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECENTITEMTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    SHOPPINGLISTLOGICALTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    SHOPPINGLISTTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    STARTERLISTSETTINGSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STARTERLISTTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    USERCATEGORIESTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERRECIPEDATATIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    categorizedItemsTimestamp: PBTimestamp
    favoriteItemTimestamps: PBTimestampList
    listFolderTimestamps: PBListFolderTimestamps
    listSettingsTimestamp: PBTimestamp
    mealPlanningCalendarTimestamp: PBLogicalTimestamp
    mobileAppSettingsTimestamp: PBTimestamp
    orderedStarterListIdsTimestamp: PBTimestamp
    recentItemTimestamps: PBTimestampList
    shoppingListLogicalTimestamps: PBLogicalTimestampList
    shoppingListTimestamps: PBTimestampList
    starterListSettingsTimestamp: PBTimestamp
    starterListTimestamps: PBTimestampList
    userCategoriesTimestamp: PBTimestamp
    userRecipeDataTimestamp: PBTimestamp
    def __init__(self, shoppingListTimestamps: _Optional[_Union[PBTimestampList, _Mapping]] = ..., listFolderTimestamps: _Optional[_Union[PBListFolderTimestamps, _Mapping]] = ..., userRecipeDataTimestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., mealPlanningCalendarTimestamp: _Optional[_Union[PBLogicalTimestamp, _Mapping]] = ..., categorizedItemsTimestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., userCategoriesTimestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., starterListTimestamps: _Optional[_Union[PBTimestampList, _Mapping]] = ..., recentItemTimestamps: _Optional[_Union[PBTimestampList, _Mapping]] = ..., favoriteItemTimestamps: _Optional[_Union[PBTimestampList, _Mapping]] = ..., orderedStarterListIdsTimestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., listSettingsTimestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., starterListSettingsTimestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., mobileAppSettingsTimestamp: _Optional[_Union[PBTimestamp, _Mapping]] = ..., shoppingListLogicalTimestamps: _Optional[_Union[PBLogicalTimestampList, _Mapping]] = ...) -> None: ...

class PBUserDataResponse(_message.Message):
    __slots__ = ["categorizedItemsResponse", "listFoldersResponse", "listSettingsResponse", "mealPlanningCalendarResponse", "mobileAppSettingsResponse", "orderedStarterListIdsResponse", "recipeDataResponse", "shoppingListsResponse", "starterListSettingsResponse", "starterListsResponse", "userCategoriesResponse"]
    CATEGORIZEDITEMSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    LISTFOLDERSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    LISTSETTINGSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    MEALPLANNINGCALENDARRESPONSE_FIELD_NUMBER: _ClassVar[int]
    MOBILEAPPSETTINGSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    ORDEREDSTARTERLISTIDSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    RECIPEDATARESPONSE_FIELD_NUMBER: _ClassVar[int]
    SHOPPINGLISTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    STARTERLISTSETTINGSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    STARTERLISTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    USERCATEGORIESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    categorizedItemsResponse: PBCategorizedItemsList
    listFoldersResponse: PBListFoldersResponse
    listSettingsResponse: PBListSettingsList
    mealPlanningCalendarResponse: PBCalendarResponse
    mobileAppSettingsResponse: PBMobileAppSettings
    orderedStarterListIdsResponse: PBIdentifierList
    recipeDataResponse: PBRecipeDataResponse
    shoppingListsResponse: ShoppingListsResponse
    starterListSettingsResponse: PBListSettingsList
    starterListsResponse: StarterListsResponseV2
    userCategoriesResponse: PBUserCategoryData
    def __init__(self, shoppingListsResponse: _Optional[_Union[ShoppingListsResponse, _Mapping]] = ..., listFoldersResponse: _Optional[_Union[PBListFoldersResponse, _Mapping]] = ..., recipeDataResponse: _Optional[_Union[PBRecipeDataResponse, _Mapping]] = ..., mealPlanningCalendarResponse: _Optional[_Union[PBCalendarResponse, _Mapping]] = ..., categorizedItemsResponse: _Optional[_Union[PBCategorizedItemsList, _Mapping]] = ..., userCategoriesResponse: _Optional[_Union[PBUserCategoryData, _Mapping]] = ..., starterListsResponse: _Optional[_Union[StarterListsResponseV2, _Mapping]] = ..., orderedStarterListIdsResponse: _Optional[_Union[PBIdentifierList, _Mapping]] = ..., listSettingsResponse: _Optional[_Union[PBListSettingsList, _Mapping]] = ..., starterListSettingsResponse: _Optional[_Union[PBListSettingsList, _Mapping]] = ..., mobileAppSettingsResponse: _Optional[_Union[PBMobileAppSettings, _Mapping]] = ...) -> None: ...

class PBUserEmailInfo(_message.Message):
    __slots__ = ["identifier", "sentMessageIdentifiers", "shouldSendNewsletters", "shouldSendOnboardingTips", "shouldSendSubscriptionLifecycleMessages", "unsubscribeId"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SENTMESSAGEIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    SHOULDSENDNEWSLETTERS_FIELD_NUMBER: _ClassVar[int]
    SHOULDSENDONBOARDINGTIPS_FIELD_NUMBER: _ClassVar[int]
    SHOULDSENDSUBSCRIPTIONLIFECYCLEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBEID_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    sentMessageIdentifiers: _containers.RepeatedScalarFieldContainer[str]
    shouldSendNewsletters: bool
    shouldSendOnboardingTips: bool
    shouldSendSubscriptionLifecycleMessages: bool
    unsubscribeId: str
    def __init__(self, identifier: _Optional[str] = ..., unsubscribeId: _Optional[str] = ..., sentMessageIdentifiers: _Optional[_Iterable[str]] = ..., shouldSendNewsletters: bool = ..., shouldSendOnboardingTips: bool = ..., shouldSendSubscriptionLifecycleMessages: bool = ...) -> None: ...

class PBUserListData(_message.Message):
    __slots__ = ["categorizedItemsRequireRefreshTimestamp", "categorizedItemsTimestamp", "hasMigratedListOrdering", "identifier", "listIds", "listIdsTimestamp", "rootFolderId", "rootFolderIdTimestamp", "timestamp", "userIds", "userIdsTimestamp"]
    CATEGORIZEDITEMSREQUIREREFRESHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CATEGORIZEDITEMSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HASMIGRATEDLISTORDERING_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LISTIDSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LISTIDS_FIELD_NUMBER: _ClassVar[int]
    ROOTFOLDERIDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ROOTFOLDERID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERIDSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    categorizedItemsRequireRefreshTimestamp: float
    categorizedItemsTimestamp: float
    hasMigratedListOrdering: bool
    identifier: str
    listIds: _containers.RepeatedScalarFieldContainer[str]
    listIdsTimestamp: float
    rootFolderId: str
    rootFolderIdTimestamp: float
    timestamp: float
    userIds: _containers.RepeatedScalarFieldContainer[str]
    userIdsTimestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., userIds: _Optional[_Iterable[str]] = ..., userIdsTimestamp: _Optional[float] = ..., listIds: _Optional[_Iterable[str]] = ..., listIdsTimestamp: _Optional[float] = ..., rootFolderId: _Optional[str] = ..., rootFolderIdTimestamp: _Optional[float] = ..., categorizedItemsTimestamp: _Optional[float] = ..., categorizedItemsRequireRefreshTimestamp: _Optional[float] = ..., hasMigratedListOrdering: bool = ...) -> None: ...

class PBUserRecipeData(_message.Message):
    __slots__ = ["allRecipesId", "allRecipesTimestamp", "hasImportedPunchforkRecipes", "identifier", "maxRecipeCount", "mealPlanningCalendarId", "recipeCollectionIds", "recipeCollectionIdsTimestamp", "recipeCollectionsTimestamp", "recipesTimestamp", "settingsMapForSystemCollections", "settingsMapForSystemCollectionsTimestamp", "timestamp", "userIds", "userIdsTimestamp"]
    ALLRECIPESID_FIELD_NUMBER: _ClassVar[int]
    ALLRECIPESTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HASIMPORTEDPUNCHFORKRECIPES_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MAXRECIPECOUNT_FIELD_NUMBER: _ClassVar[int]
    MEALPLANNINGCALENDARID_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTIONIDSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTIONIDS_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTIONSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECIPESTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SETTINGSMAPFORSYSTEMCOLLECTIONSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SETTINGSMAPFORSYSTEMCOLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERIDSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    allRecipesId: str
    allRecipesTimestamp: float
    hasImportedPunchforkRecipes: bool
    identifier: str
    maxRecipeCount: int
    mealPlanningCalendarId: str
    recipeCollectionIds: _containers.RepeatedScalarFieldContainer[str]
    recipeCollectionIdsTimestamp: float
    recipeCollectionsTimestamp: float
    recipesTimestamp: float
    settingsMapForSystemCollections: PBRecipeCollectionSettings
    settingsMapForSystemCollectionsTimestamp: float
    timestamp: float
    userIds: _containers.RepeatedScalarFieldContainer[str]
    userIdsTimestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., recipeCollectionsTimestamp: _Optional[float] = ..., recipeCollectionIdsTimestamp: _Optional[float] = ..., allRecipesId: _Optional[str] = ..., recipeCollectionIds: _Optional[_Iterable[str]] = ..., userIds: _Optional[_Iterable[str]] = ..., userIdsTimestamp: _Optional[float] = ..., hasImportedPunchforkRecipes: bool = ..., mealPlanningCalendarId: _Optional[str] = ..., settingsMapForSystemCollections: _Optional[_Union[PBRecipeCollectionSettings, _Mapping]] = ..., settingsMapForSystemCollectionsTimestamp: _Optional[float] = ..., maxRecipeCount: _Optional[int] = ..., allRecipesTimestamp: _Optional[float] = ..., recipesTimestamp: _Optional[float] = ...) -> None: ...

class PBUserSubscriptionInfo(_message.Message):
    __slots__ = ["autorenewIapReceipts", "expirationTimestampMs", "expirationTimestampMsStr", "googlePlayOrderIds", "googlePlayPurchaseToken", "googlePlayPurchases", "identifier", "masterUser", "nonrenewIapReceipts", "nonrenewStripeCharges", "sentEmailIdentifiers", "stripeCustomerId", "stripePaymentMethodBrand", "stripePaymentMethodExpirationMonth", "stripePaymentMethodExpirationYear", "stripePaymentMethodLast4", "stripeSubscriptionId", "stripeSubscriptionInvoices", "subscriptionIsActive", "subscriptionIsCanceled", "subscriptionIsInStripeAutorenewMigrationPeriod", "subscriptionIsPendingDowngrade", "subscriptionManagementSystem", "subscriptionType", "subuserLimit", "subusers", "userConfirmedNotRenewing"]
    AUTORENEWIAPRECEIPTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIMESTAMPMSSTR_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    GOOGLEPLAYORDERIDS_FIELD_NUMBER: _ClassVar[int]
    GOOGLEPLAYPURCHASES_FIELD_NUMBER: _ClassVar[int]
    GOOGLEPLAYPURCHASETOKEN_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MASTERUSER_FIELD_NUMBER: _ClassVar[int]
    NONRENEWIAPRECEIPTS_FIELD_NUMBER: _ClassVar[int]
    NONRENEWSTRIPECHARGES_FIELD_NUMBER: _ClassVar[int]
    SENTEMAILIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    STRIPECUSTOMERID_FIELD_NUMBER: _ClassVar[int]
    STRIPEPAYMENTMETHODBRAND_FIELD_NUMBER: _ClassVar[int]
    STRIPEPAYMENTMETHODEXPIRATIONMONTH_FIELD_NUMBER: _ClassVar[int]
    STRIPEPAYMENTMETHODEXPIRATIONYEAR_FIELD_NUMBER: _ClassVar[int]
    STRIPEPAYMENTMETHODLAST4_FIELD_NUMBER: _ClassVar[int]
    STRIPESUBSCRIPTIONID_FIELD_NUMBER: _ClassVar[int]
    STRIPESUBSCRIPTIONINVOICES_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONISACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONISCANCELED_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONISINSTRIPEAUTORENEWMIGRATIONPERIOD_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONISPENDINGDOWNGRADE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONMANAGEMENTSYSTEM_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    SUBUSERLIMIT_FIELD_NUMBER: _ClassVar[int]
    SUBUSERS_FIELD_NUMBER: _ClassVar[int]
    USERCONFIRMEDNOTRENEWING_FIELD_NUMBER: _ClassVar[int]
    autorenewIapReceipts: _containers.RepeatedCompositeFieldContainer[PBIAPReceipt]
    expirationTimestampMs: int
    expirationTimestampMsStr: str
    googlePlayOrderIds: _containers.RepeatedScalarFieldContainer[str]
    googlePlayPurchaseToken: str
    googlePlayPurchases: _containers.RepeatedCompositeFieldContainer[PBGooglePlayPurchase]
    identifier: str
    masterUser: PBEmailUserIDPair
    nonrenewIapReceipts: _containers.RepeatedCompositeFieldContainer[PBIAPReceipt]
    nonrenewStripeCharges: _containers.RepeatedCompositeFieldContainer[PBStripeCharge]
    sentEmailIdentifiers: _containers.RepeatedScalarFieldContainer[str]
    stripeCustomerId: str
    stripePaymentMethodBrand: str
    stripePaymentMethodExpirationMonth: int
    stripePaymentMethodExpirationYear: int
    stripePaymentMethodLast4: str
    stripeSubscriptionId: str
    stripeSubscriptionInvoices: _containers.RepeatedCompositeFieldContainer[PBStripeSubscriptionInvoice]
    subscriptionIsActive: bool
    subscriptionIsCanceled: bool
    subscriptionIsInStripeAutorenewMigrationPeriod: bool
    subscriptionIsPendingDowngrade: bool
    subscriptionManagementSystem: int
    subscriptionType: int
    subuserLimit: int
    subusers: _containers.RepeatedCompositeFieldContainer[PBEmailUserIDPair]
    userConfirmedNotRenewing: bool
    def __init__(self, identifier: _Optional[str] = ..., subscriptionIsActive: bool = ..., subscriptionManagementSystem: _Optional[int] = ..., expirationTimestampMsStr: _Optional[str] = ..., expirationTimestampMs: _Optional[int] = ..., subscriptionType: _Optional[int] = ..., masterUser: _Optional[_Union[PBEmailUserIDPair, _Mapping]] = ..., subusers: _Optional[_Iterable[_Union[PBEmailUserIDPair, _Mapping]]] = ..., nonrenewIapReceipts: _Optional[_Iterable[_Union[PBIAPReceipt, _Mapping]]] = ..., autorenewIapReceipts: _Optional[_Iterable[_Union[PBIAPReceipt, _Mapping]]] = ..., nonrenewStripeCharges: _Optional[_Iterable[_Union[PBStripeCharge, _Mapping]]] = ..., googlePlayPurchases: _Optional[_Iterable[_Union[PBGooglePlayPurchase, _Mapping]]] = ..., googlePlayPurchaseToken: _Optional[str] = ..., googlePlayOrderIds: _Optional[_Iterable[str]] = ..., subuserLimit: _Optional[int] = ..., sentEmailIdentifiers: _Optional[_Iterable[str]] = ..., userConfirmedNotRenewing: bool = ..., subscriptionIsCanceled: bool = ..., subscriptionIsPendingDowngrade: bool = ..., subscriptionIsInStripeAutorenewMigrationPeriod: bool = ..., stripeCustomerId: _Optional[str] = ..., stripeSubscriptionId: _Optional[str] = ..., stripeSubscriptionInvoices: _Optional[_Iterable[_Union[PBStripeSubscriptionInvoice, _Mapping]]] = ..., stripePaymentMethodLast4: _Optional[str] = ..., stripePaymentMethodExpirationMonth: _Optional[int] = ..., stripePaymentMethodExpirationYear: _Optional[int] = ..., stripePaymentMethodBrand: _Optional[str] = ...) -> None: ...

class PBValue(_message.Message):
    __slots__ = ["boolValue", "dataValue", "doubleValue", "encodedPb", "identifier", "intValue", "logicalTimestampValue", "pbClassName", "recipeCollectionSettingsMap", "stringValue"]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    DATAVALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLEVALUE_FIELD_NUMBER: _ClassVar[int]
    ENCODEDPB_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMPVALUE_FIELD_NUMBER: _ClassVar[int]
    PBCLASSNAME_FIELD_NUMBER: _ClassVar[int]
    RECIPECOLLECTIONSETTINGSMAP_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    boolValue: bool
    dataValue: bytes
    doubleValue: float
    encodedPb: bytes
    identifier: str
    intValue: int
    logicalTimestampValue: int
    pbClassName: str
    recipeCollectionSettingsMap: PBRecipeCollectionSettings
    stringValue: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, identifier: _Optional[str] = ..., stringValue: _Optional[_Iterable[str]] = ..., boolValue: bool = ..., intValue: _Optional[int] = ..., doubleValue: _Optional[float] = ..., dataValue: _Optional[bytes] = ..., encodedPb: _Optional[bytes] = ..., pbClassName: _Optional[str] = ..., logicalTimestampValue: _Optional[int] = ..., recipeCollectionSettingsMap: _Optional[_Union[PBRecipeCollectionSettings, _Mapping]] = ...) -> None: ...

class PBValueList(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[PBValue]
    def __init__(self, values: _Optional[_Iterable[_Union[PBValue, _Mapping]]] = ...) -> None: ...

class PBWatchSyncMultipartResponse(_message.Message):
    __slots__ = ["fullResponseHash", "reponsePart", "responseLogicalTimestamp"]
    FULLRESPONSEHASH_FIELD_NUMBER: _ClassVar[int]
    REPONSEPART_FIELD_NUMBER: _ClassVar[int]
    RESPONSELOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    fullResponseHash: str
    reponsePart: _containers.RepeatedCompositeFieldContainer[PBWatchSyncMultipartResponsePart]
    responseLogicalTimestamp: int
    def __init__(self, reponsePart: _Optional[_Iterable[_Union[PBWatchSyncMultipartResponsePart, _Mapping]]] = ..., fullResponseHash: _Optional[str] = ..., responseLogicalTimestamp: _Optional[int] = ...) -> None: ...

class PBWatchSyncMultipartResponsePart(_message.Message):
    __slots__ = ["fullResponseHash", "partIndex", "partsCount", "responsePart"]
    FULLRESPONSEHASH_FIELD_NUMBER: _ClassVar[int]
    PARTINDEX_FIELD_NUMBER: _ClassVar[int]
    PARTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSEPART_FIELD_NUMBER: _ClassVar[int]
    fullResponseHash: str
    partIndex: int
    partsCount: int
    responsePart: bytes
    def __init__(self, fullResponseHash: _Optional[str] = ..., partIndex: _Optional[int] = ..., partsCount: _Optional[int] = ..., responsePart: _Optional[bytes] = ...) -> None: ...

class PBWatchSyncResponse(_message.Message):
    __slots__ = ["categories", "categoryGroups", "deletedCategoryGroupIds", "deletedCategoryIds", "deletedListCategorizationRuleIds", "deletedListCategoryGroupIds", "deletedListCategoryIds", "deletedListFolderIds", "deletedListItemIds", "deletedListSettingIds", "deletedShoppingListIds", "deletedStoreFilterIds", "deletedStoresIds", "isFullSync", "isPremiumUser", "listCategories", "listCategorizationRules", "listCategoryGroups", "listFolders", "listItems", "listSettings", "logicalTimestamp", "processedOperationIds", "rootFolderId", "shoppingLists", "storeFilters", "stores", "userId", "watchId"]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CATEGORYGROUPS_FIELD_NUMBER: _ClassVar[int]
    DELETEDCATEGORYGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDCATEGORYIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDLISTCATEGORIZATIONRULEIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDLISTCATEGORYGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDLISTCATEGORYIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDLISTFOLDERIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDLISTITEMIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDLISTSETTINGIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDSHOPPINGLISTIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDSTOREFILTERIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDSTORESIDS_FIELD_NUMBER: _ClassVar[int]
    ISFULLSYNC_FIELD_NUMBER: _ClassVar[int]
    ISPREMIUMUSER_FIELD_NUMBER: _ClassVar[int]
    LISTCATEGORIES_FIELD_NUMBER: _ClassVar[int]
    LISTCATEGORIZATIONRULES_FIELD_NUMBER: _ClassVar[int]
    LISTCATEGORYGROUPS_FIELD_NUMBER: _ClassVar[int]
    LISTFOLDERS_FIELD_NUMBER: _ClassVar[int]
    LISTITEMS_FIELD_NUMBER: _ClassVar[int]
    LISTSETTINGS_FIELD_NUMBER: _ClassVar[int]
    LOGICALTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROCESSEDOPERATIONIDS_FIELD_NUMBER: _ClassVar[int]
    ROOTFOLDERID_FIELD_NUMBER: _ClassVar[int]
    SHOPPINGLISTS_FIELD_NUMBER: _ClassVar[int]
    STOREFILTERS_FIELD_NUMBER: _ClassVar[int]
    STORES_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    WATCHID_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[PBUserCategory]
    categoryGroups: _containers.RepeatedCompositeFieldContainer[PBCategoryGrouping]
    deletedCategoryGroupIds: _containers.RepeatedScalarFieldContainer[str]
    deletedCategoryIds: _containers.RepeatedScalarFieldContainer[str]
    deletedListCategorizationRuleIds: _containers.RepeatedScalarFieldContainer[str]
    deletedListCategoryGroupIds: _containers.RepeatedScalarFieldContainer[str]
    deletedListCategoryIds: _containers.RepeatedScalarFieldContainer[str]
    deletedListFolderIds: _containers.RepeatedScalarFieldContainer[str]
    deletedListItemIds: _containers.RepeatedScalarFieldContainer[str]
    deletedListSettingIds: _containers.RepeatedScalarFieldContainer[str]
    deletedShoppingListIds: _containers.RepeatedScalarFieldContainer[str]
    deletedStoreFilterIds: _containers.RepeatedScalarFieldContainer[str]
    deletedStoresIds: _containers.RepeatedScalarFieldContainer[str]
    isFullSync: bool
    isPremiumUser: bool
    listCategories: _containers.RepeatedCompositeFieldContainer[PBListCategory]
    listCategorizationRules: _containers.RepeatedCompositeFieldContainer[PBListCategorizationRule]
    listCategoryGroups: _containers.RepeatedCompositeFieldContainer[PBListCategoryGroup]
    listFolders: _containers.RepeatedCompositeFieldContainer[PBListFolder]
    listItems: _containers.RepeatedCompositeFieldContainer[ListItem]
    listSettings: _containers.RepeatedCompositeFieldContainer[PBListSettings]
    logicalTimestamp: int
    processedOperationIds: _containers.RepeatedScalarFieldContainer[str]
    rootFolderId: str
    shoppingLists: _containers.RepeatedCompositeFieldContainer[ShoppingList]
    storeFilters: _containers.RepeatedCompositeFieldContainer[PBStoreFilter]
    stores: _containers.RepeatedCompositeFieldContainer[PBStore]
    userId: str
    watchId: str
    def __init__(self, watchId: _Optional[str] = ..., userId: _Optional[str] = ..., isPremiumUser: bool = ..., rootFolderId: _Optional[str] = ..., logicalTimestamp: _Optional[int] = ..., isFullSync: bool = ..., shoppingLists: _Optional[_Iterable[_Union[ShoppingList, _Mapping]]] = ..., deletedShoppingListIds: _Optional[_Iterable[str]] = ..., listItems: _Optional[_Iterable[_Union[ListItem, _Mapping]]] = ..., deletedListItemIds: _Optional[_Iterable[str]] = ..., stores: _Optional[_Iterable[_Union[PBStore, _Mapping]]] = ..., deletedStoresIds: _Optional[_Iterable[str]] = ..., storeFilters: _Optional[_Iterable[_Union[PBStoreFilter, _Mapping]]] = ..., deletedStoreFilterIds: _Optional[_Iterable[str]] = ..., listSettings: _Optional[_Iterable[_Union[PBListSettings, _Mapping]]] = ..., deletedListSettingIds: _Optional[_Iterable[str]] = ..., categoryGroups: _Optional[_Iterable[_Union[PBCategoryGrouping, _Mapping]]] = ..., deletedCategoryGroupIds: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[_Union[PBUserCategory, _Mapping]]] = ..., deletedCategoryIds: _Optional[_Iterable[str]] = ..., listCategories: _Optional[_Iterable[_Union[PBListCategory, _Mapping]]] = ..., deletedListCategoryIds: _Optional[_Iterable[str]] = ..., listCategoryGroups: _Optional[_Iterable[_Union[PBListCategoryGroup, _Mapping]]] = ..., deletedListCategoryGroupIds: _Optional[_Iterable[str]] = ..., listCategorizationRules: _Optional[_Iterable[_Union[PBListCategorizationRule, _Mapping]]] = ..., deletedListCategorizationRuleIds: _Optional[_Iterable[str]] = ..., listFolders: _Optional[_Iterable[_Union[PBListFolder, _Mapping]]] = ..., deletedListFolderIds: _Optional[_Iterable[str]] = ..., processedOperationIds: _Optional[_Iterable[str]] = ...) -> None: ...

class PBXIngredient(_message.Message):
    __slots__ = ["isHeading", "name", "note", "quantity", "rawIngredient"]
    ISHEADING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RAWINGREDIENT_FIELD_NUMBER: _ClassVar[int]
    isHeading: bool
    name: str
    note: str
    quantity: str
    rawIngredient: str
    def __init__(self, rawIngredient: _Optional[str] = ..., name: _Optional[str] = ..., quantity: _Optional[str] = ..., note: _Optional[str] = ..., isHeading: bool = ...) -> None: ...

class PBXRecipe(_message.Message):
    __slots__ = ["cookTime", "creationTimestamp", "icon", "identifier", "ingredients", "name", "note", "nutritionalInfo", "photoBytes", "prepTime", "preparationSteps", "rating", "scaleFactor", "servings", "sourceName", "sourceUrl"]
    COOKTIME_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NUTRITIONALINFO_FIELD_NUMBER: _ClassVar[int]
    PHOTOBYTES_FIELD_NUMBER: _ClassVar[int]
    PREPARATIONSTEPS_FIELD_NUMBER: _ClassVar[int]
    PREPTIME_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    SCALEFACTOR_FIELD_NUMBER: _ClassVar[int]
    SERVINGS_FIELD_NUMBER: _ClassVar[int]
    SOURCENAME_FIELD_NUMBER: _ClassVar[int]
    SOURCEURL_FIELD_NUMBER: _ClassVar[int]
    cookTime: int
    creationTimestamp: float
    icon: str
    identifier: str
    ingredients: _containers.RepeatedCompositeFieldContainer[PBXIngredient]
    name: str
    note: str
    nutritionalInfo: str
    photoBytes: bytes
    prepTime: int
    preparationSteps: _containers.RepeatedScalarFieldContainer[str]
    rating: int
    scaleFactor: float
    servings: str
    sourceName: str
    sourceUrl: str
    def __init__(self, identifier: _Optional[str] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ..., note: _Optional[str] = ..., sourceName: _Optional[str] = ..., sourceUrl: _Optional[str] = ..., ingredients: _Optional[_Iterable[_Union[PBXIngredient, _Mapping]]] = ..., preparationSteps: _Optional[_Iterable[str]] = ..., photoBytes: _Optional[bytes] = ..., scaleFactor: _Optional[float] = ..., rating: _Optional[int] = ..., creationTimestamp: _Optional[float] = ..., nutritionalInfo: _Optional[str] = ..., cookTime: _Optional[int] = ..., prepTime: _Optional[int] = ..., servings: _Optional[str] = ...) -> None: ...

class PBXRecipeArchive(_message.Message):
    __slots__ = ["recipes"]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    recipes: _containers.RepeatedCompositeFieldContainer[PBXRecipe]
    def __init__(self, recipes: _Optional[_Iterable[_Union[PBXRecipe, _Mapping]]] = ...) -> None: ...

class ShoppingList(_message.Message):
    __slots__ = ["UNUSEDATTRIBUTE", "allowsMultipleListCategoryGroups", "builtInAlexaListType", "creator", "identifier", "items", "listItemSortOrder", "logicalClockTime", "name", "newListItemPosition", "notificationLocations", "password", "sharedUsers", "timestamp"]
    class ListItemSortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class NewListItemPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALLOWSMULTIPLELISTCATEGORYGROUPS_FIELD_NUMBER: _ClassVar[int]
    Alphabetical: ShoppingList.ListItemSortOrder
    BUILTINALEXALISTTYPE_FIELD_NUMBER: _ClassVar[int]
    Bottom: ShoppingList.NewListItemPosition
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    LISTITEMSORTORDER_FIELD_NUMBER: _ClassVar[int]
    LOGICALCLOCKTIME_FIELD_NUMBER: _ClassVar[int]
    Manual: ShoppingList.ListItemSortOrder
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEWLISTITEMPOSITION_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SHAREDUSERS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    Top: ShoppingList.NewListItemPosition
    UNUSEDATTRIBUTE: _containers.RepeatedScalarFieldContainer[str]
    UNUSEDATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    allowsMultipleListCategoryGroups: bool
    builtInAlexaListType: str
    creator: str
    identifier: str
    items: _containers.RepeatedCompositeFieldContainer[ListItem]
    listItemSortOrder: int
    logicalClockTime: int
    name: str
    newListItemPosition: int
    notificationLocations: _containers.RepeatedCompositeFieldContainer[PBNotificationLocation]
    password: str
    sharedUsers: _containers.RepeatedCompositeFieldContainer[PBEmailUserIDPair]
    timestamp: float
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[ListItem, _Mapping]]] = ..., creator: _Optional[str] = ..., UNUSEDATTRIBUTE: _Optional[_Iterable[str]] = ..., sharedUsers: _Optional[_Iterable[_Union[PBEmailUserIDPair, _Mapping]]] = ..., password: _Optional[str] = ..., notificationLocations: _Optional[_Iterable[_Union[PBNotificationLocation, _Mapping]]] = ..., logicalClockTime: _Optional[int] = ..., builtInAlexaListType: _Optional[str] = ..., allowsMultipleListCategoryGroups: bool = ..., listItemSortOrder: _Optional[int] = ..., newListItemPosition: _Optional[int] = ...) -> None: ...

class ShoppingListsResponse(_message.Message):
    __slots__ = ["listResponses", "modifiedLists", "newLists", "orderedIds", "unknownIds", "unmodifiedIds"]
    LISTRESPONSES_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDLISTS_FIELD_NUMBER: _ClassVar[int]
    NEWLISTS_FIELD_NUMBER: _ClassVar[int]
    ORDEREDIDS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNIDS_FIELD_NUMBER: _ClassVar[int]
    UNMODIFIEDIDS_FIELD_NUMBER: _ClassVar[int]
    listResponses: _containers.RepeatedCompositeFieldContainer[PBListResponse]
    modifiedLists: _containers.RepeatedCompositeFieldContainer[ShoppingList]
    newLists: _containers.RepeatedCompositeFieldContainer[ShoppingList]
    orderedIds: _containers.RepeatedScalarFieldContainer[str]
    unknownIds: _containers.RepeatedScalarFieldContainer[str]
    unmodifiedIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, newLists: _Optional[_Iterable[_Union[ShoppingList, _Mapping]]] = ..., modifiedLists: _Optional[_Iterable[_Union[ShoppingList, _Mapping]]] = ..., unmodifiedIds: _Optional[_Iterable[str]] = ..., unknownIds: _Optional[_Iterable[str]] = ..., orderedIds: _Optional[_Iterable[str]] = ..., listResponses: _Optional[_Iterable[_Union[PBListResponse, _Mapping]]] = ...) -> None: ...

class StarterList(_message.Message):
    __slots__ = ["identifier", "items", "listId", "name", "starterListType", "timestamp", "userId"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FavoriteItemsType: StarterList.Type
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    LISTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RecentItemsType: StarterList.Type
    STARTERLISTTYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserType: StarterList.Type
    identifier: str
    items: _containers.RepeatedCompositeFieldContainer[ListItem]
    listId: str
    name: str
    starterListType: int
    timestamp: float
    userId: str
    def __init__(self, identifier: _Optional[str] = ..., timestamp: _Optional[float] = ..., name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[ListItem, _Mapping]]] = ..., userId: _Optional[str] = ..., listId: _Optional[str] = ..., starterListType: _Optional[int] = ...) -> None: ...

class StarterListBatchResponse(_message.Message):
    __slots__ = ["includesAllLists", "listResponses", "unknownListIds"]
    INCLUDESALLLISTS_FIELD_NUMBER: _ClassVar[int]
    LISTRESPONSES_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNLISTIDS_FIELD_NUMBER: _ClassVar[int]
    includesAllLists: bool
    listResponses: _containers.RepeatedCompositeFieldContainer[StarterListResponse]
    unknownListIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, listResponses: _Optional[_Iterable[_Union[StarterListResponse, _Mapping]]] = ..., includesAllLists: bool = ..., unknownListIds: _Optional[_Iterable[str]] = ...) -> None: ...

class StarterListResponse(_message.Message):
    __slots__ = ["starterList"]
    STARTERLIST_FIELD_NUMBER: _ClassVar[int]
    starterList: StarterList
    def __init__(self, starterList: _Optional[_Union[StarterList, _Mapping]] = ...) -> None: ...

class StarterListsResponse(_message.Message):
    __slots__ = ["modifiedLists", "newLists", "orderedIds", "unknownIds", "unmodifiedIds"]
    MODIFIEDLISTS_FIELD_NUMBER: _ClassVar[int]
    NEWLISTS_FIELD_NUMBER: _ClassVar[int]
    ORDEREDIDS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNIDS_FIELD_NUMBER: _ClassVar[int]
    UNMODIFIEDIDS_FIELD_NUMBER: _ClassVar[int]
    modifiedLists: _containers.RepeatedCompositeFieldContainer[StarterList]
    newLists: _containers.RepeatedCompositeFieldContainer[StarterList]
    orderedIds: _containers.RepeatedScalarFieldContainer[str]
    unknownIds: _containers.RepeatedScalarFieldContainer[str]
    unmodifiedIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, newLists: _Optional[_Iterable[_Union[StarterList, _Mapping]]] = ..., modifiedLists: _Optional[_Iterable[_Union[StarterList, _Mapping]]] = ..., unmodifiedIds: _Optional[_Iterable[str]] = ..., unknownIds: _Optional[_Iterable[str]] = ..., orderedIds: _Optional[_Iterable[str]] = ...) -> None: ...

class StarterListsResponseV2(_message.Message):
    __slots__ = ["favoriteItemListsResponse", "hasMigratedUserFavorites", "recentItemListsResponse", "userListsResponse"]
    FAVORITEITEMLISTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    HASMIGRATEDUSERFAVORITES_FIELD_NUMBER: _ClassVar[int]
    RECENTITEMLISTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    USERLISTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    favoriteItemListsResponse: StarterListBatchResponse
    hasMigratedUserFavorites: bool
    recentItemListsResponse: StarterListBatchResponse
    userListsResponse: StarterListBatchResponse
    def __init__(self, userListsResponse: _Optional[_Union[StarterListBatchResponse, _Mapping]] = ..., recentItemListsResponse: _Optional[_Union[StarterListBatchResponse, _Mapping]] = ..., favoriteItemListsResponse: _Optional[_Union[StarterListBatchResponse, _Mapping]] = ..., hasMigratedUserFavorites: bool = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ["displayName", "imageName", "impliedTagNames", "name", "priceStats", "productIds", "searchTerms", "tagType"]
    class TagType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    IMAGENAME_FIELD_NUMBER: _ClassVar[int]
    IMPLIEDTAGNAMES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICESTATS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTIDS_FIELD_NUMBER: _ClassVar[int]
    SEARCHTERMS_FIELD_NUMBER: _ClassVar[int]
    TAGTYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_TYPE_ATTRIBUTE: Tag.TagType
    TAG_TYPE_CATEGORY: Tag.TagType
    TAG_TYPE_GENERIC: Tag.TagType
    TAG_TYPE_PRODUCT: Tag.TagType
    displayName: str
    imageName: str
    impliedTagNames: _containers.RepeatedScalarFieldContainer[str]
    name: str
    priceStats: bytes
    productIds: _containers.RepeatedScalarFieldContainer[str]
    searchTerms: _containers.RepeatedScalarFieldContainer[str]
    tagType: Tag.TagType
    def __init__(self, name: _Optional[str] = ..., displayName: _Optional[str] = ..., imageName: _Optional[str] = ..., impliedTagNames: _Optional[_Iterable[str]] = ..., searchTerms: _Optional[_Iterable[str]] = ..., productIds: _Optional[_Iterable[str]] = ..., priceStats: _Optional[bytes] = ..., tagType: _Optional[_Union[Tag.TagType, str]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["DEPRECATEDFavoriteProductsTimestamp", "DEPRECATEDFavoriteTags", "DEPRECATEDHiddenTags", "DEPRECATEDHttpReferrer", "DEPRECATEDInviteCode", "DEPRECATEDList", "DEPRECATEDLocation", "DEPRECATEDNotifyProducts", "DEPRECATEDNotifyTagNames", "DEPRECATEDPreferredChainIds", "DEPRECATEDPreferredStoreIds", "DEPRECATEDReferrer", "DEPRECATEDSavedSearches", "DEPRECATEDStarred", "DEPRECATEDWeeklyDealsEmailCount", "DEPRECATEDWelcomed", "categorizedItemsRequireRefreshTimestamp", "categorizedItemsTimestamp", "created", "email", "facebookUserId", "fcmTokens", "firstName", "freeRecipeImportsRemainingCount", "hasMigratedUserFavorites", "icalendarId", "id", "isPremiumUser", "lastName", "listDataId", "listSettingsRequireRefreshTimestamp", "listSettingsTimestamp", "notify", "orderedShoppingListIdsTimestamp", "orderedStarterListIds", "orderedStarterListIdsTimestamp", "otpSecret", "pushTokens", "recipeDataId", "savedRecipesTimestamp", "shoppingListIds", "starterListSettingsRequireRefreshTimestamp", "starterListSettingsTimestamp"]
    CATEGORIZEDITEMSREQUIREREFRESHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CATEGORIZEDITEMSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDFAVORITEPRODUCTSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDFAVORITETAGS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDFavoriteProductsTimestamp: float
    DEPRECATEDFavoriteTags: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDHIDDENTAGS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDHTTPREFERRER_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDHiddenTags: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDHttpReferrer: str
    DEPRECATEDINVITECODE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDInviteCode: str
    DEPRECATEDLIST_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDLOCATION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDList: bytes
    DEPRECATEDLocation: bytes
    DEPRECATEDNOTIFYPRODUCTS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDNOTIFYTAGNAMES_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDNotifyProducts: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDNotifyTagNames: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDPREFERREDCHAINIDS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDPREFERREDSTOREIDS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDPreferredChainIds: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDPreferredStoreIds: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDREFERRER_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDReferrer: str
    DEPRECATEDSAVEDSEARCHES_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDSTARRED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDSavedSearches: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDStarred: _containers.RepeatedScalarFieldContainer[str]
    DEPRECATEDWEEKLYDEALSEMAILCOUNT_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDWELCOMED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDWeeklyDealsEmailCount: int
    DEPRECATEDWelcomed: bool
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FACEBOOKUSERID_FIELD_NUMBER: _ClassVar[int]
    FCMTOKENS_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    FREERECIPEIMPORTSREMAININGCOUNT_FIELD_NUMBER: _ClassVar[int]
    HASMIGRATEDUSERFAVORITES_FIELD_NUMBER: _ClassVar[int]
    ICALENDARID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISPREMIUMUSER_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    LISTDATAID_FIELD_NUMBER: _ClassVar[int]
    LISTSETTINGSREQUIREREFRESHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LISTSETTINGSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    ORDEREDSHOPPINGLISTIDSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDEREDSTARTERLISTIDSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDEREDSTARTERLISTIDS_FIELD_NUMBER: _ClassVar[int]
    OTPSECRET_FIELD_NUMBER: _ClassVar[int]
    PUSHTOKENS_FIELD_NUMBER: _ClassVar[int]
    RECIPEDATAID_FIELD_NUMBER: _ClassVar[int]
    SAVEDRECIPESTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SHOPPINGLISTIDS_FIELD_NUMBER: _ClassVar[int]
    STARTERLISTSETTINGSREQUIREREFRESHTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STARTERLISTSETTINGSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    categorizedItemsRequireRefreshTimestamp: float
    categorizedItemsTimestamp: float
    created: int
    email: str
    facebookUserId: str
    fcmTokens: _containers.RepeatedScalarFieldContainer[str]
    firstName: str
    freeRecipeImportsRemainingCount: int
    hasMigratedUserFavorites: bool
    icalendarId: str
    id: str
    isPremiumUser: bool
    lastName: str
    listDataId: str
    listSettingsRequireRefreshTimestamp: float
    listSettingsTimestamp: float
    notify: bool
    orderedShoppingListIdsTimestamp: float
    orderedStarterListIds: _containers.RepeatedScalarFieldContainer[str]
    orderedStarterListIdsTimestamp: float
    otpSecret: str
    pushTokens: _containers.RepeatedScalarFieldContainer[str]
    recipeDataId: str
    savedRecipesTimestamp: float
    shoppingListIds: _containers.RepeatedScalarFieldContainer[str]
    starterListSettingsRequireRefreshTimestamp: float
    starterListSettingsTimestamp: float
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., created: _Optional[int] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., isPremiumUser: bool = ..., pushTokens: _Optional[_Iterable[str]] = ..., fcmTokens: _Optional[_Iterable[str]] = ..., hasMigratedUserFavorites: bool = ..., recipeDataId: _Optional[str] = ..., listDataId: _Optional[str] = ..., facebookUserId: _Optional[str] = ..., icalendarId: _Optional[str] = ..., freeRecipeImportsRemainingCount: _Optional[int] = ..., otpSecret: _Optional[str] = ..., orderedStarterListIds: _Optional[_Iterable[str]] = ..., orderedStarterListIdsTimestamp: _Optional[float] = ..., notify: bool = ..., savedRecipesTimestamp: _Optional[float] = ..., listSettingsTimestamp: _Optional[float] = ..., listSettingsRequireRefreshTimestamp: _Optional[float] = ..., starterListSettingsTimestamp: _Optional[float] = ..., starterListSettingsRequireRefreshTimestamp: _Optional[float] = ..., orderedShoppingListIdsTimestamp: _Optional[float] = ..., shoppingListIds: _Optional[_Iterable[str]] = ..., categorizedItemsTimestamp: _Optional[float] = ..., categorizedItemsRequireRefreshTimestamp: _Optional[float] = ..., DEPRECATEDStarred: _Optional[_Iterable[str]] = ..., DEPRECATEDSavedSearches: _Optional[_Iterable[str]] = ..., DEPRECATEDList: _Optional[bytes] = ..., DEPRECATEDWelcomed: bool = ..., DEPRECATEDNotifyProducts: _Optional[_Iterable[str]] = ..., DEPRECATEDNotifyTagNames: _Optional[_Iterable[str]] = ..., DEPRECATEDLocation: _Optional[bytes] = ..., DEPRECATEDPreferredChainIds: _Optional[_Iterable[str]] = ..., DEPRECATEDFavoriteTags: _Optional[_Iterable[str]] = ..., DEPRECATEDHiddenTags: _Optional[_Iterable[str]] = ..., DEPRECATEDReferrer: _Optional[str] = ..., DEPRECATEDInviteCode: _Optional[str] = ..., DEPRECATEDHttpReferrer: _Optional[str] = ..., DEPRECATEDWeeklyDealsEmailCount: _Optional[int] = ..., DEPRECATEDPreferredStoreIds: _Optional[_Iterable[str]] = ..., DEPRECATEDFavoriteProductsTimestamp: _Optional[float] = ...) -> None: ...
