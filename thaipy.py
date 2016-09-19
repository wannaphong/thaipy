#!/usr/bin/python3
# -*- coding: utf-8 -*-
class ThpyPlugin(object):
    """
    basic plugin class
    """
    pass


def revert_dict(lang_dict):
    """make a reverse dictionary from the input dictionary
    >>> revert_dict({'a':'1', 'b':'2'})
    {'1': 'a', '2': 'b'}
    """
    return dict ( (v,k) for k, v in lang_dict.items() )

# Simplized chinese keywords
class th_keyword(ThpyPlugin):
    """
    python cn keyword
    """
    title = "คำสำคัญ"
    description = "Python คีย์เวิดร์"
    keyword = {
          # logic
          u"และ":"and",
          u"หรือ":"or",
          u"จริง": "True",
          u"เท็จ":"False",
          u"ว่าง":"None",
          # def
          u"ฟังก์ชัน":"def",
          u"ฟังก์ชั่น":"def",
          u"ชั้น":"class",
          u"คลาส":"class",
          # import
          u"จาก":"from",
          u"เรียก":"import",
          u"เป็น":"as",
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
    python cn methods
    """
    title = "methods"
    description = "Python methods"
    keyword = {
          u"กรอก":"input",
          u"รบ":"input",
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
pattern = '[\u0E31|\u0E4A|\u0E35|\u0E33|\u0E49|\u0E48|\u0E37]' # ตัวแปรสำหรับไว้เก็บตัวกรอก ่ , ุ ออกจากไฟล์โค้ด
import tokenize,re
def translate_code(readline, translations):
	for type, name, _,_,_ in tokenize.generate_tokens(readline):
		#name=re.sub(regex,'',name)
		#print(name,type == tokenize.NAME)
		if type == tokenize.NAME and name in translations:
			#print("\ntype")
			#print(tokenize.NAME, translations[name])
			yield tokenize.NAME, translations[name]
		else:
			#print("else")
			#print(type, name)
			yield type, name
translations = trans
import runpy
import sys
import os
import tokenize 
import io
def commandline():
    """thaipy, the python language in Traditional Thai

    usage: thaipy file.twpy
    """
    if len(sys.argv) != 2:
        print(commandline.__doc__)
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("thaipy: file '%s' does not exists" % file_path)
        sys.exit(1)
    sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))
    file=io.StringIO(open(file_path,'r',encoding='utf-8').read())
    file2=re.sub(pattern,'',file.read())
    file.close()
    file=io.StringIO(file2)
    del file2
    openfile = list(translate_code(file.readline, translations))
    file.close()
    source = tokenize.untokenize(openfile)
    code = compile(source, file_path, "exec")

    runpy._run_module_code(code, mod_name="__main__")

if __name__=="__main__":
    commandline()
