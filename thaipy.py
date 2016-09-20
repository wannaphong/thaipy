#!/usr/bin/python3
# -*- coding: utf-8 -*-
#   Apache License Version 2.0
# เขียนโดย วรรณพงษ์  ภัททิยไพบูลย์
import re
import runpy
import sys
import os
import io
class ThpyPlugin(object):
    """
    basic plugin class
    """
    pass

def multiple_replace(dict, text):
	# Create a regular expression  from the dictionary keys
	regex = re.compile('((^["]*$)%s(^["]*$))' % "|".join(map(re.escape, dict.keys())))
	#print(regex)
	# For each match, look-up corresponding value in dictionary
	return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

# Simplized thai keywords
class th_keyword(ThpyPlugin):
    """
    python th keyword
    """
    title = "คำสำคัญ"
    description = "Python คีย์เวิดร์"
    keyword = {
          # logic
          u"และ":"and",
          u"หรือ":"or",
          u"จริง": "True",
          u"เท็จ":"False",
          u"คือ":"is",
          u"เป็น":"is",
          u"ไม่":"not",
          u"ไม่เป็น":"is not",
          # def
          u"ฟังก์ชัน":"def",
          u"ชั้น":"class",
          u"คลาส":"class",
          # import
          u"จาก":"from",
          u"เรียก":"import",
          # flow
          u"คืนค่า":"return",
          u"ว่าง":"pass",
          # control
          u"หาก":"if",
          u"หากว่า":"elif",
          u"อื่น":"else",
          # for loop
          u"สำหรับ":"for",
          u"ใน":"in",
          # while loop
          u"ขณะ":"while",
          u"แสดง":"print",}


class th_buildin_method(ThpyPlugin):
    """
    python th methods
    """
    title = "methods"
    description = "Python methods"
    keyword = {
          u"นี่":"this",
          u"กรอก":"input",
          u"รับ":"input",
          # build-in types
          u"ข้อความ":"str",
          u"รายการ": "list",
          # number methods
          u"ตัวเลข":"int",
          u"จำนวนจริง":"float",
          # build in functions
          u"ความยาว":"len",
          u"ช่วง":"range",
          u"ชนิด":"type",
          u"ช่วย":"help",
          u"เอกสาร":"help",
          }

keyword = th_keyword()
method = th_buildin_method()

trans = dict(keyword.keyword, **method.keyword) # ตัวแปรสำหรับรวมคำสั่ง
translations = trans
def commandline():
    """thaipy, the python language in Traditional Thai

    usage: thaipy file.thpy
    """
    if len(sys.argv) != 2:
        print(commandline.__doc__)
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("thaipy: file '%s' does not exists" % file_path) # ไม่พบไฟล์ แจ้งเตือน
        sys.exit(1)
    sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path)) # ดึงที่ตั้งของไฟล์
    file=io.StringIO(open(file_path,'r',encoding='utf-8').read()) # โหลดไฟล์เข้าหน่วยความจำ
    file2=multiple_replace(translations,file.read()) # แทนที่คำสั่ง
    file.close() # ปิดเพื่อคืนความจำ
    file=io.StringIO(file2) # โหลดเข้าใหม่
    del file2
    runpy._run_module_code(file.read(), mod_name="__main__") # รันโค้ด

if __name__=="__main__":
    commandline()
