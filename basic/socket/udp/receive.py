import socket

# 1. 创建一个 udp 套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 绑定目标 IP 地址和端口, 对接收方来说是本机 IP 地址
dest_addr = ('', 5700)  # 目标(接收方) IP 地址和端口, 即发送方的目标 IP 地址及端口
sock.bind(dest_addr)  # 绑定目标地址

# 3. 接收数据
while True:
    # msg = sock.recvfrom(1024)
    # print(msg)
    # print(msg[0].decode('UTF-8'))
    data, src_addr = sock.recvfrom(1024)
    print(data.decode('UTF-8'), src_addr)

    if data.decode('UTF-8') == 'quit':
        break

# 4. 关闭套接字
sock.close()
