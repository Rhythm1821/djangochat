import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            
        )