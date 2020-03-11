from flask import Flask, jsonify, request, abort
import json
import redis
import requests
import uuid

app = Flask(__name__)
#  连接redis返回redis操作对象
redis_client = redis.StrictRedis(host='127.0.0.1')


@app.route('/todo/api/v1.0/put', methods=['POST'])
def handle_put_redis():
    if request.get_data():
        json_data = json.loads(request.get_data().decode("utf-8"))
        print(json_data)
        if 'data' not in json_data:
            return jsonify({'status': 'fail', 'code': '2222', 'msg': '请输入参数 data'})
        if type(json_data['data']) != int:
            return jsonify({'status': 'fail', 'code': '1111', 'msg': '参数类型错误'})
        data = json_data['data']
        redis_client.set('data', data)  # 写入redis
        redis_client.expire('data', 1800)  # 设置'data'的过期时间为半个小时，防止处理函数忘记删除
        # notice_handle()  # 调用planB的时候请注释掉该函数
        return jsonify({'status': 'ok', 'code': '0000', 'msg': 'successd'})
    else:
        return jsonify({'status': 'fail', 'code': '2222', 'msg': 'please input param'})


def notice_handle():
    r = requests.post('http://127.0.0.1:5001/api/v1.0/oper')  # 通知另一个服务器处理
    print(r.content.decode('utf-8'))


if __name__ == '__main__':
    app.run(processes=True)
