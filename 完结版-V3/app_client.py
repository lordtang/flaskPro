import requests
import json
import uuid
import time
import binascii
import os

"""
function:向指定服务器发送post请求，服务器没无响应自动重发
parameter:
    url:请求路径 str
    request_data:请求参数 dict
    required:必传参数列表
    max_times：最大请求次数
    interval：每次请求的间隔
return:
    False:请求出错
    content:请求成功返回内容
usage:
    ret = send_request(url, data, required)
    if ret:
        print(ret)
"""


def send_request(url, request_data, required, max_times=5, interval=3):
    timer = 1  # 计数器
    while timer <= (max_times if max_times >= 0 else 0):
        try:
            if not all(k in request_data for k in required):  # 参数校验
                print('必传参数不完整')
                return False
            ret = requests.post(url=url, data=json.dumps(request_data), timeout=5)
            if not str(ret.status_code).startswith('2'):  # 不以2开头的都认为是错误的
                print('请求错误：{}'.format(ret.status_code))
                return False
            else:
                content = ret.content.decode('utf-8')
                return content
        except requests.exceptions.RequestException as e:
            interval = interval if interval >= 0 else 0
            print('连接失败,第{}次尝试连接,{}秒后重试'.format(timer, interval))
            time.sleep(interval)
            timer += 1
            if timer == max_times:  # 达到最大连接次数
                return False


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/todo/api/v1.0/noticeTasks'

    data = {
        'reqCode': str(uuid.uuid3(namespace=uuid.NAMESPACE_URL, name='iiot')),
        'reqTime': time.strftime("%Y%m%d%H%M%S", time.localtime()),
        'clientCode': str(uuid.uuid1()),
        'tokenCode': str(binascii.b2a_base64(os.urandom(24))[:-1]),
        'method': 'F01',
        'taskCode': '2019-4545-56',
        'wbCode': '125452'
    }

    # 必传参数名称列表
    required = ['reqCode', 'reqTime', 'clientCode', 'tokenCode', 'method', 'taskCode', 'wbCode']  # 需要填写的参数

    ret = send_request(url, data, required)
    if ret:
        print(ret)
