# -*- coding:utf-8 -*-

class URL(object):

    # 天元数学登录的url
    TYSX_LOGIN="http://yfqt.wdtysx.com/app/jsp/dlzc/login.html"
    # 天元数学作业管理的url
    TYSX_WORK="http://yfqt.wdtysx.com/app/jsp/zy/zygl.html?pagetype=zygl"

def switch_window_to(driver, target_page_title):
        for window1 in driver.window_handles:
            driver.switch_to.window(window1)
            print(driver.title)
            if driver.title == target_page_title:
             break
