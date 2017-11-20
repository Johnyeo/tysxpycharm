# coding:utf-8
import os

CURRENT_PATH = os.getcwd()
PROJECT_DIR = os.path.abspath(os.path.join(CURRENT_PATH, os.pardir))
UPLOAD_EXE_DIR = CURRENT_PATH+"\\"
UPLOAD_EXE_DIR2 = UPLOAD_EXE_DIR.replace('\\','/')
print(UPLOAD_EXE_DIR)
