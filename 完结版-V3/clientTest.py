import requests
import json

url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks'
# 发送给服务器的参数
content = {'title':4}
r = requests.post(url=url, data=json.dumps(content))
print(r.status_code)
