#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################
### Extracted from platform version: 5.0.2 
#################################################
AOSP_PERMISSIONS = {
    "android.permission.REMOTE_AUDIO_PLAYBACK": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.DUMP": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to retrieve internal state of the system. Malicious apps may retrieve a wide variety of private and secure information that they should never normally need.",
        "protectionLevel": "signature|system|development",
        "label": "retrieve system internal state"
    },
    "android.permission.BODY_SENSORS": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description":
        "Allows the app to access data from sensors you use to measure what’s happening inside your body, such as heart rate.",
        "protectionLevel": "",
        "label": "body sensors (like heart rate monitors)"
    },
    "android.permission.READ_SOCIAL_STREAM": {
        "permissionGroup": "android.permission-group.SOCIAL_INFO",
        "description":
        "Allows the app to access and sync social updates from you and your friends. Be careful when sharing information -- this allows the app to read communications between you and your friends on social networks, regardless of confidentiality. Note: this permission may not be enforced on all social networks.",
        "protectionLevel": "dangerous",
        "label": "read your social stream"
    },
    "android.permission.MODIFY_AUDIO_ROUTING": {
        "permissionGroup": "",
        "description":
        "Allows the app to directly control audio routing and override audio policy decisions.",
        "protectionLevel": "signature|system",
        "label": "Audio Routing"
    },
    "android.permission.READ_NETWORK_USAGE_HISTORY": {
        "permissionGroup": "",
        "description":
        "Allows the app to read historical network usage for specific networks and apps.",
        "protectionLevel": "signature|system",
        "label": "read historical network usage"
    },
    "android.permission.BIND_DIRECTORY_SEARCH": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.INTERNET": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to create network sockets and use custom network protocols. The browser and other applications provide means to send data to the internet, so this permission is not required to send data to the internet.",
        "protectionLevel": "dangerous",
        "label": "full network access"
    },
    "android.permission.HARDWARE_TEST": {
        "permissionGroup": "android.permission-group.HARDWARE_CONTROLS",
        "description":
        "Allows the app to control various peripherals for the purpose of hardware testing.",
        "protectionLevel": "signature",
        "label": "test hardware"
    },
    "android.permission.START_TASKS_FROM_RECENTS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to use an ActivityManager.RecentTaskInfo object to launch a defunct task that was returned from ActivityManager.getRecentTaskList().",
        "protectionLevel": "signature|system",
        "label": "start a task from recents"
    },
    "android.permission.ACCESS_DOWNLOAD_MANAGER_ADVANCED": {
        "permissionGroup": "",
        "description":
        "Allows the app to access the download manager\'s advanced functions. Malicious apps can use this to disrupt downloads and access private information.",
        "protectionLevel": "signatureOrSystem",
        "label": "Advanced download manager functions."
    },
    "android.permission.REMOVE_DRM_CERTIFICATES": {
        "permissionGroup": "",
        "description":
        "Allows an application to remove DRM certficates. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "remove DRM certificates"
    },
    "com.android.launcher.permission.INSTALL_SHORTCUT": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows an application to add Homescreen shortcuts without user intervention.",
        "protectionLevel": "dangerous",
        "label": "install shortcuts"
    },
    "android.permission.BIND_TV_INPUT": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a TV input. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "bind to a TV input"
    },
    "android.permission.BIND_VPN_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a Vpn service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a VPN service"
    },
    "com.android.voicemail.permission.READ_VOICEMAIL": {
        "permissionGroup": "android.permission-group.VOICEMAIL",
        "description": "Allows the app to read your voicemails.",
        "protectionLevel": "system|signature",
        "label": "read voicemail"
    },
    "android.permission.READ_SEARCH_INDEXABLES": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.BIND_INPUT_METHOD": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of an input method. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to an input method"
    },
    "android.permission.ACCESS_CACHE_FILESYSTEM": {
        "permissionGroup": "",
        "description": "Allows the app to read and write the cache filesystem.",
        "protectionLevel": "signature|system",
        "label": "access the cache filesystem"
    },
    "android.permission.DOWNLOAD_CACHE_NON_PURGEABLE": {
        "permissionGroup": "",
        "description":
        "Allows the app to download files to the download cache, which can\'t be automatically deleted when the download manager needs more space.",
        "protectionLevel": "signatureOrSystem",
        "label": "Reserve space in the download cache"
    },
    "android.permission.CONFIGURE_WIFI_DISPLAY": {
        "permissionGroup": "",
        "description":
        "Allows the app to configure and connect to Wifi displays.",
        "protectionLevel": "signature",
        "label": "configure Wifi displays"
    },
    "com.android.gallery3d.permission.GALLERY_PROVIDER": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": ""
    },
    "com.android.permission.WHITELIST_BLUETOOTH_DEVICE": {
        "permissionGroup": "",
        "description":
        "Allows the app to temporarily whitelist a Bluetooth device, allowing that device to send files to this device without user confirmation.",
        "protectionLevel": "signature",
        "label": "Whitelist bluetooth device access."
    },
    "android.permission.READ_CELL_BROADCASTS": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to read cell broadcast messages received by your device. Cell broadcast alerts are delivered in some locations to warn you of emergency situations. Malicious apps may interfere with the performance or operation of your device when an emergency cell broadcast is received.",
        "protectionLevel": "dangerous",
        "label": "read cell broadcast messages"
    },
    "android.permission.BIND_DEVICE_ADMIN": {
        "permissionGroup": "",
        "description":
        "Allows the holder to send intents to a device administrator. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "interact with a device admin"
    },
    "android.permission.FRAME_STATS": {
        "permissionGroup": "",
        "description":
        "Allows an application to collect frame statistics. Malicious apps may observe the frame statistics of windows from other apps.",
        "protectionLevel": "signature",
        "label": "retrieve frame statistics"
    },
    "com.android.providers.tv.permission.ACCESS_ALL_EPG_DATA": {
        "permissionGroup": "",
        "description":
        "Allows the app to read and write all TV channel/program data stored on your device.",
        "protectionLevel": "signatureOrSystem",
        "label": "access all TV channel/program information"
    },
    "android.permission.WRITE_SECURE_SETTINGS": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to modify the system\'s secure settings data. Not for use by normal apps.",
        "protectionLevel": "signature|system|development",
        "label": "modify secure system settings"
    },
    "android.permission.MANAGE_DOCUMENTS": {
        "permissionGroup": "android.permission-group.STORAGE",
        "description": "Allows the app to manage document storage.",
        "protectionLevel": "signature",
        "label": "manage document storage"
    },
    "android.permission.SYSTEM_ALERT_WINDOW": {
        "permissionGroup": "android.permission-group.DISPLAY",
        "description":
        "Allows the app to draw on top of other applications or parts of the user interface. They may interfere with your use of the interface in any application, or change what you think you are seeing in other applications.",
        "protectionLevel": "dangerous",
        "label": "draw over other apps"
    },
    "com.android.cts.permissionNotUsedWithSignature": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.READ_SYNC_STATS": {
        "permissionGroup": "android.permission-group.SYNC_SETTINGS",
        "description":
        "Allows an app to read the sync stats for an account, including the history of sync events and how much data is synced.",
        "protectionLevel": "normal",
        "label": "read sync statistics"
    },
    "android.permission.START_ANY_ACTIVITY": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to start any activity, regardless of permission protection or exported state.",
        "protectionLevel": "signature",
        "label": "start any activity"
    },
    "android.permission.AUTHENTICATE_ACCOUNTS": {
        "permissionGroup": "android.permission-group.ACCOUNTS",
        "description":
        "Allows the app to use the account authenticator capabilities of the AccountManager, including creating accounts and getting and setting their passwords.",
        "protectionLevel": "dangerous",
        "label": "create accounts and set passwords"
    },
    "test_permission": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "normal",
        "label": ""
    },
    "android.permission.MODIFY_PHONE_STATE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description":
        "Allows the app to control the phone features of the device. An app with this permission can switch networks, turn the phone radio on and off and the like without ever notifying you.",
        "protectionLevel": "signature|system",
        "label": "modify phone state"
    },
    "android.permission.LAUNCH_TRUST_AGENT_SETTINGS": {
        "permissionGroup": "",
        "description":
        "Allows an application to launch an activity that changes the trust agent behavior.",
        "protectionLevel": "signatureOrSystem",
        "label": "Launch trust agent settings menu."
    },
    "android.permission.CAPTURE_SECURE_VIDEO_OUTPUT": {
        "permissionGroup": "",
        "description":
        "Allows the app to capture and redirect secure video output.",
        "protectionLevel": "signature|system",
        "label": "capture secure video output"
    },
    "com.android.launcher.permission.PRELOAD_WORKSPACE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": ""
    },
    "android.permission.BIND_CONNECTION_SERVICE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description":
        "Allows the app to interact with telephony services to make/receive calls.",
        "protectionLevel": "system|signature",
        "label": "interact with telephony services"
    },
    "android.permission.WRITE_PROFILE": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description":
        "Allows the app to change or add to personal profile information stored on your device, such as your name and contact information. This means the app can identify you and may send your profile information to others.",
        "protectionLevel": "dangerous",
        "label": "modify your own contact card"
    },
    "android.permission.BIND_NFC_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to applications that are emulating NFC cards. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to NFC service"
    },
    "android.permission.GRANT_REVOKE_PERMISSIONS": {
        "permissionGroup": "",
        "description":
        "Allows an application to grant or revoke specific permissions for it or other applications. Malicious applications may use this to access features you have not granted them.",
        "protectionLevel": "signature",
        "label": "grant or revoke permissions"
    },
    "android.permission.CAMERA": {
        "permissionGroup": "android.permission-group.CAMERA",
        "description":
        "Allows the app to take pictures and videos with the camera. This permission allows the app to use the camera at any time without your confirmation.",
        "protectionLevel": "dangerous",
        "label": "take pictures and videos"
    },
    "android.permission.START_PRINT_SERVICE_CONFIG_ACTIVITY": {
        "permissionGroup": "",
        "description":
        "Allows the holder to start the configuration activities of a print service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "start print service configuration activities"
    },
    "android.permission.SET_WALLPAPER_HINTS": {
        "permissionGroup": "android.permission-group.WALLPAPER",
        "description": "Allows the app to set the system wallpaper size hints.",
        "protectionLevel": "normal",
        "label": "adjust your wallpaper size"
    },
    "android.permission.INVOKE_CARRIER_SETUP": {
        "permissionGroup": "",
        "description":
        "Allows the holder to invoke the carrier-provided configuration app. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "invoke the carrier-provided configuration app"
    },
    "android.permission.BIND_NOTIFICATION_LISTENER_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a notification listener service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a notification listener service"
    },
    "android.permission.REBOOT": {
        "permissionGroup": "",
        "description": "Allows the app to force the phone to reboot.",
        "protectionLevel": "signature|system",
        "label": "force phone reboot"
    },
    "android.permission.BROADCAST_WAP_PUSH": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to broadcast a notification that a WAP PUSH message has been received. Malicious apps may use this to forge MMS message receipt or to silently replace the content of any webpage with malicious variants.",
        "protectionLevel": "signature",
        "label": "send WAP-PUSH-received broadcast"
    },
    "android.permission.ACCESS_NETWORK_STATE": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to view information about network connections such as which networks exist and are connected.",
        "protectionLevel": "normal",
        "label": "view network connections"
    },
    "android.permission.CAPTURE_TV_INPUT": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": ""
    },
    "android.permission.CHANGE_WIMAX_STATE": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to connect the phone to and disconnect the phone from WiMAX networks.",
        "protectionLevel": "dangerous",
        "label": "Change WiMAX state"
    },
    "com.foo.mypermission": {
        "permissionGroup": "",
        "description": "MyActivity",
        "protectionLevel": "",
        "label": "MyActivity"
    },
    "android.permission.MOUNT_FORMAT_FILESYSTEMS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows the app to format removable storage.",
        "protectionLevel": "system|signature",
        "label": "erase SD Card"
    },
    "android.permission.SCORE_NETWORKS": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to rank networks and influence which networks the phone should prefer.",
        "protectionLevel": "signature|system",
        "label": "score networks"
    },
    "android.permission.BIND_APPWIDGET": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description":
        "Allows the app to tell the system which widgets can be used by which app. An app with this permission can give access to personal data to other apps. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "choose widgets"
    },
    "com.android.frameworks.coretests.permission.TEST_GRANTED": {
        "permissionGroup": "",
        "description":
        "Used for running unit tests, for testing operations where we have the permission.",
        "protectionLevel": "normal",
        "label": "Test Granted"
    },
    "android.permission.ASEC_CREATE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows the app to create internal storage.",
        "protectionLevel": "signature",
        "label": "create internal storage"
    },
    "android.permission.MANAGE_CA_CERTIFICATES": {
        "permissionGroup": "",
        "description":
        "Allows the app to install and uninstall CA certificates as trusted credentials.",
        "protectionLevel": "signature|system",
        "label": "manage trusted credentials"
    },
    "android.permission.INSTALL_LOCATION_PROVIDER": {
        "permissionGroup": "",
        "description":
        "Create mock location sources for testing or install a new location provider. This allows the app to override the location and/or status returned by other location sources such as GPS or location providers.",
        "protectionLevel": "signature|system",
        "label": "permission to install a location provider"
    },
    "android.permission.LOOP_RADIO": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.TRANSMIT_IR": {
        "permissionGroup": "android.permission-group.AFFECTS_BATTERY",
        "description":
        "Allows the app to use the phone\'s infrared transmitter.",
        "protectionLevel": "normal",
        "label": "transmit infrared"
    },
    "com.android.browser.permission.WRITE_HISTORY_BOOKMARKS": {
        "permissionGroup": "android.permission-group.BOOKMARKS",
        "description":
        "Allows the app to modify the Browser\'s history or bookmarks stored on your phone. This may allow the app to erase or modify Browser data. Note: this permission may note be enforced by third-party browsers or other applications with web browsing capabilities.",
        "protectionLevel": "dangerous",
        "label": "write web bookmarks and history"
    },
    "android.permission.WRITE_SETTINGS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to modify the system\'s settings data. Malicious apps may corrupt your system\'s configuration.",
        "protectionLevel": "normal",
        "label": "modify system settings"
    },
    "android.permission.MANAGE_APP_TOKENS": {
        "permissionGroup": "",
        "description":
        "Allows the app to create and manage their own tokens, bypassing their normal Z-ordering. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "manage app tokens"
    },
    "android.permission.RESTART_PACKAGES": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to end background processes of other apps. This may cause other apps to stop running.",
        "protectionLevel": "normal",
        "label": "close other apps"
    },
    "android.permission.ACCESS_DRM_CERTIFICATES": {
        "permissionGroup": "",
        "description":
        "Allows an application to provision and use DRM certficates. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "access DRM certificates"
    },
    "android.permission.PACKAGE_VERIFICATION_AGENT": {
        "permissionGroup": "",
        "description": "Allows the app to verify a package is installable.",
        "protectionLevel": "signature|system",
        "label": "verify packages"
    },
    "android.permission.CONFIRM_FULL_BACKUP": {
        "permissionGroup": "",
        "description":
        "Allows the app to launch the full backup confirmation UI. Not to be used by any app.",
        "protectionLevel": "signature",
        "label": "confirm a full backup or restore operation"
    },
    "com.android.smspush.WAPPUSH_MANAGER_BIND": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": ""
    },
    "com.android.gallery3d.filtershow.permission.READ": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.BIND_PRINT_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a print service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a print service"
    },
    "com.android.providers.tv.permission.ACCESS_WATCHED_PROGRAMS": {
        "permissionGroup": "",
        "description":
        "Allows the app to read and write the list of TV programs you watched. Malicious apps may collect your private TV watch history.",
        "protectionLevel": "signatureOrSystem",
        "label": "access watched TV program information"
    },
    "android.permission.ASEC_ACCESS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows the app to get information on internal storage.",
        "protectionLevel": "signature",
        "label": "get information on internal storage"
    },
    "android.permission.USE_SIP": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description": "Allows the app to make and receive SIP calls.",
        "protectionLevel": "dangerous",
        "label": "make/receive SIP calls"
    },
    "android.permission.RECEIVE_DATA_ACTIVITY_CHANGE": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.NET_ADMIN": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.CHANGE_BACKGROUND_DATA_SETTING": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to change the background data usage setting.",
        "protectionLevel": "signature",
        "label": "change background data usage setting"
    },
    "android.permission.PROCESS_CALLLOG_INFO": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.CAPTURE_AUDIO_HOTWORD": {
        "permissionGroup": "",
        "description":
        "Allows the app to capture audio for Hotword detection. The capture can happen in the background but does not prevent other audio capture (e.g. Camcorder).",
        "protectionLevel": "signature|system",
        "label": "Hotword detection"
    },
    "android.permission.NFC": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to communicate with Near Field Communication (NFC) tags, cards, and readers.",
        "protectionLevel": "dangerous",
        "label": "control Near Field Communication"
    },
    "android.permission.SEND_SMS": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to send SMS messages. This may result in unexpected charges. Malicious apps may cost you money by sending messages without your confirmation.",
        "protectionLevel": "dangerous",
        "label": "send SMS messages"
    },
    "android.permission.INTERACT_ACROSS_USERS_FULL": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows all possible interactions across users.",
        "protectionLevel": "signature",
        "label": "full license to interact across users"
    },
    "android.permission.CLEAR_APP_USER_DATA": {
        "permissionGroup": "",
        "description": "Allows the app to clear user data.",
        "protectionLevel": "signature",
        "label": "delete other apps\' data"
    },
    "android.permission.ACCESS_MOCK_LOCATION": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Create mock location sources for testing or install a new location provider. This allows the app to override the location and/or status returned by other location sources such as GPS or location providers.",
        "protectionLevel": "dangerous",
        "label": "mock location sources for testing"
    },
    "android.permission.CAPTURE_AUDIO_OUTPUT": {
        "permissionGroup": "",
        "description": "Allows the app to capture and redirect audio output.",
        "protectionLevel": "signature|system",
        "label": "capture audio output"
    },
    "android.permission.GET_DETAILED_TASKS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to retrieve detailed information about currently and recently running tasks. Malicious apps may discover private information about other apps.",
        "protectionLevel": "signature",
        "label": "retrieve details of running apps"
    },
    "android.permission.ACCESS_ALL_DOWNLOADS": {
        "permissionGroup": "",
        "description":
        "Allows the app to view and modify all downloads initiated by any app on the system.",
        "protectionLevel": "signature",
        "label": "Access all system downloads"
    },
    "android.permission.STATUS_BAR": {
        "permissionGroup": "",
        "description":
        "Allows the app to disable the status bar or add and remove system icons.",
        "protectionLevel": "signature|system",
        "label": "disable or modify status bar"
    },
    "android.permission.TV_INPUT_HARDWARE": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": ""
    },
    "android.permission.MEDIA_CONTENT_CONTROL": {
        "permissionGroup": "",
        "description":
        "Allows the app to control media playback and access the media information (title, author...).",
        "protectionLevel": "signature|system",
        "label": "control media playback and metadata access"
    },
    "android.permission.DOWNLOAD_WITHOUT_NOTIFICATION": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to download files through the download manager without any notification being shown to the user.",
        "protectionLevel": "normal",
        "label": "download files without notification"
    },
    "android.permission.RECOVERY": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows an application to interact with the recovery system and system updates.",
        "protectionLevel": "signature|system",
        "label": "Interact with update and recovery system"
    },
    "com.android.email.permission.READ_ATTACHMENT": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description": "Allows the app to read your email attachments.",
        "protectionLevel": "dangerous",
        "label": "Read email attachments"
    },
    "android.permission.NET_TUNNELING": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.SET_TIME": {
        "permissionGroup": "",
        "description": "Allows the app to change the phone\'s clock time.",
        "protectionLevel": "signature|system",
        "label": "set time"
    },
    "android.permission.MANAGE_MEDIA_PROJECTION": {
        "permissionGroup": "",
        "description":
        "Allows an application to manage media projection sessions. These sessions can provide applications the ability to capture display and audio contents. Should never be needed by normal apps.",
        "protectionLevel": "signature",
        "label": "Manage media projection sessions"
    },
    "android.permission.CALL_PHONE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description":
        "Allows the app to call phone numbers without your intervention. This may result in unexpected charges or calls. Note that this doesn\'t allow the app to call emergency numbers. Malicious apps may cost you money by making calls without your confirmation.",
        "protectionLevel": "dangerous",
        "label": "directly call phone numbers"
    },
    "android.permission.FLASHLIGHT": {
        "permissionGroup": "android.permission-group.AFFECTS_BATTERY",
        "description": "Allows the app to control the flashlight.",
        "protectionLevel": "normal",
        "label": "control flashlight"
    },
    "android.permission.READ_PHONE_STATE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description":
        "Allows the app to access the phone features of the device. This permission allows the app to determine the phone number and device IDs, whether a call is active, and the remote number connected by a call.",
        "protectionLevel": "dangerous",
        "label": "read phone status and identity"
    },
    "android.permission.MANAGE_DEVICE_ADMINS": {
        "permissionGroup": "",
        "description":
        "Allows the holder to add or remove active device administrators. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "add or remove a device admin"
    },
    "com.android.voicemail.permission.ADD_VOICEMAIL": {
        "permissionGroup": "android.permission-group.VOICEMAIL",
        "description":
        "Allows the app to add messages to your voicemail inbox.",
        "protectionLevel": "dangerous",
        "label": "add voicemail"
    },
    "android.permission.REAL_GET_TASKS": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to retrieve information about currently and recently running tasks. This may allow the app to discover information about which applications are used on the device.",
        "protectionLevel": "signature|system",
        "label": "retrieve running apps"
    },
    "com.android.server.telecom.permission.REGISTER_PROVIDER_OR_SUBSCRIPTION": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.KILL_BACKGROUND_PROCESSES": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to end background processes of other apps. This may cause other apps to stop running.",
        "protectionLevel": "normal",
        "label": "close other apps"
    },
    "android.permission.RECEIVE_MMS": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to receive and process MMS messages. This means the app could monitor or delete messages sent to your device without showing them to you.",
        "protectionLevel": "dangerous",
        "label": "receive text messages (MMS)"
    },
    "android.permission.WAKE_LOCK": {
        "permissionGroup": "android.permission-group.AFFECTS_BATTERY",
        "description":
        "Allows the app to prevent the phone from going to sleep.",
        "protectionLevel": "normal",
        "label": "prevent phone from sleeping"
    },
    "android.permission.BIND_VOICE_INTERACTION": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a voice interaction service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a voice interactor"
    },
    "android.permission.STATUS_BAR_SERVICE": {
        "permissionGroup": "",
        "description": "Allows the app to be the status bar.",
        "protectionLevel": "signature",
        "label": "status bar"
    },
    "android.permission.DELETE_CACHE_FILES": {
        "permissionGroup": "",
        "description": "Allows the app to delete cache files.",
        "protectionLevel": "signature|system",
        "label": "delete other apps\' caches"
    },
    "android.permission.MODIFY_NETWORK_ACCOUNTING": {
        "permissionGroup": "",
        "description":
        "Allows the app to modify how network usage is accounted against apps. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "modify network usage accounting"
    },
    "android.permission.GET_ACCOUNTS": {
        "permissionGroup": "android.permission-group.ACCOUNTS",
        "description":
        "Allows the app to get the list of accounts known by the phone. This may include any accounts created by applications you have installed.",
        "protectionLevel": "normal",
        "label": "find accounts on the device"
    },
    "android.permission.CHANGE_NETWORK_STATE": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to change the state of network connectivity.",
        "protectionLevel": "normal",
        "label": "change network connectivity"
    },
    "android.permission.ACCESS_MTP": {
        "permissionGroup": "android.permission-group.HARDWARE_CONTROLS",
        "description":
        "Allows access to the kernel MTP driver to implement the MTP USB protocol.",
        "protectionLevel": "signature|system",
        "label": "implement MTP protocol"
    },
    "android.permission.DISABLE_KEYGUARD": {
        "permissionGroup": "android.permission-group.SCREENLOCK",
        "description":
        "Allows the app to disable the keylock and any associated password security. For example, the phone disables the keylock when receiving an incoming phone call, then re-enables the keylock when the call is finished.",
        "protectionLevel": "dangerous",
        "label": "disable your screen lock"
    },
    "android.permission.BIND_PACKAGE_VERIFIER": {
        "permissionGroup": "",
        "description":
        "Allows the holder to make requests of package verifiers. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a package verifier"
    },
    "com.android.launcher.permission.UNINSTALL_SHORTCUT": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the application to remove Homescreen shortcuts without user intervention.",
        "protectionLevel": "dangerous",
        "label": "uninstall shortcuts"
    },
    "android.permission.USE_CREDENTIALS": {
        "permissionGroup": "android.permission-group.ACCOUNTS",
        "description": "Allows the app to request authentication tokens.",
        "protectionLevel": "dangerous",
        "label": "use accounts on the device"
    },
    "android.permission.WRITE_MEDIA_STORAGE": {
        "permissionGroup": "android.permission-group.STORAGE",
        "description":
        "Allows the app to modify the contents of the internal media storage.",
        "protectionLevel": "signature|system",
        "label": "modify/delete internal media storage contents"
    },
    "android.permission.ACCESS_COARSE_LOCATION": {
        "permissionGroup": "android.permission-group.LOCATION",
        "description":
        "Allows the app to get your approximate location. This location is derived by location services using network location sources such as cell towers and Wi-Fi. These location services must be turned on and available to your device for the app to use them. Apps may use this to determine approximately where you are.",
        "protectionLevel": "dangerous",
        "label": "approximate location (network-based)"
    },
    "android.permission.BIND_KEYGUARD_APPWIDGET": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.BIND_TRUST_AGENT": {
        "permissionGroup": "",
        "description":
        "Allows an application to bind to a trust agent service.",
        "protectionLevel": "signature",
        "label": "Bind to a trust agent service"
    },
    "android.permission.BLUETOOTH_ADMIN": {
        "permissionGroup": "android.permission-group.BLUETOOTH_NETWORK",
        "description":
        "Allows the app to configure the local Bluetooth phone, and to discover and pair with remote devices.",
        "protectionLevel": "dangerous",
        "label": "access Bluetooth settings"
    },
    "android.permission.PERSISTENT_ACTIVITY": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to make parts of itself persistent in memory. This can limit memory available to other apps slowing down the phone.",
        "protectionLevel": "normal",
        "label": "make app always run"
    },
    "android.permission.TRUST_LISTENER": {
        "permissionGroup": "",
        "description":
        "Allows an application to listen for changes in trust state.",
        "protectionLevel": "signature",
        "label": "Listen to trust state changes."
    },
    "android.permission.BIND_TEXT_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a text service(e.g. SpellCheckerService). Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a text service"
    },
    "android.permission.RECEIVE_WAP_PUSH": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to receive and process WAP messages. This permission includes the ability to monitor or delete messages sent to you without showing them to you.",
        "protectionLevel": "dangerous",
        "label": "receive text messages (WAP)"
    },
    "com.foo.mypermission2": {
        "permissionGroup": "",
        "description": "MyActivity",
        "protectionLevel": "",
        "label": "MyActivity"
    },
    "android.permission.SET_WALLPAPER": {
        "permissionGroup": "android.permission-group.WALLPAPER",
        "description": "Allows the app to set the system wallpaper.",
        "protectionLevel": "normal",
        "label": "set wallpaper"
    },
    "android.permission.PROVIDE_TRUST_AGENT": {
        "permissionGroup": "",
        "description": "Allows an application to provide a trust agent.",
        "protectionLevel": "signatureOrSystem",
        "label": "Provide a trust agent."
    },
    "android": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "",
        "label": ""
    },
    "android.permission.BIND_PRINT_SPOOLER_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a print spooler service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a print spooler service"
    },
    "android.permission.GET_PACKAGE_SIZE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to retrieve its code, data, and cache sizes",
        "protectionLevel": "normal",
        "label": "measure app storage space"
    },
    "android.permission.BIND_REMOTE_DISPLAY": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a remote display. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a remote display"
    },
    "android.permission.READ_EXTERNAL_STORAGE": {
        "permissionGroup": "android.permission-group.STORAGE",
        "description": "Allows the app to read the contents of your SD card.",
        "protectionLevel": "normal",
        "label": "read the contents of your SD card"
    },
    "android.permission.SET_KEYBOARD_LAYOUT": {
        "permissionGroup": "",
        "description":
        "Allows the app to change the keyboard layout. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "change keyboard layout"
    },
    "com.android.frameworks.coretests.SIGNATURE": {
        "permissionGroup": "android.permission-group.COST_MONEY",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.INTERNAL_SYSTEM_WINDOW": {
        "permissionGroup": "",
        "description":
        "Allows the app to create windows that are intended to be used by the internal system user interface. Not for use by normal apps.",
        "protectionLevel": "signature",
        "label": "display unauthorized windows"
    },
    "com.android.cts.intent.sender.permission.SAMPLE": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "",
        "label": ""
    },
    "com.android.launcher3.permission.RECEIVE_FIRST_LOAD_BROADCAST": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": ""
    },
    "android.permission.PERFORM_CDMA_PROVISIONING": {
        "permissionGroup": "",
        "description":
        "Allows the app to start CDMA provisioning. Malicious apps may unnecessarily start CDMA provisioning.",
        "protectionLevel": "signature|system",
        "label": "directly start CDMA phone setup"
    },
    "com.android.browser.permission.PRELOAD": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": "Preload results"
    },
    "android.permission.MODIFY_AUDIO_SETTINGS": {
        "permissionGroup": "android.permission-group.AUDIO_SETTINGS",
        "description":
        "Allows the app to modify global audio settings such as volume and which speaker is used for output.",
        "protectionLevel": "normal",
        "label": "change your audio settings"
    },
    "android.permission.CONTROL_WIFI_DISPLAY": {
        "permissionGroup": "",
        "description":
        "Allows the app to control low-level features of Wifi displays.",
        "protectionLevel": "signature",
        "label": "control Wifi displays"
    },
    "android.permission.SET_ACTIVITY_WATCHER": {
        "permissionGroup": "",
        "description":
        "Allows the app to monitor and control how the system launches activities. Malicious apps may completely compromise the system. This permission is only needed for development, never for normal use.",
        "protectionLevel": "signature",
        "label": "monitor and control all app launching"
    },
    "com.android.frameworks.coretests.NORMAL": {
        "permissionGroup": "android.permission-group.COST_MONEY",
        "description": "",
        "protectionLevel": "normal",
        "label": ""
    },
    "android.permission.COPY_PROTECTED_DATA": {
        "permissionGroup": "",
        "description": "copy content",
        "protectionLevel": "signature",
        "label": "copy content"
    },
    "android.permission.RETRIEVE_WINDOW_TOKEN": {
        "permissionGroup": "",
        "description":
        "Allows an application to retrieve the window token. Malicious apps may perfrom unauthorized interaction with the application window impersonating the system.",
        "protectionLevel": "signature",
        "label": "retrieve window token"
    },
    "com.android.cts.permissionWithSignature": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.PACKAGE_USAGE_STATS": {
        "permissionGroup": "",
        "description":
        "Allows the app to modify collected component usage statistics. Not for use by normal apps.",
        "protectionLevel": "signature|development|appop",
        "label": "update component usage statistics"
    },
    "android.permission.RECEIVE_BLUETOOTH_MAP": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to receive and process Bluetooth MAP messages. This means the app could monitor or delete messages sent to your device without showing them to you.",
        "protectionLevel": "signature|system",
        "label": "receive Bluetooth messages (MAP)"
    },
    "android.permission.BROADCAST_CALLLOG_INFO": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.CONTROL_INCALL_EXPERIENCE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description": "Allows the app to provide an in-call user experience.",
        "protectionLevel": "system|signature",
        "label": "provide an in-call user experience"
    },
    "android.permission.MOUNT_UNMOUNT_FILESYSTEMS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to mount and unmount filesystems for removable storage.",
        "protectionLevel": "system|signature",
        "label": "access SD Card filesystem"
    },
    "android.permission.BIND_WALLPAPER": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a wallpaper. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "bind to a wallpaper"
    },
    "android.permission.READ_DREAM_STATE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.NFC_HANDOVER_STATUS": {
        "permissionGroup": "",
        "description":
        "Allows this application to receive information about current Android Beam transfers",
        "protectionLevel": "signature|system",
        "label": "Receive Android Beam transfer status"
    },
    "android.permission.FORCE_BACK": {
        "permissionGroup": "",
        "description":
        "Allows the app to force any activity that is in the foreground to close and go back. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "force app to close"
    },
    "android.permission.READ_CALENDAR": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description":
        "Allows the app to read all calendar events stored on your phone, including those of friends or co-workers. This may allow the app to share or save your calendar data, regardless of confidentiality or sensitivity.",
        "protectionLevel": "dangerous",
        "label": "read calendar events plus confidential information"
    },
    "android.permission.DEVICE_POWER": {
        "permissionGroup": "",
        "description": "Allows the app to turn the phone on or off.",
        "protectionLevel": "signature",
        "label": "power phone on or off"
    },
    "android.permission.SHUTDOWN": {
        "permissionGroup": "",
        "description":
        "Puts the activity manager into a shutdown state. Does not perform a complete shutdown.",
        "protectionLevel": "signature|system",
        "label": "partial shutdown"
    },
    "android.os.cts.permission.TEST_GRANTED": {
        "permissionGroup": "",
        "description":
        "Used for running CTS tests, for testing operations where we have the permission.",
        "protectionLevel": "normal",
        "label": "Test Granted"
    },
    "android.permission.CHANGE_CONFIGURATION": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to change the current configuration, such as the locale or overall font size.",
        "protectionLevel": "signature|system|development",
        "label": "change system display settings"
    },
    "android.permission.READ_CONTACTS": {
        "permissionGroup": "android.permission-group.SOCIAL_INFO",
        "description":
        "Allows the app to read data about your contacts stored on your phone, including the frequency with which you\'ve called, emailed, or communicated in other ways with specific individuals. This permission allows apps to save your contact data, and malicious apps may share contact data without your knowledge.",
        "protectionLevel": "dangerous",
        "label": "read your contacts"
    },
    "android.permission.BIND_DREAM_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a dream service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a dream service"
    },
    "android.permission.SEND_DOWNLOAD_COMPLETED_INTENTS": {
        "permissionGroup": "",
        "description":
        "Allows the app to send notifications about completed downloads. Malicious apps can use this to confuse other apps that download files.",
        "protectionLevel": "signature",
        "label": "Send download notifications."
    },
    "android.permission.READ_CALL_LOG": {
        "permissionGroup": "android.permission-group.SOCIAL_INFO",
        "description":
        "Allows the app to read your phone\'s call log, including data about incoming and outgoing calls. This permission allows apps to save your call log data, and malicious apps may share call log data without your knowledge.",
        "protectionLevel": "dangerous",
        "label": "read call log"
    },
    "android.permission.BLUETOOTH_PRIVILEGED": {
        "permissionGroup": "android.permission-group.BLUETOOTH_NETWORK",
        "description":
        "Allows the app to pair with remote devices without user interaction.",
        "protectionLevel": "system|signature",
        "label": "allow Bluetooth pairing by Application"
    },
    "android.permission.WRITE_CALL_LOG": {
        "permissionGroup": "android.permission-group.SOCIAL_INFO",
        "description":
        "Allows the app to modify your phone\'s call log, including data about incoming and outgoing calls. Malicious apps may use this to erase or modify your call log.",
        "protectionLevel": "dangerous",
        "label": "write call log"
    },
    "android.permission.CHANGE_WIFI_MULTICAST_STATE": {
        "permissionGroup": "android.permission-group.AFFECTS_BATTERY",
        "description":
        "Allows the app to receive packets sent to all devices on a Wi-Fi network using multicast addresses, not just your phone. It uses more power than the non-multicast mode.",
        "protectionLevel": "dangerous",
        "label": "allow Wi-Fi Multicast reception"
    },
    "android.permission.MODIFY_APPWIDGET_BIND_PERMISSIONS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.SET_TIME_ZONE": {
        "permissionGroup": "android.permission-group.SYSTEM_CLOCK",
        "description": "Allows the app to change the phone\'s time zone.",
        "protectionLevel": "normal",
        "label": "set time zone"
    },
    "android.permission.HDMI_CEC": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signatureOrSystem",
        "label": ""
    },
    "android.permission.WRITE_SYNC_SETTINGS": {
        "permissionGroup": "android.permission-group.SYNC_SETTINGS",
        "description":
        "Allows an app to modify the sync settings for an account. For example, this can be used to enable sync of the People app with an account.",
        "protectionLevel": "normal",
        "label": "toggle sync on and off"
    },
    "android.permission.CRYPT_KEEPER": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.READ_LOGS": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to read from the system\'s various log files. This allows it to discover general information about what you are doing with the phone, potentially including personal or private information.",
        "protectionLevel": "signature|system|development",
        "label": "read sensitive log data"
    },
    "android.permission.WRITE_GSERVICES": {
        "permissionGroup": "",
        "description":
        "Allows the app to modify the Google services map. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "modify the Google services map"
    },
    "android.permission.SET_ORIENTATION": {
        "permissionGroup": "",
        "description":
        "Allows the app to change the rotation of the screen at any time. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "change screen orientation"
    },
    "android.permission.BROADCAST_STICKY": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to send sticky broadcasts, which remain after the broadcast ends. Excessive use may make the phone slow or unstable by causing it to use too much memory.",
        "protectionLevel": "normal",
        "label": "send sticky broadcast"
    },
    "android.permission.FORCE_STOP_PACKAGES": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows the app to forcibly stop other apps.",
        "protectionLevel": "signature|system",
        "label": "force stop other apps"
    },
    "com.android.frameworks.coretests.permission.TEST_DENIED": {
        "permissionGroup": "",
        "description":
        "Used for running unit tests, for testing operations where we do not have the permission.",
        "protectionLevel": "normal",
        "label": "Test Denied"
    },
    "android.permission.BROADCAST_SCORE_NETWORKS": {
        "permissionGroup": "",
        "description":
        "Allows the app to broadcast a notification that networks need to be scored. Never needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "send score networks broadcast"
    },
    "com.android.providers.tv.permission.READ_EPG_DATA": {
        "permissionGroup": "",
        "description":
        "Allows the app to read the TV channel/program information stored on your device.",
        "protectionLevel": "dangerous",
        "label": "read TV channel/program information"
    },
    "android.permission.UPDATE_DEVICE_STATS": {
        "permissionGroup": "",
        "description":
        "Allows the app to modify collected battery statistics. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "modify battery statistics"
    },
    "android.permission.ACCESS_LOCATION_EXTRA_COMMANDS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to access extra location provider commands. This may allow the app to interfere with the operation of the GPS or other location sources.",
        "protectionLevel": "normal",
        "label": "access extra location provider commands"
    },
    "android.permission.GET_TASKS": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to retrieve information about currently and recently running tasks. This may allow the app to discover information about which applications are used on the device.",
        "protectionLevel": "normal",
        "label": "retrieve running apps"
    },
    "android.permission.CHANGE_WIFI_STATE": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to connect to and disconnect from Wi-Fi access points and to make changes to device configuration for Wi-Fi networks.",
        "protectionLevel": "dangerous",
        "label": "connect and disconnect from Wi-Fi"
    },
    "android.permission.RECEIVE_SMS": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to receive and process SMS messages. This means the app could monitor or delete messages sent to your device without showing them to you.",
        "protectionLevel": "dangerous",
        "label": "receive text messages (SMS)"
    },
    "android.permission.READ_PROFILE": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description":
        "Allows the app to read personal profile information stored on your device, such as your name and contact information. This means the app can identify you and may send your profile information to others.",
        "protectionLevel": "dangerous",
        "label": "read your own contact card"
    },
    "android.permission.ACCESS_NETWORK_CONDITIONS": {
        "permissionGroup": "",
        "description":
        "Allows an application to listen for observations on network conditions. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "listen for observations on network conditions"
    },
    "android.permission.ACCOUNT_MANAGER": {
        "permissionGroup": "android.permission-group.ACCOUNTS",
        "description": "Allows the app to make calls to AccountAuthenticators.",
        "protectionLevel": "signature",
        "label": "act as the AccountManagerService"
    },
    "android.permission.SET_ANIMATION_SCALE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to change the global animation speed (faster or slower animations) at any time.",
        "protectionLevel": "signature|system|development",
        "label": "modify global animation speed"
    },
    "com.android.certinstaller.INSTALL_AS_USER": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.BLUETOOTH_STACK": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.SET_PROCESS_LIMIT": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to control the maximum number of processes that will run. Never needed for normal apps.",
        "protectionLevel": "signature|system|development",
        "label": "limit number of running processes"
    },
    "android.permission.MOVE_PACKAGE": {
        "permissionGroup": "",
        "description":
        "Allows the app to move app resources from internal to external media and vice versa.",
        "protectionLevel": "signature|system",
        "label": "move app resources"
    },
    "com.android.cts.permissionAllowedWithSignature": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.SET_DEBUG_APP": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to turn on debugging for another app. Malicious apps may use this to kill other apps.",
        "protectionLevel": "signature|system|development",
        "label": "enable app debugging"
    },
    "android.permission.BRICK": {
        "permissionGroup": "",
        "description":
        "Allows the app to disable the entire phone permanently. This is very dangerous.",
        "protectionLevel": "signature",
        "label": "permanently disable phone"
    },
    "android.permission.BLUETOOTH": {
        "permissionGroup": "android.permission-group.BLUETOOTH_NETWORK",
        "description":
        "Allows the app to view the configuration of the Bluetooth on the phone, and to make and accept connections with paired devices.",
        "protectionLevel": "dangerous",
        "label": "pair with Bluetooth devices"
    },
    "com.android.launcher3.permission.RECEIVE_LAUNCH_BROADCASTS": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.MMS_SEND_OUTBOX_MSG": {
        "permissionGroup": "",
        "description": "Sends out all MMSs from the outbox to the network",
        "protectionLevel": "signatureOrSystem",
        "label": "MMS Wakeup"
    },
    "android.permission.UPDATE_APP_OPS_STATS": {
        "permissionGroup": "",
        "description":
        "Allows the app to modify collected application operation statistics. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "modify app ops statistics"
    },
    "android.permission.READ_PRIVILEGED_PHONE_STATE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.SET_WALLPAPER_COMPONENT": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "com.android.launcher3.permission.READ_SETTINGS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to read the settings and shortcuts in Home.",
        "protectionLevel": "normal",
        "label": "read Home settings and shortcuts"
    },
    "android.permission.WRITE_DREAM_STATE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.ACCESS_BLUETOOTH_SHARE": {
        "permissionGroup": "",
        "description":
        "Allows the app to access the BluetoothShare manager and use it to transfer files.",
        "protectionLevel": "signature",
        "label": "Access download manager."
    },
    "android.permission.READ_WIFI_CREDENTIAL": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.intent.category.MASTER_CLEAR.permission.C2D_MESSAGE": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.UPDATE_LOCK": {
        "permissionGroup": "",
        "description":
        "Allows the holder to offer information to the system about when would be a good time for a noninteractive reboot to upgrade the device.",
        "protectionLevel": "signatureOrSystem",
        "label": "discourage automatic device updates"
    },
    "com.android.cts.keysets_permdef.keysets_perm": {
        "permissionGroup": "",
        "description": "keysets_perm_description",
        "protectionLevel": "signature",
        "label": "keysets_perm_label"
    },
    "android.permission.WRITE_USER_DICTIONARY": {
        "permissionGroup": "android.permission-group.WRITE_USER_DICTIONARY",
        "description":
        "Allows the app to write new words into the user dictionary.",
        "protectionLevel": "normal",
        "label": "add words to user-defined dictionary"
    },
    "com.android.browser.permission.READ_HISTORY_BOOKMARKS": {
        "permissionGroup": "android.permission-group.BOOKMARKS",
        "description":
        "Allows the app to read the history of all URLs that the Browser has visited, and all of the Browser\'s bookmarks. Note: this permission may not be enforced by third-party browsers or other applications with web browsing capabilities.",
        "protectionLevel": "dangerous",
        "label": "read your Web bookmarks and history"
    },
    "android.permission.RECORD_AUDIO": {
        "permissionGroup": "android.permission-group.MICROPHONE",
        "description":
        "Allows the app to record audio with the microphone. This permission allows the app to record audio at any time without your confirmation.",
        "protectionLevel": "dangerous",
        "label": "record audio"
    },
    "android.permission.WRITE_CONTACTS": {
        "permissionGroup": "android.permission-group.SOCIAL_INFO",
        "description":
        "Allows the app to modify the data about your contacts stored on your phone, including the frequency with which you\'ve called, emailed, or communicated in other ways with specific contacts. This permission allows apps to delete contact data.",
        "protectionLevel": "dangerous",
        "label": "modify your contacts"
    },
    "android.permission.CONTROL_LOCATION_UPDATES": {
        "permissionGroup": "",
        "description":
        "Allows the app to enable/disable location update notifications from the radio. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "control location update notifications"
    },
    "android.permission.ACCESS_KEYGUARD_SECURE_STORAGE": {
        "permissionGroup": "",
        "description":
        "Allows an application to access keguard secure storage.",
        "protectionLevel": "signature",
        "label": "Access keyguard secure storage"
    },
    "android.permission.BIND_CONDITION_PROVIDER_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a condition provider service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to a condition provider service"
    },
    "android.permission.SIGNAL_PERSISTENT_PROCESSES": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to request that the supplied signal be sent to all persistent processes.",
        "protectionLevel": "signature|system|development",
        "label": "send Linux signals to apps"
    },
    "android.permission.MANAGE_VOICE_KEYPHRASES": {
        "permissionGroup": "",
        "description":
        "Allows the holder to manage the keyphrases for voice hotword detection. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "manage voice keyphrases"
    },
    "android.permission.MASTER_CLEAR": {
        "permissionGroup": "",
        "description":
        "Allows the app to completely reset the system to its factory settings, erasing all data, configuration, and installed apps.",
        "protectionLevel": "signature|system",
        "label": "reset system to factory defaults"
    },
    "android.permission.READ_INPUT_STATE": {
        "permissionGroup": "",
        "description":
        "Allows the app to watch the keys you press even when interacting with another app (such as typing a password). Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "record what you type and actions you take"
    },
    "android.permission.INJECT_EVENTS": {
        "permissionGroup": "",
        "description":
        "Allows the app to deliver its own input events (key presses, etc.) to other apps. Malicious apps may use this to take over the phone.",
        "protectionLevel": "signature",
        "label": "press keys and control buttons"
    },
    "com.android.email.permission.ACCESS_PROVIDER": {
        "permissionGroup": "",
        "description":
        "Allows the app to access your email database, including received messages, sent messages, usernames, and passwords.",
        "protectionLevel": "signature",
        "label": "Access email provider data"
    },
    "org.chromium.content_shell.permission.SANDBOX": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.ACCESS_WIMAX_STATE": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to determine whether WiMAX is enabled and information about any WiMAX networks that are connected.",
        "protectionLevel": "normal",
        "label": "connect and disconnect from WiMAX"
    },
    "com.android.launcher.permission.WRITE_SETTINGS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to change the settings and shortcuts in Home.",
        "protectionLevel": "signatureOrSystem",
        "label": "write Home settings and shortcuts"
    },
    "android.permission.FREEZE_SCREEN": {
        "permissionGroup": "",
        "description":
        "Allows the application to temporarily freeze the screen for a full-screen transition.",
        "protectionLevel": "signature",
        "label": "freeze screen"
    },
    "android.permission.GET_TOP_ACTIVITY_INFO": {
        "permissionGroup": "",
        "description":
        "Allows the holder to retrieve private information about the current application in the foreground of the screen.",
        "protectionLevel": "signature",
        "label": "get current app info"
    },
    "android.permission.WRITE_APN_SETTINGS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to change network settings and to intercept and inspect all network traffic, for example to change the proxy and port of any APN. Malicious apps may monitor, redirect, or modify network packets without your knowledge.",
        "protectionLevel": "signature|system",
        "label": "change/intercept network settings and traffic"
    },
    "android.permission.ACCESS_SURFACE_FLINGER": {
        "permissionGroup": "",
        "description":
        "Allows the app to use SurfaceFlinger low-level features.",
        "protectionLevel": "signature",
        "label": "access SurfaceFlinger"
    },
    "android.permission.USER_ACTIVITY": {
        "permissionGroup": "",
        "description": "Allows the app to reset the display timeout.",
        "protectionLevel": "signature|system",
        "label": "reset display timeout"
    },
    "android.permission.SERIAL_PORT": {
        "permissionGroup": "",
        "description":
        "Allows the holder to access serial ports using the SerialManager API.",
        "protectionLevel": "signature|system",
        "label": "access serial ports"
    },
    "android.permission.ALLOW_ANY_CODEC_FOR_PLAYBACK": {
        "permissionGroup": "",
        "description":
        "Allows the app to use any installed media decoder to decode for playback.",
        "protectionLevel": "signature|system",
        "label": "use any media decoder for playback"
    },
    "android.permission.MANAGE_USB": {
        "permissionGroup": "android.permission-group.HARDWARE_CONTROLS",
        "description":
        "Allows the app to manage preferences and permissions for USB devices.",
        "protectionLevel": "signature|system",
        "label": "manage preferences and permissions for USB devices"
    },
    "android.permission.PROCESS_OUTGOING_CALLS": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description":
        "Allows the app to see the number being dialed during an outgoing call with the option to redirect the call to a different number or abort the call altogether.",
        "protectionLevel": "dangerous",
        "label": "reroute outgoing calls"
    },
    "android.permission.CALL_PRIVILEGED": {
        "permissionGroup": "",
        "description":
        "Allows the app to call any phone number, including emergency numbers, without your intervention. Malicious apps may place unnecessary and illegal calls to emergency services.",
        "protectionLevel": "signature|system",
        "label": "directly call any phone numbers"
    },
    "com.android.gallery3d.filtershow.permission.WRITE": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.WRITE_CALENDAR": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description":
        "Allows the app to add, remove, change events that you can modify on your phone, including those of friends or co-workers. This may allow the app to send messages that appear to come from calendar owners, or modify events without the owners\' knowledge.",
        "protectionLevel": "dangerous",
        "label":
        "add or modify calendar events and send email to guests without owners\' knowledge"
    },
    "android.permission.ACCESS_CONTENT_PROVIDERS_EXTERNALLY": {
        "permissionGroup": "",
        "description":
        "Allows the holder to access content providers from the shell. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "access content providers externally"
    },
    "android.permission.SUBSCRIBED_FEEDS_READ": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to get details about the currently synced feeds.",
        "protectionLevel": "normal",
        "label": "read subscribed feeds"
    },
    "android.permission.MANAGE_ACCOUNTS": {
        "permissionGroup": "android.permission-group.ACCOUNTS",
        "description":
        "Allows the app to perform operations like adding and removing accounts, and deleting their password.",
        "protectionLevel": "dangerous",
        "label": "add or remove accounts"
    },
    "android.permission.BIND_INCALL_SERVICE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description":
        "Allows the app to control when and how the user sees the in-call screen.",
        "protectionLevel": "system|signature",
        "label": "interact with in-call screen"
    },
    "android.permission.BIND_REMOTEVIEWS": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of a widget service. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "bind to a widget service"
    },
    "android.permission.BIND_ACCESSIBILITY_SERVICE": {
        "permissionGroup": "",
        "description":
        "Allows the holder to bind to the top-level interface of an accessibility service. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "bind to an accessibility service"
    },
    "android.permission.ACCESS_NOTIFICATIONS": {
        "permissionGroup": "",
        "description":
        "Allows the app to retrieve, examine, and clear notifications, including those posted by other apps.",
        "protectionLevel": "signature|system",
        "label": "access notifications"
    },
    "com.android.server.telecom.permission.REGISTER_CONNECTION_MANAGER": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.WRITE_SMS": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to write to SMS messages stored on your phone or SIM card. Malicious apps may delete your messages.",
        "protectionLevel": "dangerous",
        "label": "edit your text messages (SMS or MMS)"
    },
    "android.permission.DELETE_PACKAGES": {
        "permissionGroup": "",
        "description":
        "Allows the app to delete Android packages. Malicious apps may use this to delete important apps.",
        "protectionLevel": "signature|system",
        "label": "delete apps"
    },
    "android.permission.FILTER_EVENTS": {
        "permissionGroup": "",
        "description":
        "Allows an application to register an input filter which filters the stream of all user events before they are dispatched. Malicious app may control the system UI whtout user intervention.",
        "protectionLevel": "signature",
        "label": "filter events"
    },
    "android.permission.ACCESS_CHECKIN_PROPERTIES": {
        "permissionGroup": "",
        "description":
        "Allows the app read/write access to properties uploaded by the checkin service. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "access checkin properties"
    },
    "android.permission.SEND_RESPOND_VIA_MESSAGE": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to send requests to other messaging apps to handle respond-via-message events for incoming calls.",
        "protectionLevel": "signature|system",
        "label": "send respond-via-message events"
    },
    "com.android.voicemail.permission.WRITE_VOICEMAIL": {
        "permissionGroup": "android.permission-group.VOICEMAIL",
        "description":
        "Allows the app to modify and remove messages from your voicemail inbox.",
        "protectionLevel": "system|signature",
        "label": "write voicemails"
    },
    "android.permission.RETRIEVE_WINDOW_CONTENT": {
        "permissionGroup": "android.permission-group.PERSONAL_INFO",
        "description":
        "Allows the app to retrieve the content of the active window. Malicious apps may retrieve the entire window content and examine all its text except passwords.",
        "protectionLevel": "signature|system",
        "label": "retrieve screen content"
    },
    "android.permission.SET_PREFERRED_APPLICATIONS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to modify your preferred apps. Malicious apps may silently change the apps that are run, spoofing your existing apps to collect private data from you.",
        "protectionLevel": "signature",
        "label": "set preferred apps"
    },
    "android.permission.VIBRATE": {
        "permissionGroup": "android.permission-group.AFFECTS_BATTERY",
        "description": "Allows the app to control the vibrator.",
        "protectionLevel": "normal",
        "label": "control vibration"
    },
    "android.app.cts.permission.TEST_GRANTED": {
        "permissionGroup": "",
        "description":
        "Used for running CTS tests, for testing operations where we have the permission.",
        "protectionLevel": "normal",
        "label": "Test Granted"
    },
    "android.permission.DIAGNOSTIC": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to read and write to any resource owned by the diag group; for example, files in /dev. This could potentially affect system stability and security. This should be ONLY be used for hardware-specific diagnostics by the manufacturer or operator.",
        "protectionLevel": "signature",
        "label": "read/write to resources owned by diag"
    },
    "android.permission.BIND_JOB_SERVICE": {
        "permissionGroup": "",
        "description":
        "This permission allows the Android system to run the application in the background when requested.",
        "protectionLevel": "signature",
        "label": "run the application\'s scheduled background work"
    },
    "org.chromium.chrome.shell.permission.SANDBOX": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.INTERACT_ACROSS_USERS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to perform actions across different users on the device. Malicious apps may use this to violate the protection between users.",
        "protectionLevel": "signature|system|development",
        "label": "interact across users"
    },
    "android.permission.BROADCAST_SMS": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to broadcast a notification that an SMS message has been received. Malicious apps may use this to forge incoming SMS messages.",
        "protectionLevel": "signature",
        "label": "send SMS-received broadcast"
    },
    "android.permission.BLUETOOTH_MAP": {
        "permissionGroup": "android.permission-group.BLUETOOTH_NETWORK",
        "description": "Allows the app to access Bluetooth MAP data.",
        "protectionLevel": "signature",
        "label": "access Bluetooth MAP data"
    },
    "android.permission.READ_FRAME_BUFFER": {
        "permissionGroup": "",
        "description":
        "Allows the app to read the content of the frame buffer.",
        "protectionLevel": "signature|system",
        "label": "read frame buffer"
    },
    "android.permission.STOP_APP_SWITCHES": {
        "permissionGroup": "",
        "description": "Prevents the user from switching to another app.",
        "protectionLevel": "signature|system",
        "label": "prevent app switches"
    },
    "android.permission.ACCESS_WIFI_STATE": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description":
        "Allows the app to view information about Wi-Fi networking, such as whether Wi-Fi is enabled and name of connected Wi-Fi devices.",
        "protectionLevel": "normal",
        "label": "view Wi-Fi connections"
    },
    "android.permission.GLOBAL_SEARCH_CONTROL": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.ACCESS_DOWNLOAD_MANAGER": {
        "permissionGroup": "",
        "description":
        "Allows the app to access the download manager and to use it to download files. Malicious apps can use this to disrupt downloads and access private information.",
        "protectionLevel": "signatureOrSystem",
        "label": "Access download manager."
    },
    "com.android.launcher3.permission.WRITE_SETTINGS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to change the settings and shortcuts in Home.",
        "protectionLevel": "signatureOrSystem",
        "label": "write Home settings and shortcuts"
    },
    "android.permission.MODIFY_PARENTAL_CONTROLS": {
        "permissionGroup": "",
        "description":
        "Allows the holder to modify the system\'s parental controls data. Should never be needed for normal apps.",
        "protectionLevel": "signature|system",
        "label": "modify parental controls"
    },
    "android.permission.READ_SYNC_SETTINGS": {
        "permissionGroup": "android.permission-group.SYNC_SETTINGS",
        "description":
        "Allows the app to read the sync settings for an account. For example, this can determine whether the People app is synced with an account.",
        "protectionLevel": "normal",
        "label": "read sync settings"
    },
    "android.permission.OEM_UNLOCK_STATE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.SUBSCRIBED_FEEDS_WRITE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to modify your currently synced feeds. Malicious apps may change your synced feeds.",
        "protectionLevel": "dangerous",
        "label": "write subscribed feeds"
    },
    "android.permission.READ_USER_DICTIONARY": {
        "permissionGroup": "android.permission-group.USER_DICTIONARY",
        "description":
        "Allows the app to read all words, names and phrases that the user may have stored in the user dictionary.",
        "protectionLevel": "dangerous",
        "label": "read terms you added to the dictionary"
    },
    "android.permission.READ_INSTALL_SESSIONS": {
        "permissionGroup": "",
        "description":
        "Allows an application to read install sessions. This allows it to see details about active package installations.",
        "protectionLevel": "",
        "label": "Read install sessions"
    },
    "android.permission.MANAGE_USERS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows apps to manage users on the device, including query, creation and deletion.",
        "protectionLevel": "signature|system",
        "label": "manage users"
    },
    "android.permission.FACTORY_TEST": {
        "permissionGroup": "",
        "description":
        "Run as a low-level manufacturer test, allowing complete access to the phone hardware. Only available when a phone is running in manufacturer test mode.",
        "protectionLevel": "signature",
        "label": "run in factory test mode"
    },
    "android.permission.CHANGE_COMPONENT_ENABLED_STATE": {
        "permissionGroup": "",
        "description":
        "Allows the app to change whether a component of another app is enabled or not. Malicious apps may use this to disable important phone capabilities. Care must be used with this permission, as it is possible to get app components into an unusable, inconsistent, or unstable state.",
        "protectionLevel": "signature|system",
        "label": "enable or disable app components"
    },
    "android.permission.RECEIVE_BOOT_COMPLETED": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to have itself started as soon as the system has finished booting. This can make it take longer to start the phone and allow the app to slow down the overall phone by always running.",
        "protectionLevel": "normal",
        "label": "run at startup"
    },
    "android.permission.SET_POINTER_SPEED": {
        "permissionGroup": "",
        "description":
        "Allows the app to change the mouse or trackpad pointer speed at any time. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "change pointer speed"
    },
    "android.permission.BACKUP": {
        "permissionGroup": "",
        "description":
        "Allows the app to control the system\'s backup and restore mechanism. Not for use by normal apps.",
        "protectionLevel": "signature|system",
        "label": "control system backup and restore"
    },
    "android.permission.TEMPORARY_ENABLE_ACCESSIBILITY": {
        "permissionGroup": "",
        "description":
        "Allows an application to temporarily enable accessibility on the device. Malicious apps may enable accessibility without user consent.",
        "protectionLevel": "signature",
        "label": "temporary enable accessibility"
    },
    "android.permission.EXPAND_STATUS_BAR": {
        "permissionGroup": "android.permission-group.STATUS_BAR",
        "description": "Allows the app to expand or collapse the status bar.",
        "protectionLevel": "normal",
        "label": "expand/collapse status bar"
    },
    "android.permission.ACCESS_FINE_LOCATION": {
        "permissionGroup": "android.permission-group.LOCATION",
        "description":
        "Allows the app to get your precise location using the Global Positioning System (GPS) or network location sources such as cell towers and Wi-Fi. These location services must be turned on and available to your device for the app to use them. Apps may use this to determine where you are, and may consume additional battery power.",
        "protectionLevel": "dangerous",
        "label": "precise location (GPS and network-based)"
    },
    "android.permission.ASEC_RENAME": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows the app to rename internal storage.",
        "protectionLevel": "signature",
        "label": "rename internal storage"
    },
    "android.permission.LOCATION_HARDWARE": {
        "permissionGroup": "android.permission-group.LOCATION",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "com.android.frameworks.coretests.keysets_permdef.keyset_perm": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.GET_APP_OPS_STATS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to retrieve collected application operation statistics. Not for use by normal apps.",
        "protectionLevel": "signature|system|development",
        "label": "retrieve app ops statistics"
    },
    "android.permission.REORDER_TASKS": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to move tasks to the foreground and background. The app may do this without your input.",
        "protectionLevel": "normal",
        "label": "reorder running apps"
    },
    "com.android.cts.permissionNormal": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "",
        "label": ""
    },
    "android.permission.CONTROL_KEYGUARD": {
        "permissionGroup": "",
        "description": "Allows an application to control keguard.",
        "protectionLevel": "signature",
        "label": "Control displaying and hiding keyguard"
    },
    "android.permission.ASEC_DESTROY": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows the app to destroy internal storage.",
        "protectionLevel": "signature",
        "label": "destroy internal storage"
    },
    "android.permission.BROADCAST_PACKAGE_REMOVED": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to broadcast a notification that an app package has been removed. Malicious apps may use this to kill any other running app.",
        "protectionLevel": "signature",
        "label": "send package removed broadcast"
    },
    "android.permission.MANAGE_ACTIVITY_STACKS": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to add, remove, and modify the activity stacks in which other apps run. Malicious apps may disrupt the behavior of other apps.",
        "protectionLevel": "signature|system",
        "label": "manage activity stacks"
    },
    "android.permission.CONNECTIVITY_INTERNAL": {
        "permissionGroup": "android.permission-group.NETWORK",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.SET_SCREEN_COMPATIBILITY": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to control the screen compatibility mode of other applications. Malicious applications may break the behavior of other applications.",
        "protectionLevel": "signature",
        "label": "set screen compatibility"
    },
    "android.permission.WRITE_EXTERNAL_STORAGE": {
        "permissionGroup": "android.permission-group.STORAGE",
        "description": "Allows the app to write to the SD card.",
        "protectionLevel": "dangerous",
        "label": "modify or delete the contents of your SD card"
    },
    "android.permission.CAMERA_DISABLE_TRANSMIT_LED": {
        "permissionGroup": "android.permission-group.CAMERA",
        "description":
        "Allows a pre-installed system application to disable the camera use indicator LED.",
        "protectionLevel": "signature|system",
        "label": "disable transmit indicator LED when camera is in use"
    },
    "com.android.frameworks.coretests.DANGEROUS": {
        "permissionGroup": "android.permission-group.COST_MONEY",
        "description": "",
        "protectionLevel": "dangerous",
        "label": ""
    },
    "android.permission.WRITE_SOCIAL_STREAM": {
        "permissionGroup": "android.permission-group.SOCIAL_INFO",
        "description":
        "Allows the app to display social updates from your friends. Be careful when sharing information -- this allows the app to produce messages that may appear to come from a friend. Note: this permission may not be enforced on all social networks.",
        "protectionLevel": "dangerous",
        "label": "write to your social stream"
    },
    "com.android.printspooler.permission.ACCESS_ALL_PRINT_JOBS": {
        "permissionGroup": "",
        "description":
        "Allows the holder to access print jobs created by another app. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "access all print jobs"
    },
    "android.permission.ASEC_MOUNT_UNMOUNT": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "Allows the app to mount/unmount internal storage.",
        "protectionLevel": "signature",
        "label": "mount/unmount internal storage"
    },
    "android.permission.INSTALL_PACKAGES": {
        "permissionGroup": "",
        "description":
        "Allows the app to install new or updated Android packages. Malicious apps may use this to add new apps with arbitrarily powerful permissions.",
        "protectionLevel": "signature|system",
        "label": "directly install apps"
    },
    "com.android.providers.tv.permission.WRITE_EPG_DATA": {
        "permissionGroup": "",
        "description":
        "Allows the app to provide and modify the TV channel/program information on your device.",
        "protectionLevel": "dangerous",
        "label": "write TV channel/program information"
    },
    "android.permission.RECEIVE_EMERGENCY_BROADCAST": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to receive and process emergency broadcast messages. This permission is only available to system apps.",
        "protectionLevel": "signature|system",
        "label": "receive emergency broadcasts"
    },
    "com.android.launcher.permission.READ_SETTINGS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to read the settings and shortcuts in Home.",
        "protectionLevel": "normal",
        "label": "read Home settings and shortcuts"
    },
    "com.android.alarm.permission.SET_ALARM": {
        "permissionGroup": "android.permission-group.DEVICE_ALARMS",
        "description":
        "Allows the app to set an alarm in an installed alarm clock app. Some alarm clock apps may not implement this feature.",
        "protectionLevel": "normal",
        "label": "set an alarm"
    },
    "android.permission.CAPTURE_VIDEO_OUTPUT": {
        "permissionGroup": "",
        "description": "Allows the app to capture and redirect video output.",
        "protectionLevel": "signature|system",
        "label": "capture video output"
    },
    "org.chromium.chrome.shell.permission.C2D_MESSAGE": {
        "permissionGroup": "",
        "description": "",
        "protectionLevel": "signature",
        "label": ""
    },
    "android.permission.READ_PRECISE_PHONE_STATE": {
        "permissionGroup": "android.permission-group.PHONE_CALLS",
        "description":
        "Allows the app to access the precise phone states. This permission allows the app to determine the real call status, whether a call is active or in the background, call fails, precise data connection status and data connection fails.",
        "protectionLevel": "signature|system",
        "label": "read precise phone states"
    },
    "android.permission.READ_SMS": {
        "permissionGroup": "android.permission-group.MESSAGES",
        "description":
        "Allows the app to read SMS messages stored on your phone or SIM card. This allows the app to read all SMS messages, regardless of content or confidentiality.",
        "protectionLevel": "dangerous",
        "label": "read your text messages (SMS or MMS)"
    },
    "android.permission.ACCESS_INPUT_FLINGER": {
        "permissionGroup": "",
        "description": "Allows the app to use InputFlinger low-level features.",
        "protectionLevel": "signature",
        "label": "access InputFlinger"
    },
    "android.permission.BATTERY_STATS": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows an application to read the current low-level battery use data. May allow the application to find out detailed information about which apps you use.",
        "protectionLevel": "signature|system|development",
        "label": "read battery statistics"
    },
    "android.permission.GLOBAL_SEARCH": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description": "",
        "protectionLevel": "signature|system",
        "label": ""
    },
    "android.permission.SET_INPUT_CALIBRATION": {
        "permissionGroup": "",
        "description":
        "Allows the app to modify the calibration parameters of the touch screen. Should never be needed for normal apps.",
        "protectionLevel": "signature",
        "label": "change input device calibration"
    },
    "android.permission.REMOVE_TASKS": {
        "permissionGroup": "android.permission-group.APP_INFO",
        "description":
        "Allows the app to remove tasks and kill their apps. Malicious apps may disrupt the behavior of other apps.",
        "protectionLevel": "signature",
        "label": "stop running apps"
    },
    "android.permission.SET_ALWAYS_FINISH": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to control whether activities are always finished as soon as they go to the background. Never needed for normal apps.",
        "protectionLevel": "signature|system|development",
        "label": "force background apps to close"
    },
    "android.permission.ACCESS_ALL_EXTERNAL_STORAGE": {
        "permissionGroup": "android.permission-group.DEVELOPMENT_TOOLS",
        "description":
        "Allows the app to access external storage for all users.",
        "protectionLevel": "signature",
        "label": "access external storage of all users"
    },
    "android.permission.CLEAR_APP_CACHE": {
        "permissionGroup": "android.permission-group.SYSTEM_TOOLS",
        "description":
        "Allows the app to free phone storage by deleting files in the cache directories of other applications. This may cause other applications to start up more slowly as they need to re-retrieve their data.",
        "protectionLevel": "dangerous",
        "label": "delete all app cache data"
    },
    "android.permission.MANAGE_NETWORK_POLICY": {
        "permissionGroup": "",
        "description":
        "Allows the app to manage network policies and define app-specific rules.",
        "protectionLevel": "signature",
        "label": "manage network policy"
    },
}

