
'''from suds.client import Client

url = 'http://115.236.50.12:80/rcs/services/rest/hikRpcService'
client = Client(url)
print(client)'''

import requests,json
 
url_json = 'http://115.236.50.12:808/rcs/services/rest/hikRpcService/genAgvSchedulingTask'
data_json = json.dumps({'reqCode':'111112312','taskTyp':'move','userCallCode':'BB','userCallCodePath':['BB'],'podCode':'555555'})   #dumps：将python对象解码为json数据
r_json = requests.post(url_json,data_json)
print(r_json)
print(r_json.text)
print(r_json.content)

























'''r = requests.post(url, data=json.dumps({"reqCode": "468513",'tasktyp':'move','usercallcode':'AA','usercallcodepath':['BB'],'podCode':'111111' ""
}))
print(r.json())'''

'''#请求api地址
url ="http://115.236.50.12:808/rcs/services/rest/hikRpcService"
#请求参数
data={"reqCode":"121312312",'taskTyp':'move','userCallCode':'AA','userCallCodePath':['BB'],'podCode':'111111'}
#执行请求
response= requests.get(url,params=data)
#查看执行的url
print('\n查看请求执行的url:\n',response.url)
#获得请求的内容
print('\n获得请求的内容:\n' , response.text)
#解析获取的json数据
data_json = json.loads(response.text)
print('\n解析获取json中data的值:\n',data_json['data'])'''

