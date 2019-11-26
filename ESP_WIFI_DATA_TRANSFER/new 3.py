#python实现tcp服务器客户端（支持多客户端）

1、只支持一个客户端访问
服务器：

from socket import *
address='127.0.0.1'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=12345             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(1)     #最大连接数
while True:
    clientsock,clientaddress=s.accept()
    print('connect from:',clientaddress)
#传输数据都利用clientsock，和s无关
    while True:  
        recvdata=clientsock.recv(buffsize).decode('utf-8')
        if recvdata=='exit' or not recvdata:
            break
        senddata=recvdata+'from sever'
        clientsock.send(senddata.encode())
    clientsock.close()
s.close()


客户端：

from socket import *
address='127.0.0.1'   #服务器的ip地址
port=12345           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
while True:
    senddata=input('想要发送的数据：')
    if senddata=='exit':
        break
    s.send(senddata.encode())
    recvdata=s.recv(buffsize).decode('utf-8')
    print(recvdata)
s.close()


2、支持多个客户端并发访问
服务器：

from socket import *
import threading
address='127.0.0.1'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=12345             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(2)     #最大连接数

def tcplink(sock,addr):
    while True:  
        recvdata=clientsock.recv(buffsize).decode('utf-8')
        if recvdata=='exit' or not recvdata:
            break
        senddata=recvdata+'from sever'
        clientsock.send(senddata.encode())
    clientsock.close()

while True:
    clientsock,clientaddress=s.accept()
    print('connect from:',clientaddress)
#传输数据都利用clientsock，和s无关
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))  #t为新创建的线程
    t.start()
s.close()


客户端：

#客户端与上一个没有任何改变
from socket import *
address='127.0.0.1'   #服务器的ip地址
port=12345           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
while True:
    senddata=input('想要发送的数据：')
    if senddata=='exit':
        break
    s.send(senddata.encode())
    recvdata=s.recv(buffsize).decode('utf-8')
    print(recvdata)
s.close()
————————————————
版权声明：本文为CSDN博主「gongdileidechouzhu」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/gongdileidechouzhu/article/details/78808557