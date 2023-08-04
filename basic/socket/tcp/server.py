import socket

# 1. 创建一个 tcp 套接字, AF_INET 表示 IPV4, SOCK_STREAM 表示 tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定本地信息
server_addr = ('', 5700)
server.bind(server_addr)

# 3. 将套接字的主动连接模式改为被动模式(监听)
server.listen(128)

# 4. 等待客户端连接, 会返回一个元组, 第一个元素为连接好的套接字, 使用该套接字进行后续操作, 第二个元素为连接的客户端信息
connect_sock, client_info = server.accept()
print(connect_sock, '----', client_info)

# 5. 接收/发送数据
while True:
    data = connect_sock.recv(1024)
    if len(data) == 0:
        connect_sock.close()
        break

    print(data.decode('UTF-8'))
    connect_sock.send('服务端返回响应消息'.encode('UTF-8'))

# 6. 关闭套接字
server.close()
