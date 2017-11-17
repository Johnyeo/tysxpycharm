# -*- coding:utf-8 -*-
import time
import subprocess

import helper
# 参数化休眠时间调整
a = 2
b = 4
def BendFileWork(self):
    upload_url = helper.UPLOAD_EXE_DIR

    # 上传本地文件(正确文件Excel)

    self.brower.FindId("fileUpload_upload").click()
    time.sleep(a)
    print(upload_url + 'uploadExcel.exe')
    subprocess.Popen(upload_url + 'uploadExcel.exe')
    time.sleep(a)
    time.sleep(b)
    # 点击删除文件按钮
    self.brower.FindClass("wj-del").click()
    time.sleep(b)
    # 弹框 提示--是否确认删除文件
    # 点击确定删除
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(a)
    time.sleep(b)

    # 上传本地文件(正确文件Word)
    self.brower.FindId("fileUpload_upload").click()
    time.sleep(a)
    subprocess.Popen(upload_url + 'uploadWord.exe')
    time.sleep(a)
    time.sleep(b)
    # 删除文件
    # 点击删除文件按钮
    self.brower.FindClass("wj-del").click()
    time.sleep(a)
    # 弹框 提示--是否确认删除文件
    # 取消删除
    self.brower.FindId("prompt-wd_prompt_close-cancle-confirm").click()
    time.sleep(b)

    # 上传本地文件（空文件）
    self.brower.FindId("fileUpload_upload").click()
    time.sleep(a)
    subprocess.Popen(upload_url + 'uploadEmptyWord.exe')
    time.sleep(b)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-error").text, u"不能上传空文件")
    time.sleep(a)
    # 关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-error").click()
    time.sleep(a)

    # 上传本地文件(错误文件 txt文本)
    self.brower.FindId("fileUpload_upload").click()
    time.sleep(a)
    subprocess.Popen(upload_url + 'uploadTXT.exe')
    time.sleep(b)

    self.assertEqual(self.brower.FindClasses("wd-prompt-textarea-text")[0].text,
                     u"格式仅支持*.mp4;*.avi;*.flv;*.f4v;*.rmvb;*.wmv;*.3gp;*.m4v;*.Mov;*.asf;*.jpg;*.jpeg;*.png;*.wav;*.mp3;*.wma;*.ogg;*.aac*;*.amr;*.m4a;*.spx;*.caf;*.ppt;*.pptx;*.doc;*.docx;*.xls;*.xlsx;*.pdf")
    time.sleep(b)
    # 关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-error").click()
    time.sleep(a)


# 上传多媒体文件
def DMTFileWork(self):
    # 添加多媒体空间文件
    self.brower.FindClasses("btn-icon-tjwj")[1].click()
    # 休眠
    time.sleep(b)

    # 输入内容 点击搜索
    self.brower.FindId("searchwjmc").send_keys("h")
    self.brower.FindClass("search_btn").click()
    time.sleep(a)
    # 点击全选按钮
    self.brower.FindId("wd_checkBox_wdcheckall").click()
    time.sleep(a)

    # 取消全选
    self.brower.FindId("wd_checkBox_wdcheckall").click()
    time.sleep(a)
    # 点击文件勾选框
    self.brower.FindId("wd_checkBox_a1").click()
    time.sleep(a)
    # 点击确定 成功添加上传文件
    self.brower.FindNmae("prompt_dmtkjxz").click()
    time.sleep(a)
    self.assertEqual(self.brower.driver.title, u"发作业-文件作业")
    time.sleep(b)
    # 再次点击添加多媒体文件
    self.brower.FindClasses("btn-icon-tjwj")[1].click()
    time.sleep(a)
    # 点击文件夹
    self.brower.FindClass("text-left").click()
    time.sleep(a)
    # 点击排序
    self.brower.FindClass("pxlxlist").click()
    time.sleep(a)
    self.brower.FindXpath("//*[@id='spsc-dmtkj-box']/div[1]/select/option[a]").click()
    time.sleep(a)
    # 点击文件勾选框
    self.brower.FindId("wd_checkBox_a1").click()
    time.sleep(a)
    # 点击确定 成功添加上传文件
    self.brower.FindNmae("prompt_dmtkjxz").click()
    time.sleep(b)

    # 点击添加多媒体文件
    self.brower.FindClasses("btn-icon-tjwj")[1].click()
    time.sleep(a)
    # 点击文件夹
    self.brower.FindClass("text-left").click()
    time.sleep(a)
    # 点击上一级文件目录
    self.brower.FindId("showCatList").click()
    time.sleep(a)
    # 点击文件夹
    self.brower.FindClass("re_name").click()
    time.sleep(a)
    # 勾选全部文件
    self.brower.FindId("wd_checkBox_wdcheckall").click()
    time.sleep(a)
    # 点击确定 成功上传文件
    self.brower.FindNmae("prompt_dmtkjxz").click()
    time.sleep(b)
