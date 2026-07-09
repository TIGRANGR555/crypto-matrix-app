[app]
title = CryptoMatrix
package.name = cryptomatrix
package.domain = org.tigrangr
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

[target]
# Targets specifically configured for modern Ubuntu cloud runners
android.api = 34
android.minapi = 24
android.ndk = 26b
android.ndk_api = 24
android.allow_gpl = True
