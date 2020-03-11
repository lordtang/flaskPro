import requests
import json

"""
服务器接收失败返回格式：
return jsonify({'status': 'fail', 'code': '2222', 'msg': '请输入参数 data'})

服务器接收成功返回格式：
return jsonify({'status': 'ok', 'code': '0000', 'msg': 'successd'})

status:状态，code:状态码，msg:原因
"""


url = 'http://127.0.0.1:5000/todo/api/v1.0/put'
data = {'data': 100}
content = requests.post(url, data=json.dumps(data)).content.decode('utf-8')
ret_data = json.loads(content)  # 获取发送时返回的数据
# 发送成功后服务器向客户端返回'0000'
if ret_data['code'] != '0000':  # 发送失败，code不等于0000，进行一次重发
    print('发送失败，{},正在重发'.format(ret_data['msg']))  # 发送失败，并显示服务器返回的原因
    ret_data = json.loads(requests.post(url, json.dumps(data)).content.decode('utf-8'))  # 获取重发时返回的的数据
    if ret_data['code'] != '0000':  # 判断重发是否成功
        print('重发失败,{}'.format(ret_data['msg']))  # 重发失败，并显示服务器返回的原因
    else:
        print('重发成功')
else:  # 发送成功。code等于0000
    print('发送成功', data['msg'])



