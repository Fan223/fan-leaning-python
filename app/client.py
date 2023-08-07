# WebSocket 客户端

import websocket

# 1. 建立连接
ws = websocket.create_connection('ws://127.0.0.1:8000/ws/123/')
# 2. 获取连接状态
print("获取连接状态: ", ws.getstatus())

while True:
    msg = input('请输入内容: ')
    if msg == 'quit':
        break

    # 3. 发送信息
    ws.send(msg)
    # 4. 获取返回结果
    result = ws.recv()
    print("接收结果: ", result)

# 5. 关闭连接
ws.close()
