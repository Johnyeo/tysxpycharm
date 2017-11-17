# -*- coding:utf-8 -*-
import time
import subprocess
def BendFileWork(self):
    #上传本地文件(正确文件)

    self.brower.FindId("fileUpload_upload").click()
    time.sleep(3)
    subprocess.Popen('C:\Users\Administrator\Desktop\upload.exe')
    time.sleep(3)
    # 点击删除文件按钮
    self.brower.FindClass("wj-del").click()
    time.sleep(3)
    # 弹框 提示--是否确认删除文件
    # 点击确定删除
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(8)

    self.brower.FindId("fileUpload_upload").click()
    time.sleep(3)
    subprocess.Popen('C:\Users\Administrator\Desktop\uploadexcept.exe')
    time.sleep(5)
    # 删除文件
    # 点击删除文件按钮
    self.brower.FindClass("wj-del").click()
    time.sleep(3)
    # 弹框 提示--是否确认删除文件
    # 取消删除
    self.brower.FindId("prompt-wd_prompt_close-cancle-confirm").click()
    time.sleep(5)

    # 上传本地文件（空文件）
    self.brower.FindId("fileUpload_upload").click()
    time.sleep(3)
    subprocess.Popen('C:\Users\Administrator\Desktop\uploadhaha.exe')
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-error").text, u"不能上传空文件")
    time.sleep(3)
    # 关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-error").click()
    time.sleep(3)

    # 上传本地文件(错误文件 txt文本)
    self.brower.FindId("fileUpload_upload").click()
    time.sleep(3)
    subprocess.Popen('C:\Users\Administrator\Desktop\uploadnews.exe')

    time.sleep(5)

    self.assertEqual(self.brower.FindClasses("wd-prompt-textarea-text")[0].text,
                     u"格式仅支持*.mp4;*.avi;*.flv;*.f4v;*.rmvb;*.wmv;*.3gp;*.m4v;*.Mov;*.asf;*.jpg;*.jpeg;*.png;*.wav;*.mp3;*.wma;*.ogg;*.aac*;*.amr;*.m4a;*.spx;*.caf;*.ppt;*.pptx;*.doc;*.docx;*.xls;*.xlsx;*.pdf")
    time.sleep(5)
    # 关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-error").click()
    time.sleep(3)

# 上传多媒体文件
def DMTFileWork(self):
    # 添加多媒体空间文件
    self.brower.FindClasses("btn-icon-tjwj")[1].click()
    # 休眠
    time.sleep(5)

    # 输入内容 点击搜索
    self.brower.FindId("searchwjmc").send_keys("h")
    self.brower.FindClass("search_btn").click()
    time.sleep(3)
    # 点击全选按钮
    self.brower.FindId("wd_checkBox_wdcheckall").click()
    time.sleep(3)

    # 取消全选
    self.brower.FindId("wd_checkBox_wdcheckall").click()
    time.sleep(3)
    # 点击文件勾选框
    self.brower.FindId("wd_checkBox_a1").click()
    time.sleep(3)
    # 点击确定 成功添加上传文件
    self.brower.FindNmae("prompt_dmtkjxz").click()
    time.sleep(3)
    self.assertEqual(self.brower.driver.title, u"发作业-文件作业")
    time.sleep(5)
    # 再次点击添加多媒体文件
    self.brower.FindClasses("btn-icon-tjwj")[1].click()
    time.sleep(3)
    # 点击文件夹
    self.brower.FindClass("text-left").click()
    time.sleep(3)
    # 点击排序
    self.brower.FindClass("pxlxlist").click()
    time.sleep(3)
    self.brower.FindXpath("//*[@id='spsc-dmtkj-box']/div[1]/select/option[3]").click()
    time.sleep(3)
    # 点击文件勾选框
    self.brower.FindId("wd_checkBox_a1").click()
    time.sleep(3)
    # 点击确定 成功添加上传文件
    self.brower.FindNmae("prompt_dmtkjxz").click()
    time.sleep(5)

    # 点击添加多媒体文件
    self.brower.FindClasses("btn-icon-tjwj")[1].click()
    time.sleep(3)
    # 点击文件夹
    self.brower.FindClass("text-left").click()
    time.sleep(3)
    # 点击上一级文件目录
    self.brower.FindId("showCatList").click()
    time.sleep(3)
    # 点击文件夹
    self.brower.FindClass("re_name").click()
    time.sleep(3)
    # 勾选全部文件
    self.brower.FindId("wd_checkBox_wdcheckall").click()
    time.sleep(3)
    # 点击确定 成功上传文件
    self.brower.FindNmae("prompt_dmtkjxz").click()
    time.sleep(5)