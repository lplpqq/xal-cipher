import json

from xal import encode_data


serialized_data = {'fingerprint_version': 30, 'timestamp': '2023-07-23T15:10:20.749Z', 'math_rand': '135a8e5d615b26', 'document': {'title': 'Sign in to Your Epic Games account | Epic Games', 'referrer': ''}, 'navigator': {'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', 'platform': 'MacIntel', 'language': 'en-GB', 'languages': ['en-GB'], 'hardware_concurrency': 10, 'device_memory': 8, 'product': 'Gecko', 'product_sub': '20030107', 'vendor': 'Google Inc.', 'vendor_sub': '', 'webdriver': False, 'max_touch_points': 0, 'cookie_enabled': True, 'property_list': ['vendorSub', 'productSub', 'vendor', 'maxTouchPoints', 'scheduling', 'userActivation', 'doNotTrack', 'geolocation', 'connection', 'plugins', 'mimeTypes', 'pdfViewerEnabled', 'webkitTemporaryStorage', 'webkitPersistentStorage', 'hardwareConcurrency', 'cookieEnabled', 'appCodeName', 'appName', 'appVersion', 'platform', 'product', 'userAgent', 'language', 'languages', 'onLine', 'webdriver', 'getGamepads', 'javaEnabled', 'sendBeacon', 'vibrate', 'bluetooth', 'clipboard', 'credentials', 'keyboard', 'managed', 'mediaDevices', 'storage', 'serviceWorker', 'virtualKeyboard', 'wakeLock', 'deviceMemory', 'ink', 'hid', 'locks', 'mediaCapabilities', 'mediaSession', 'permissions', 'presentation', 'serial', 'usb', 'windowControlsOverlay', 'xr', 'userAgentData', 'clearAppBadge', 'getBattery', 'getUserMedia', 'requestMIDIAccess', 'requestMediaKeySystemAccess', 'setAppBadge', 'webkitGetUserMedia', 'getInstalledRelatedApps', 'registerProtocolHandler', 'unregisterProtocolHandler'], 'connection_rtt': 100}, 'web_gl': {'canvas_fingerprint': {'length': 36578, 'num_colors': 5496, 'md5': 'c766d5240eca3f299bc8a03ce6311171', 'tlsh': '08F2F18D4AFB8940077E41D23D75162BAA9382ED44E4907A1F7F36CBC4E9A0ADD45C1E'}, 'parameters': {'renderer': 'ANGLE (Apple, Apple M2 Pro, OpenGL 4.1)', 'vendor': 'Google Inc. (Apple)'}}, 'window': {'location': {'origin': 'https://www.epicgames.com', 'pathname': '/id/login/epic', 'href': 'https://www.epicgames.com/id/login/epic'}, 'history': {'length': 2}, 'screen': {'avail_height': 950, 'avail_width': 1512, 'avail_top': 32, 'height': 982, 'width': 1512, 'color_depth': 30}, 'performance': {'memory': {'js_heap_size_limit': 4294705152, 'total_js_heap_size': 43611555, 'used_js_heap_size': 26165111}, 'resources': ['https://static-assets-prod.unrealengine.com/account-portal/static/static/js/3.d886ac25.chunk.js', 'https://static-assets-prod.unrealengine.com/account-portal/static/static/js/main.13635d77.chunk.js', 'https://tracking.epicgames.com/tracking.js', 'https://static-assets-prod.unrealengine.com/account-portal/static/static/css/4.2a621477.chunk.css', 'https://static-assets-prod.unrealengine.com/account-portal/static/static/js/4.66f43835.chunk.js', 'https://static-assets-prod.unrealengine.com/account-portal/static/static/js/polyfills.1e00ef5d.chunk.js', 'https://www.epicgames.com/id/api/reputation', 'https://www.epicgames.com/id/api/location', 'https://www.epicgames.com/id/api/i18n?ns=messages', 'https://www.epicgames.com/id/api/i18n?ns=epic-consent-dialog', 'https://www.epicgames.com/id/api/i18n?ns=epic-consent-dialog', 'https://www.epicgames.com/id/api/i18n?ns=messages', 'https://www.epicgames.com/id/api/analytics', 'https://static-assets-prod.unrealengine.com/account-portal/static/epic-favicon-96x96.png', 'https://tracking.epicgames.com/track.png?referringUrl=none&location=https%3A%2F%2Fwww.epicgames.com%2Fid%2Flogin%2Fepic&now=1690125004160&eventType=pageView', 'https://www.epicgames.com/id/api/analytics', 'https://www.epicgames.com/id/api/analytics', 'https://www.epicgames.com/id/api/authenticate', 'https://static-assets-prod.unrealengine.com/account-portal/static/epic-favicon-96x96.png', 'https://www.epicgames.com/id/api/analytics', 'https://www.epicgames.com/id/api/analytics', 'https://static-assets-prod.unrealengine.com/account-portal/static/static/js/49.b6156753.chunk.js', 'https://static-assets-prod.unrealengine.com/account-portal/static/static/js/17.3087abf1.chunk.js', 'https://talon-website-prod.ecosec.on.epicgames.com/talon_sdk.js', 'https://talon-service-prod.ecosec.on.epicgames.com/v1/init', 'https://js.hcaptcha.com/1/api.js?onload=hCaptchaLoaded&render=explicit', 'https://newassets.hcaptcha.com/captcha/v1/fd00b2a/static/hcaptcha.html#frame=challenge&id=09pcmwke9c9g&host=www.epicgames.com&sentry=true&reportapi=https%3A%2F%2Faccounts.hcaptcha.com&recaptchacompat=true&custom=false&hl=en&tplinks=on&sitekey=91e4137f-95af-4bc9-97af-cdcedce21c8c&theme=dark&size=invisible&challenge-container=h_captcha_challenge_login_prod&origin=https%3A%2F%2Fwww.epicgames.com', 'https://newassets.hcaptcha.com/captcha/v1/fd00b2a/static/hcaptcha.html#frame=checkbox&id=09pcmwke9c9g&host=www.epicgames.com&sentry=true&reportapi=https%3A%2F%2Faccounts.hcaptcha.com&recaptchacompat=true&custom=false&hl=en&tplinks=on&sitekey=91e4137f-95af-4bc9-97af-cdcedce21c8c&theme=dark&size=invisible&challenge-container=h_captcha_challenge_login_prod&origin=https%3A%2F%2Fwww.epicgames.com', 'https://talon-service-prod.ecosec.on.epicgames.com/v1/phaser/batch', 'https://talon-service-prod.ecosec.on.epicgames.com/v1/init/execute', 'https://talon-service-prod.ecosec.on.epicgames.com/v1/phaser/batch']}, 'device_pixel_ratio': 2, 'dark_mode': True, 'chrome': True, 'property_list': ['0', '1', 'window', 'self', 'document', 'name', 'location', 'customElements', 'history', 'navigation', 'locationbar', 'menubar', 'personalbar', 'scrollbars', 'statusbar', 'toolbar', 'status', 'closed', 'frames', 'length', 'top', 'opener', 'parent', 'frameElement', 'navigator', 'origin', 'external', 'screen', 'innerWidth', 'innerHeight', 'scrollX', 'pageXOffset', 'scrollY', 'pageYOffset', 'visualViewport', 'screenX', 'screenY', 'outerWidth', 'outerHeight', 'devicePixelRatio', 'clientInformation', 'screenLeft', 'screenTop', 'styleMedia', 'onsearch', 'isSecureContext', 'trustedTypes', 'performance', 'onappinstalled', 'onbeforeinstallprompt', 'crypto', 'indexedDB', 'sessionStorage', 'localStorage', 'onbeforexrselect', 'onabort', 'onbeforeinput', 'onblur', 'oncancel', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'onclose', 'oncontextlost', 'oncontextmenu', 'oncontextrestored', 'oncuechange', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'onformdata', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange', 'onreset', 'onresize', 'onscroll', 'onsecuritypolicyviolation', 'onseeked', 'onseeking', 'onselect', 'onslotchange', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate', 'ontoggle', 'onvolumechange', 'onwaiting', 'onwebkitanimationend', 'onwebkitanimationiteration', 'onwebkitanimationstart', 'onwebkittransitionend', 'onwheel', 'onauxclick', 'ongotpointercapture', 'onlostpointercapture', 'onpointerdown', 'onpointermove', 'onpointerrawupdate', 'onpointerup', 'onpointercancel', 'onpointerover', 'onpointerout', 'onpointerenter', 'onpointerleave', 'onselectstart', 'onselectionchange', 'onanimationend', 'onanimationiteration', 'onanimationstart', 'ontransitionrun', 'ontransitionstart', 'ontransitionend', 'ontransitioncancel', 'onafterprint', 'onbeforeprint', 'onbeforeunload', 'onhashchange', 'onlanguagechange', 'onmessage', 'onmessageerror', 'onoffline', 'ononline', 'onpagehide', 'onpageshow', 'onpopstate', 'onrejectionhandled', 'onstorage', 'onunhandledrejection', 'onunload', 'crossOriginIsolated', 'scheduler', 'alert', 'atob', 'blur', 'btoa', 'cancelAnimationFrame', 'cancelIdleCallback', 'captureEvents', 'clearInterval', 'clearTimeout', 'close', 'confirm', 'createImageBitmap', 'fetch', 'find', 'focus', 'getComputedStyle', 'getSelection', 'matchMedia', 'moveBy', 'moveTo', 'open', 'postMessage', 'print', 'prompt', 'queueMicrotask', 'releaseEvents', 'reportError', 'requestAnimationFrame', 'requestIdleCallback', 'resizeBy', 'resizeTo', 'scroll', 'scrollBy', 'scrollTo', 'setInterval', 'setTimeout', 'stop', 'structuredClone', 'webkitCancelAnimationFrame', 'webkitRequestAnimationFrame', 'chrome', 'credentialless', 'caches', 'cookieStore', 'ondevicemotion', 'ondeviceorientation', 'ondeviceorientationabsolute', 'launchQueue', 'onbeforematch', 'getScreenDetails', 'queryLocalFonts', 'showDirectoryPicker', 'showOpenFilePicker', 'showSaveFilePicker', 'originAgentCluster', 'speechSynthesis', 'oncontentvisibilityautostatechange', 'openDatabase', 'webkitRequestFileSystem', 'webkitResolveLocalFileSystemURL', 'define', 'ethereum', 'AppInit', '_epicEnableCookieGuard', '__tracking_base', 'webpackJsonpaccountportal-node-website', 'regeneratorRuntime', '2f1acc6c3a606b082e5eef5e54414ffb', '__SENTRY__', '__axiosInstance', '__core-js_shared__', 'core', '__axiosInstanceCached', 'IMask', '__store', 'setImmediate', 'clearImmediate', '_epicTrackingCookieDomainId', '_epicTrackingCountryCode', '_epicTracking', 'recaptchaOptions', 'a0_0x998b', 'a0_0x7883', 'IntlPolyfill', 'talon', 'hCaptchaLoaded', 'hCaptchaReady', 'Raven', 'hcaptcha', 'grecaptcha', 'k', 'i', 'TEMPORARY', 'PERSISTENT', 'addEventListener', 'dispatchEvent', 'removeEventListener']}, 'date': {'timezone_offset': -120, 'format': {'calendar': 'gregory', 'day': '2-digit', 'locale': 'en-GB', 'month': '2-digit', 'numbering_system': 'latn', 'time_zone': 'Europe/Warsaw', 'year': 'numeric'}}, 'runtime': {'sd_recurse': False}, 'fpjs': {'version': '3.3.6', 'visitor_id': '519462c2c0684ff2093f7114324f8499', 'confidence': 0.5, 'hashes': {'fonts': '1b84ad4b7c13144aedd005c370f67b06', 'plugins': '7bf9267ddde7a33539244ab8ffe927d5', 'audio': 'b72cb0f5e109fe4d17fbaba30ad9ddcb', 'canvas': '42b2191d0bf12fe43832ba4802a313d0', 'screen': 'be6de320c4566fe1e0ca2cf4021d3c36'}}, 'motion': {'mousemove': [{'t': 2518.600000023842, 'x': 859, 'y': 309}, {'t': 2562.900000035763, 'x': 854, 'y': 310}, {'t': 2586.900000035763, 'x': 855, 'y': 310}, {'t': 2672.100000023842, 'x': 855, 'y': 310}, {'t': 2744, 'x': 856, 'y': 310}, {'t': 2768.2000000476837, 'x': 859, 'y': 309}, {'t': 6653.400000035763, 'x': 702, 'y': 508}, {'t': 6703.700000047684, 'x': 688, 'y': 516}, {'t': 6726.800000011921, 'x': 703, 'y': 517}, {'t': 9559.800000011921, 'x': 701, 'y': 445}, {'t': 9610.800000011921, 'x': 548, 'y': 410}, {'t': 9660.800000011921, 'x': 425, 'y': 384}, {'t': 9710.800000011921, 'x': 337, 'y': 357}, {'t': 9760.800000011921, 'x': 291, 'y': 333}, {'t': 9809.800000011921, 'x': 284, 'y': 327}, {'t': 9858.900000035763, 'x': 282, 'y': 324}, {'t': 9912.900000035763, 'x': 281, 'y': 324}, {'t': 9962.800000011921, 'x': 286, 'y': 328}, {'t': 9987.800000011921, 'x': 306, 'y': 342}, {'t': 10102.300000011921, 'x': 497, 'y': 404}, {'t': 10152.800000011921, 'x': 622, 'y': 434}, {'t': 10184.800000011921, 'x': 702, 'y': 451}, {'t': 11051.100000023842, 'x': 703, 'y': 484}, {'t': 11101.800000011921, 'x': 576, 'y': 409}, {'t': 11151.800000011921, 'x': 462, 'y': 343}, {'t': 11197.900000035763, 'x': 435, 'y': 326}, {'t': 11203.5, 'x': 435, 'y': 326}, {'t': 11301.800000011921, 'x': 434, 'y': 326}, {'t': 11314.100000023842, 'x': 434, 'y': 326}, {'t': 14810.900000035763, 'x': 434, 'y': 326}, {'t': 14861.900000035763, 'x': 432, 'y': 360}, {'t': 14911.800000011921, 'x': 417, 'y': 365}, {'t': 14921.800000011921, 'x': 415, 'y': 365}, {'t': 15022.100000023842, 'x': 415, 'y': 365}, {'t': 15075.800000011921, 'x': 415, 'y': 366}, {'t': 15125.900000035763, 'x': 413, 'y': 383}, {'t': 15148.900000035763, 'x': 413, 'y': 386}, {'t': 15309, 'x': 413, 'y': 386}, {'t': 15352.900000035763, 'x': 413, 'y': 388}, {'t': 15535.800000011921, 'x': 413, 'y': 389}, {'t': 15586.800000011921, 'x': 401, 'y': 410}, {'t': 15633.800000011921, 'x': 405, 'y': 459}, {'t': 15686.800000011921, 'x': 409, 'y': 505}, {'t': 15735.800000011921, 'x': 413, 'y': 531}, {'t': 15787.200000047684, 'x': 414, 'y': 541}, {'t': 15834.900000035763, 'x': 415, 'y': 546}, {'t': 16110.800000011921, 'x': 607, 'y': 559}, {'t': 16162.800000011921, 'x': 703, 'y': 556}, {'t': 16298.800000011921, 'x': 703, 'y': 540}, {'t': 16349.800000011921, 'x': 653, 'y': 540}, {'t': 16398.900000035763, 'x': 640, 'y': 546}, {'t': 16449.80000001192, 'x': 681, 'y': 544}, {'t': 16469.80000001192, 'x': 703, 'y': 539}], 'mousedown': [{'t': 9810.800000011921, 'x': 284, 'y': 327}, {'t': 11183.800000011921, 'x': 439, 'y': 328}, {'t': 15106.900000035763, 'x': 414, 'y': 375}, {'t': 15863.100000023842, 'x': 415, 'y': 546}], 'mouseup': [{'t': 9888.900000035763, 'x': 282, 'y': 324}, {'t': 11252.300000011921, 'x': 435, 'y': 326}, {'t': 15194.200000047684, 'x': 413, 'y': 386}, {'t': 15943.100000023842, 'x': 415, 'y': 546}], 'wheel': [], 'touchstart': [], 'touchend': [], 'touchmove': [], 'scroll': [], 'keydown': [{'t': 11310.900000035763}, {'t': 11342.400000035763}, {'t': 11362.5}, {'t': 11477}, {'t': 11485.700000047684}, {'t': 11485.700000047684}, {'t': 11674.700000047684}, {'t': 11694.700000047684}, {'t': 11898.900000035763}, {'t': 11902.200000047684}, {'t': 12009.5}, {'t': 12094.800000011921}, {'t': 12516}, {'t': 12621.5}, {'t': 12727.900000035763}, {'t': 12940.900000035763}, {'t': 13016.100000023842}, {'t': 13130.400000035763}, {'t': 13734.100000023842}, {'t': 13924}, {'t': 14074.400000035763}, {'t': 14196.100000023842}, {'t': 14268.100000023842}, {'t': 14395.300000011921}, {'t': 15354.200000047684}, {'t': 15398.700000047684}, {'t': 15406.400000035763}, {'t': 15540.200000047684}, {'t': 15552.400000035763}, {'t': 15568.300000011921}, {'t': 15709.200000047684}, {'t': 15712.900000035763}, {'t': 15721.800000011921}], 'keyup': [{'t': 11399.100000023842}, {'t': 11402.300000011921}, {'t': 11406.600000023842}, {'t': 11552.400000035763}, {'t': 11556.100000023842}, {'t': 11565.100000023842}, {'t': 11755.100000023842}, {'t': 11758.600000023842}, {'t': 11946.700000047684}, {'t': 11950.800000011921}, {'t': 12042.400000035763}, {'t': 12167.300000011921}, {'t': 12548.300000011921}, {'t': 12678.300000011921}, {'t': 12800.5}, {'t': 12997.300000011921}, {'t': 13080.600000023842}, {'t': 13174.300000011921}, {'t': 13782.300000011921}, {'t': 13984.5}, {'t': 14131}, {'t': 14247.600000023842}, {'t': 14312.700000047684}, {'t': 14464.400000035763}, {'t': 15454.900000035763}, {'t': 15458.700000047684}, {'t': 15462.900000035763}, {'t': 15612.200000047684}, {'t': 15624.400000035763}, {'t': 15624.700000047684}, {'t': 15761.200000047684}, {'t': 15773.200000047684}, {'t': 15785.400000035763}], 'resize': [{'t': 3090.600000023842, 'w': 1512, 'h': 982}, {'t': 3136.100000023842, 'w': 1512, 'h': 982}, {'t': 3156.300000011921, 'w': 1512, 'h': 982}, {'t': 3167.800000011921, 'w': 1512, 'h': 982}, {'t': 3178.300000011921, 'w': 1512, 'h': 982}, {'t': 3187, 'w': 1512, 'h': 982}, {'t': 3194.600000023842, 'w': 1512, 'h': 982}, {'t': 3204.600000023842, 'w': 1512, 'h': 982}, {'t': 3281, 'w': 1512, 'h': 982}, {'t': 3291.800000011921, 'w': 1512, 'h': 982}, {'t': 3303.800000011921, 'w': 1512, 'h': 982}, {'t': 3336.2000000476837, 'w': 1512, 'h': 982}], 'paste': []}, 'solve_token': True}
raw_data = json.dumps(serialized_data)  # conversion into raw string (pass separators=(',', ':') into json.dumps function, in case you want to obtain original xal token)
built_xal = encode_data(raw_data)
print(built_xal)
