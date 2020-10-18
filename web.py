from flask import Flask
app = Flask(__name__)
from flask import request
import main
import re

@app.route('/<type>')
def login(type):

    if (type != "1" and type != "0"):
        return "请输入正确的参数"
    else:
        phone = request.args.get('phone')
        reg = "^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[0-35-9]\d{2}|4(?:0\d|1[0-2]|9\d))|9[0-35-9]\d{2}|6[2567]\d{2}|4(?:(?:10|4[01])\d{3}|[68]\d{4}|[579]\d{2}))\d{6}$"
        find = re.findall(reg, phone)
        if(len(find)==0):
            return "请输入正确格式手机号"
        a_ction = main.doACtion(phone, type)
        return a_ction


