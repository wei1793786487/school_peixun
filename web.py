from flask import Flask
app = Flask(__name__)
from flask import request
import main

@app.route('/<type>')
def login(type):
    if(type!=1 and type!=0):
        return "请输入正确的参数"
    else:
        phone = request.form["python"]
        a_ction = main.doACtion(phone, type)
        return a_ction


