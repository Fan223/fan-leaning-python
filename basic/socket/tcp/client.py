import socket

# 1. 创建一个 tcp 套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 连接服务器
server_addr = ('172.16.63.132', 5700)
client.connect(server_addr)

# 3. 发送数据
while True:
    data = input('请输入数据: ')
    client.send(data.encode('UTF-8'))

    response = client.recv(1024)
    print(response.decode('UTF-8'))

    if data == 'quit':
        break

# 4. 关闭套接字
client.close()
