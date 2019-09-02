import uiautomator2 as u2
import os
import sys
import logging
import time
from assertpy import assert_that

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(os.path.split(curPath)[0])[0]
sys.path.append(rootPath)

from TestResource.gwmv2_res import *



class gwmv2:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.connDev = None

    def connectToDevice(self):
        self.connDev = u2.connect(Device_Serial)
        logging.info(self.connDev)

    def shortTouch(self, btn):
        try:
            self.connDev.xpath(btn).click()
        except:
            logging.error(self.connDev.xpath(btn).click())
            assert (self.connDev.xpath(btn).click())

            # assert (self.connDev.xpath(btn).click())
            # assert_that(self.connDev.xpath(btn).click()).is_true()
            # logging.error("Button cannot be found:%s" %btn)
            # assert ("Button cannot be found:%s" %btn)
            # logging.error("Button cannot be found:%s" %btn)

    def startHomeApp(self):
        try:
            self.connDev.session(Home_Pkg)
        except:
            logging.error("Home App start failed")
            assert(self.connDev.session(Home_Pkg))


    def getDev(self):
        return self.connDev


    def swipeLeft(self):
        time.sleep(2)
        self.connDev.swipe(0.9, 0.1, 0.1,0.1)

    def swipeRight(self):
        time.sleep(2)
        self.connDev.swipe(0.1, 0.1, 0.9,0.1)

    def elemExistJudgement(self,elem):
        try:
            self.connDev.xpath(elem).exists
            logging.info("Element exist %s" %elem)
        except:
            logging.error("Elemnt cannot be found.")
            assert (self.connDev.xpath(elem))

    def compareImg(self,captured_img,verified_img):
        self.connDev.screenshot(captured_img)

    def enterAppListFromHome(self,elem):
        try:
            self.connDev.xpath(elem).click()
        except:
            logging.error("Elemnt cannot be found.")
            assert (self.connDev.xpath(elem))

    def statusOfWifiConnection(self):
        # try:
        #     output, exit_code = self.connDev.shell(["dumpsys","wifi|more"])
        #     status = "Wi-Fi is enabled"
        #     traffic_stats = "mEnableTrafficStatsPoll true"
        #     host_name = WIFI_Host
        #     if (host_name and traffic_stats and status) in output:
        #         # assert_that(output).contains_only(host_name,status,traffic_stats)
        #         logging.info("WIFI is connectd,%s" %status)
        # except:
        #     logging.error("WIFI is not connected,please connect WIFI first")
        #     raise ValueError("WIFI is not connected,please connect WIFI first")
        output, exit_code = self.connDev.shell(["dumpsys", "wifi|more"])
        str1 = "Wi-Fi is enabled"
        str2 = "mEnableTrafficStatsPoll true"
        if u"华为p20" and str1 and str2 in output:
            logging.info("WIFI is connectd,%s" %str1)
        else:
            raise ValueError("WIFI is not connected,please connect WIFI first")
    #
    # def enterAppFromAppList(self,app_name,btn):
    #     # self.connDev.xpath(Btn_App_Lists).click()
    #     # time.sleep(2)
    #     try:
    #         if self.connDev.xpath(app_name).exists:
    #             self.connDev.xpath(btn).click()
    #         else:
    #             for i in range(3):
    #                 time.sleep(2)
    #                 self.connDev.swipe(0.9, 0.1, 0.1, 0.1)
    #                 self.connDev.xpath(btn).click()
    #     except:
    #         logging.error("App cannot found")
    #









# if __name__=='__main__':
#     gwmv2.swipe(0.9,0.5,0.1,0.5)


# if __name__=="__main__":
#     test = GWMV2.ConnectToDevice()
