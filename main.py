from pyaxmlparser import APK

apk = APK('USBDebug 1.0_1.apk')
print(apk.package)
print(apk.version_name)
print(apk.version_code)
print(apk.icon_info)
print(apk.icon_data)
print(apk.application)