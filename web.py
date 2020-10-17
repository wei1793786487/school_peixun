from flask import Flask
app = Flask(__name__)
from flask import request
import main
import re



@app.route('/<type>')
def login(type):
    if (type != 1 and type != 0):
        return "请输入正确的参数"
    else:
        phone = request.args.get('phone')
        reg = "1[3|4|5|7|8][0-9]{9}"
        find = re.findall(reg, phone)
        if(len(find)==0):
            return "请输入正确格式手机号"
        a_ction = main.doACtion(phone, type)
        return a_ction