AOSP_PERMISSION_GROUPS = {
    "android.permission-group.AFFECTS_BATTERY": {
        "description": "Use features that can quickly drain battery.",
        "label": "Affects Battery"
    },
    "android.permission-group.PERSONAL_INFO": {
        "description":
        "Direct access to information about you, stored in on your contact card.",
        "label": "Your personal information"
    },
    "android.permission-group.WRITE_USER_DICTIONARY": {
        "description": "Add words to the user dictionary.",
        "label": "Write User Dictionary"
    },
    "android.permission-group.BLUETOOTH_NETWORK": {
        "description": "Access devices and networks through Bluetooth.",
        "label": "Bluetooth"
    },
    "android.permission-group.DISPLAY": {
        "description": "Effect the UI of other applications.",
        "label": "Other Application UI"
    },
    "android.permission-group.SCREENLOCK": {
        "description":
        "Ability to affect behavior of the lock screen on your device.",
        "label": "Lock screen"
    },
    "android.permission-group.STORAGE":
    {"description": "Access the SD card.",
     "label": "Storage"},
    "android.permission-group.APP_INFO": {
        "description":
        "Ability to affect behavior of other applications on your device.",
        "label": "Your applications information"
    },
    "android.permission-group.SYNC_SETTINGS":
    {"description": "Access to the sync settings.",
     "label": "Sync Settings"},
    "android.permission-group.AUDIO_SETTINGS":
    {"description": "Change audio settings.",
     "label": "Audio Settings"},
    "android.permission-group.WALLPAPER": {
        "description": "Change the device wallpaper settings.",
        "label": "Wallpaper"
    },
    "android.permission-group.CALENDAR": {
        "description": "Direct access to calendar and events.",
        "label": "Calendar"
    },
    "android.permission-group.DEVICE_ALARMS":
    {"description": "Set the alarm clock.",
     "label": "Alarm"},
    "android.permission-group.DEVELOPMENT_TOOLS": {
        "description": "Features only needed for app developers.",
        "label": "Development tools"
    },
    "android.permission-group.USER_DICTIONARY": {
        "description": "Read words in user dictionary.",
        "label": "Read User Dictionary"
    },
    "android.permission-group.VOICEMAIL":
    {"description": "Direct access to voicemail.",
     "label": "Voicemail"},
    "android.permission-group.LOCATION": {
        "description": "Monitor your physical location.",
        "label": "Your location"
    },
    "android.permission-group.STATUS_BAR": {
        "description": "Change the device status bar settings.",
        "label": "Status Bar"
    },
    "android.permission-group.SYSTEM_TOOLS": {
        "description": "Lower-level access and control of the system.",
        "label": "System tools"
    },
    "android.permission-group.SYSTEM_CLOCK":
    {"description": "Change the device time or timezone.",
     "label": "Clock"},
    "android.permission-group.SOCIAL_INFO": {
        "description":
        "Direct access to information about your contacts and social connections.",
        "label": "Your social information"
    },
    "android.permission-group.NETWORK": {
        "description": "Access various network features.",
        "label": "Network communication"
    },
    "android.permission-group.MESSAGES": {
        "description": "Read and write your SMS, email, and other messages.",
        "label": "Your messages"
    },
    "android.permission-group.MICROPHONE": {
        "description": "Direct access to the microphone to record audio.",
        "label": "Microphone"
    },
    "android.permission-group.ACCESSIBILITY_FEATURES": {
        "description": "Features that assistive technology can request.",
        "label": "Accessibility features"
    },
    "android.permission-group.ACCOUNTS": {
        "description": "Access the available accounts.",
        "label": "Your accounts"
    },
    "android.permission-group.COST_MONEY": {"description": "",
                                            "label": ""},
    "android.permission-group.CAMERA": {
        "description": "Direct access to camera for image or video capture.",
        "label": "Camera"
    },
    "android.permission-group.HARDWARE_CONTROLS": {
        "description": "Direct access to hardware on the handset.",
        "label": "Hardware controls"
    },
    "android.permission-group.PHONE_CALLS": {
        "description": "Monitor, record, and process phone calls.",
        "label": "Phone calls"
    },
    "android.permission-group.BOOKMARKS": {
        "description": "Direct access to bookmarks and browser history.",
        "label": "Bookmarks and History"
    },
}
#################################################
