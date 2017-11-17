# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Chrome(object):
    # 打开谷歌浏览器
    def StartChrom(self,url):
        self.driver=webdriver.Chrome()
        # 设置窗口最大化
        self.driver.maximize_window()
        # 打开网址
        self.driver.get(url)
        # 设置休眠时间
        time.sleep(2)
        pass
    # 关闭谷歌浏览器
    def CloseChrom(self):
        self.driver.quit()
        pass


        # 查找控件

        # 通过ID查找
    def FindId(self, ID):
        # 使用 try

        try:

            # 通过by去查找id
            ids = (By.ID, ID)
            # 使用显示等待去等待
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ids))
            # 开始查找控件
            return self.driver.find_element_by_id(ID)

        except Exception:

            # 自动化测试会自动捕捉该异常
            pass
    # 通过name查找
    def FindNmae(self,name):

        try:
            # 通过by去查找name
            names=(By.NAME,name)
            # 使用显示等待去等待
            WebDriverWait(self.driver,20,0,5).until(EC.presence_of_element_located(names))
            # 开始查找控件
            return self.driver.find_element_by_name(name)
        except Exception:
            # 自动化测试会自动捕捉该异常

         pass
     # 通过class_name查找

    def FindClass(self, class_name):

        try:
                # 通过by去查找class
                class_names = (By.CLASS_NAME, class_name)
                # 使用显示等待去等待
                WebDriverWait(self.driver, 20, 0, 5).until(EC.presence_of_element_located(class_names))
                # 开始查找控件
                return self.driver.find_element_by_class_name(class_name)

        except Exception:
                # 自动化测试会自动捕捉该异常

                pass
    # 通过class_name查找

    def FindClasses(self, class_name):

            try:
                # 通过by去查找class
                class_names = (By.CLASS_NAME, class_name)
                # 使用显示等待去等待
                WebDriverWait(self.driver, 20, 0, 5).until(EC.presence_of_element_located(class_names))
                # 开始查找控件
                return self.driver.find_elements_by_class_name(class_name)

            except Exception:
                # 自动化测试会自动捕捉该异常

                pass
    # 通过tag_name查找

    def FindTag(self, tag_name):

        try:
                # 通过by去查找tag
                tag_names = (By.TAG_NAME, tag_name)
                # 使用显示等待去等待
                WebDriverWait(self.driver, 20, 0, 5).until(EC.presence_of_element_located(tag_names))
                # 开始查找控件
                return self.driver.find_element_by_tag_name(tag_name)
        except Exception:
                # 自动化测试会自动捕捉该异常

                pass

    # 通过css查找

    def FindCss(self, css):

        try:
                # 通过by去查找css
                csses = (By.CSS_SELECTOR, css)
                # 使用显示等待去等待
                WebDriverWait(self.driver, 20, 0, 5).until(EC.presence_of_element_located(csses))
                # 开始查找控件
                return self.driver.find_element_by_css_selector(css)
        except Exception:
                # 自动化测试会自动捕捉该异常

                pass

    # 通过link_text查找

    def FindLink_text(self, link):

        try:
                # 通过by去查找link_text
                link_text = (By.LINK_TEXT, link)
                # 使用显示等待去等待
                WebDriverWait(self.driver, 20, 0, 5).until(EC.presence_of_element_located(link_text))
                # 开始查找控件
                return self.driver.find_element_by_link_text(link)
        except Exception:
                # 自动化测试会自动捕捉该异常

                pass

    # 通过par_link_text查找

    def FindParttalLink(self, par_link):
            try:

                par_link_text = (By.PARTIAL_LINK_TEXT, par_link)
                WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(par_link_text))
                return self.driver.find_element_by_partial_link_text(par_link)
            except Exception:
                # 自动化测试会自动捕捉该异常

                pass

    # 通过xpath查找

    def FindXpath(self, xpath):

        try:
                # 通过by去查找xpath
                Xpath = (By.XPATH, xpath)
                # 使用显示等待去等待
                WebDriverWait(self.driver, 20, 0, 5).until(EC.presence_of_element_located(Xpath))
                # 开始查找控件
                return self.driver.find_element_by_xpath(xpath)
        except Exception:
                # 自动化测试会自动捕捉该异常

                pass
