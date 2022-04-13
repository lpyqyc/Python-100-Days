"""
套接字 - 基于TCP协议创建时间服务器

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""

from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('服务器已经启动正在监听客户端连接.')
while True:
    client, address = server.accept()
    print('客户端%s:%d连接成功.' % (address[0], address[1]))
    curr_time = localtime(time())
    time_str = strftime('%Y-%m-%d %H:%M:%S', curr_time)
    client.send(time_str.encode('utf-8'))
    client.close()
server.close()
