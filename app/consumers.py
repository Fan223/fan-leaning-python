from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 有客户端来向服务端发送 WebSocket 连接的请求时自动触发
        print('客户端发起连接')
        # 服务端允许和客户端创建连接(握手)
        self.accept()

    def websocket_receive(self, message):
        # 客户端基于 WebSocket 向服务端发送数据, 自动触发接收消息
        print('接收到的消息: ', message)

        # 服务端主动断开连接
        if message.get('text') == '关闭':
            self.close()
            # raise StopConsumer
            return
        self.send(message.get('text'))

    def websocket_disconnect(self, message):
        # 客户端与服务端断开连接时自动触发
        print('断开连接了')
        # 服务端同意断开连接
        raise StopConsumer
