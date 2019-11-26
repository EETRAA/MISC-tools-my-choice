#!/usr/bin/env python

# _*_ coding:utf-8 _*_

import socket

import time

IP_PORT = ('127.0.0.1',8009)

BUF_SIZE = 1024

  

tcp_server = socket.socket()

tcp_server.bind(IP_PORT)

tcp_server.listen(5)

  

while True:

    print("waiting for connection...")

    conn,addr = tcp_server.accept()

    print("...connected from:",addr)

    while True:

        data = tcp_server.recv(BUF_SIZE)

        if not data:break

        tcp_server.send('[%s] %s'%(time.ctime(),data))

  

tcp_server.close()