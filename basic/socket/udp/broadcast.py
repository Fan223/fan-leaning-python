import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 设置 udp 套接字允许广播
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 目标 IP 地址设为 <broadcast>
dest_addr = ('<broadcast>', 5701)

sock.sendto('hello'.encode('UTF-8'), dest_addr)
# 4. 关闭套接字
sock.close()
