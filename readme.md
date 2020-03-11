## 环境和运行步骤


### 需要安装的python环境：
```bash
pip install requests
pip install redis
```
### 需要的外部支持：

#### redis win10下的安装和启动：

- 在合适的目录下创建文件夹：redis
- 将解压Redis-x64-3.2.100.zip到redis文件夹下
- 双击运行 redis-server.exe启动redis服务器即可

### planA程序执行步骤 ：

- 运行app_service.py和planA.py
- 使用postman使用post调用app_service.py中的接口：http://127.0.0.1:5000/todo/api/v1.0/put 
- 参数示例为:
```json
{"data": 500}
```
- app_service.py程序在21行调用notice_handle()函数通知planA.py程序收到了客户端数据
- planA.py程序进行运算并将结果存入redis,并在23行调用requests.post('http://127.0.0.1:5001/api/v1.0/oper2')通知oper2函数进行运算
- oper2函数可以将oper函数运算后存入redis的结果再运算
- 需要取最终结果需要从redis取出即可，满足连续运算并实现了通知机制

### planB程序运算步骤：
- 注释掉planB中21行的notice_handle()函数
- 运行app_service.py,planB.py
- 使用postman使用post方法调用app_service.py中的接口：http://127.0.0.1:5000/todo/apip/v1.0/put
- 参数示例：
```json
{"data": 500}
```
- 查看程序planB的控制台，会有运算结果输出

####可能的问题：
- 如果不方便使用postman或者apidebug等浏览器插件，可以使用在线的api调试工具，比如https://www.sojson.com/http/test.html

