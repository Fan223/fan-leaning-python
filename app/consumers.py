# WebSocket 服务端

from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 接受这个客户端的连接
        self.accept()
        # 获取群号, 即路由匹配中的地址
        url_route = self.scope['url_route']
        print(url_route)
        group_id = url_route['kwargs'].get('group')
        # 将这个客户端的连接对象分组加入到内存或 Redis, 由配置决定使用内存还是 Redis
        # self.channel_layer.group_add('group_code', self.channel_name)  # group_add() 方法默认为异步
        async_to_sync(self.channel_layer.group_add)(group_id, self.channel_name)  # 转换为同步

    def websocket_receive(self, message):
        print('接收到的消息: ', message)
        group_id = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_send)(group_id, {'type': 'send_msg', 'message': message})

    def send_msg(self, event):
        text = event['message']['text']
        self.send(text)

    def websocket_disconnect(self, message):
        group_id = self.scope['url_route']['kwargs'].get('group')
        async_to_sync(self.channel_layer.group_discard)(group_id, self.channel_name)
        raise StopConsumer

# conn_list = []
#
#
# class ChatConsumer(WebsocketConsumer):
#     def websocket_connect(self, message):
#         # 有客户端来向服务端发送 WebSocket 连接的请求时自动触发
#         print('客户端发起连接')
#         # 服务端允许和客户端创建连接(握手)
#         self.accept()
#
#         # 添加进连接列表
#         conn_list.append(self)
#
#     def websocket_receive(self, message):
#         # 客户端基于 WebSocket 向服务端发送数据, 自动触发接收消息
#         print('接收到的消息: ', message)
#
#         # 服务端主动断开连接
#         if message.get('text') == '关闭':
#             self.close()
#             # raise StopConsumer
#             conn_list.remove(self)
#             return
#
#         for conn in conn_list:
#             conn.send(message.get('text'))
#
#     def websocket_disconnect(self, message):
#         # 客户端与服务端断开连接时自动触发
#         print('断开连接了')
#         conn_list.remove(self)
#         # 服务端同意断开连接
#         raise StopConsumer
