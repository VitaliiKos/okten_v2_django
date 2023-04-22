from channels.db import database_sync_to_async
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class AutoParkConsumer(GenericAsyncAPIConsumer):

    def __init__(self, *args, **kwargs):
        self.room_name = None
        self.name = None
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            await self.close()

        self.room_name = self.scope['url_route']['kwargs']['room']

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        self.name= await self.get_profile_name()
        if self.room_name == 'chat':
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'sender',
                    'message': 'connected to chat',
                    'user': self.name
                }
            )
        await self.accept()

    @database_sync_to_async
    def get_profile_name(self):
        return self.scope['user'].profile.name

    async def sender(self, event):
        await self.send_json(event)

    @action()
    async def send_message(self, data, request_id, action):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'sender',
                'message': data,
                'user': self.name,
                'id': request_id
            }
        )
