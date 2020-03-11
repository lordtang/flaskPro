from flask import Flask, jsonify, request, abort
import json
from time import *
import datetime

app = Flask(__name__)


def rizhi(x):
    try:
        c = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        doc = open('C:/log/PCB板程序载入-1前.txt', 'a+')  # 打开文件
        print('Time:%s：%d ' % (c, x), file=doc)  # 输出
        doc.close()
    except:
        a = 1


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    # 获取传递来的json参数
    json_data = json.loads(request.get_data().decode("utf-8"))
    print(json_data)
    aa = 2
    print(aa)
    print(json_data['title'])
    print(aa + json_data['title'])
    rizhi(aa + json_data['title'])
    return jsonify(aa + json_data['title']), 201  # 并且返回这个添加的task内容和状态码。


# 任务执行通知
@app.route('/todo/api/v1.0/noticeTasks', methods=['post'])
def cancel_task():
    # 判断参数是否存在
    if not request.get_data():
        return jsonify({'code': '1', 'massage': '请输入参数', 'reqCode': '', 'data': ''})
    # 获取请求参数
    request_data = json.loads(request.get_data().decode("utf-8"))
    # 判断参数完整性
    required = ['reqCode', 'reqTime', 'clientCode', 'tokenCode', 'method', 'taskCode', 'wbCode']  # 需要填写的参数
    if not all(k in request_data for k in required):
        return jsonify({'code': '2', 'massage': '必传参数缺失',
                        'reqCode': request_data['reqCode'] if 'reqCode' in request_data else '', 'data': ''})
    # 参数完整 任务执行通知，doSomething...

    return jsonify({'code': '0', 'massage': '成功', 'reqCode': request_data['reqCode'], 'data': ''})


if __name__ == '__main__':
    app.run(debug=True)
