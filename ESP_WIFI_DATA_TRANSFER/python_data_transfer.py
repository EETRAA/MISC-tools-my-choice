from socket import *
address='192.168.1.145'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
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
        print(recvdata)
        #senddata=recvdata+'from sever'
        #clientsock.send(senddata.encode())
    clientsock.close()
s.close()



from socket import *
address='192.168.1.145'   #服务器的ip地址
port=12345           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
while True:
    senddata=input('想要发送的数据：')
    if senddata=='exit':
        break
    s.send(senddata.encode())
    #recvdata=s.recv(buffsize).decode('utf-8')
    #print(recvdata)
s.close()
