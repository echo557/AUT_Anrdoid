# import os
# import sys
#
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(os.path.split(curPath)[0])[0]
#
# from TestResource.GWMV2.GWMV2Res import *
#
# print(App_List_Home_Btn)
import time
import uiautomator2 as u2
import re




d=u2.connect("CJUD4R68605940")
output, exit_code = d.shell(["dumpsys","wifi|more"])

# print(type(output))
# str1 = "Wi-Fi is enabled"
# str2 = "mEnableTrafficStatsPoll true"
# if u"华为p20" and str1 and str2 in output:
#     print("WIFI is connected")
# else:
#     print("WIFI is not connected, please connect WIFI to retry")
print(output,exit_code)



#
# d.press("home")
# d.xpath('//*[@resource-id="com.harman.gwm.hmi.launcher:id/iv_arrow"]').click()

# time.sleep(2)
# d.swipe_ext("right")
# d.long_click(0.5,0.5)
# d.swipe()
# d.click(0.5,0.6)
# d.swipe(0.9, 0.1, 0.1,0.1)
# time.sleep(2)
# d.swipe(0.1, 0.1, 0.9,0.1)
# time.sleep(2)
#


# d.swipe_ext("right")