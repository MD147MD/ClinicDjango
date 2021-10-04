import json
from channels.generic.websocket import WebsocketConsumer
from accounts.models import UserLoginAttempt
from django.core import serializers
from asgiref.sync import async_to_sync

class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.accept()
        see_sms_logs_permission_code = 71
        if self.user.is_authenticated and self.user.has_permission(see_sms_logs_permission_code):
            async_to_sync(self.channel_layer.group_add)("sms_logs", self.channel_name)
            attempts = UserLoginAttempt.objects.all().order_by("-created_at")[:20]
            data = serializers.serialize('json',attempts, use_natural_foreign_keys=True, use_natural_primary_keys=True,indent=2)
            # response = '{"type":"data","data":"'+ data + '"}'
            # print(response)
            self.send(data)
        else:
            self.channel_layer.group_discard

    # def disconnect(self, close_code):
    #     self.channel_layer.group_discard

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
    
    def append_data(self, event):
        self.send('{"type":"append","data":' + event["data"] + "}")
    

    def edit_data(self, event):
        self.send('{"type":"edit","data":' + event["data"] + "}")


        