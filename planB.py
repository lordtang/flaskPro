# 方案B：使用redis作为缓存数据库，planB.py中轮询查看是否存在该数，存在则处理并返回结果
# 优点：简单
# 缺点：一直轮询比较浪费机器资源和性能
import redis

redis_client = redis.StrictRedis('127.0.0.1')

# redis是一个高性能数据库，常用在大数据领域和缓存服务器



def oper():
    while True:
        if redis_client.exists('data'):  # 如果redis中存在data
            data = redis_client.get('data').decode('utf-8')  # 取出data并解码
            redis_client.delete('data')  # 删除data
            return data
        else:
            continue


if __name__ == '__main__':
    ret = oper()
    print(ret)
