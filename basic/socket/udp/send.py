import socket

# 1. 创建一个 udp 套接字, AF_INET 表示 IPV4, SOCK_DGRAM 表示 udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 绑定来源 IP 地址和端口, 对发送方来说就是本机 IP 地址; 不指定的话会默认绑定本机 IP 地址, 并绑定一个随机的端口
# src_addr = ('172.16.63.132', 5701)  # 来源地址(发送方地址), IP 写死
src_addr = ('', 5701)  # 推荐不写死, 置空的话会去获取本机(发送方)的 IP 地址
sock.bind(src_addr)  # 绑定来源地址

# 3. 发送数据
dest_addr = ('172.16.63.132', 5700)  # 目标地址(接收方地址)
while True:
    data = input('请输入发送数据: ')
    sock.sendto(data.encode('UTF-8'), dest_addr)  # 发送数据

    if data == 'quit':
        break
# 4. 关闭套接字
sock.close()
