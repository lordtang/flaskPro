# 方案A：使用redis作为缓存数据库，planA.py中调用接口在函数中查看是否存在该数，并运算，运算后将结果存入redis中。还可以继续调用其他接口对运算结果进行再运算
# 优点：包含通知机制，运算的状态可追踪，不运算的时候不会被调用，性能较好，比较推荐

import redis
from flask import Flask, jsonify, request, abort
import requests

# 连接redis
redis_client = redis.StrictRedis('127.0.0.1')

app = Flask(__name__)


# 运算app_service.py中存入redis中的值
@app.route('/api/v1.0/oper', methods=['POST'])
def oper():
    if redis_client.exists('data'):
        data = redis_client.get('data').decode('utf-8')
        result = int(data) + 13  # 运算
        redis_client.delete('data')  # 删除redis中运算完的值
        redis_client.set('oper2', result)  # 保存运算结果，方便后面运算
        print('oper函数运算完成！')
        requests.post('http://127.0.0.1:5001/api/v1.0/oper2') # 通知oper2函数进行运算
        return jsonify({'code': '0000', 'msg': 'successful'})
    else:
        return jsonify({'code': '1111', 'msg': 'fail'})


@app.route('/api/v1.0/oper2', methods=['POST'])
def oper2():
    if redis_client.exists('oper2'):  # 检查该键是否存在
        data = redis_client.get('oper2').decode('utf-8')
        result = int(data) + 14  # 运算
        redis_client.delete('oper2')  # 删除运算完的数
        redis_client.set('oper3', result)  # 保存运算结果
        print('oper2 运算完成！！')
        # requests.post('..............')通知其他函数进行运算
        return jsonify({'code': '0000', 'msg': 'successful'})
    else:
        return jsonify({'code': '1111', 'msg': 'fail'})


if __name__ == '__main__':
    app.run('127.0.0.1', 5001, True)  # 绑定和app_service.py中的flask不同的端口即可
