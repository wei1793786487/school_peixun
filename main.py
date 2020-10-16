import getUtlis
import logging
logging.basicConfig(level=logging.INFO)

# type 0 为签到 1为签退

def doACtion(phone,type):

    logging.info("手机号为:{}".format(phone))

    # 手机验证码
    code = getUtlis.getCode(phone)

    logging.info("触发手机短信")

    login_info = getUtlis.login(phone)

    login_data = login_info["data"]["user"]

    user_id = login_data["id"]

    logging.info("获取用户id:{}".format(user_id))

    # type_id  ??????
    type_id=login_data["typeId"]

    logging.info("获取用户typeId:{}".format(type_id) )

    info_list = getUtlis.getSignInfoList(user_id)

    class_id = info_list["data"]["curriculumList"][0]['id']
    name = info_list["data"]["curriculumList"][0]['name']

    logging.info("获取课程信息:{}，id为:{}：".format(name,class_id) )

    info = getUtlis.getUserInfo(user_id, class_id)

    curriculum_id=info['data']['curriculumDetailList'][0]["id"]
    time_ = info['data']['curriculumDetailList'][0]['shoukeTime']
    logging.info("最新一期时间:{}".format(time_))
    log_ = info['data']['curriculum']["log"]
    lat = info['data']['curriculum']["lat"]

    url=info["data"]["sfzhImgJust"]

    logging.info("curriculum_id为:{}，经纬度为:{},{}：".format(curriculum_id, log_,lat))

    sign_in = getUtlis.sign_in(curriculum_id, type_id,type,lat,log_,url)
    logging.info("返回信息:{}".format(sign_in["msg"]))
    return sign_in


