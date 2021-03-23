'''
python 实现redis 集群的订阅发布功能
发布订阅模式的结构主要包含3个部分: 发布者、订阅者、channel

           channel msg          msg
publisher -------------channel---------subscriber_1
                               ---------          2
'''

import redis

class RedisHelper():
    def __init__(self):
        self._conn=redis.Redis(host='172.20.128.31',port=6379)
        self.channel='monitor' #定义名称

    def publish(self,msg):   #定义发布方法
        self._conn.publish(self.channel,msg)
        return True

    def subscribe(self):    #定义订阅方法
        pub=self._conn.pubsub()
        pub.subscribe(self.channel)   #订阅给定模式相匹配的频道
        pub.parse_response()
        return pub
    